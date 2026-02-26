#!/usr/bin/env python3
"""
小红书内容抓取脚本
基于 x-reader 的方法：Playwright + Jina Reader 降级策略
"""

import asyncio
import re
import json
from typing import Optional, Dict, Any
from urllib.parse import quote

from playwright.async_api import async_playwright


async def fetch_xiaohongshu_search(keyword: str, limit: int = 10) -> list:
    """
    抓取小红书搜索结果
    
    Args:
        keyword: 搜索关键词
        limit: 返回结果数量
        
    Returns:
        笔记列表，包含 title, content, url, author 等
    """
    encoded_keyword = quote(keyword)
    search_url = f"https://www.xiaohongshu.com/search_result?keyword={encoded_keyword}"
    
    results = []
    
    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        
        page = await context.new_page()
        
        try:
            # 访问搜索页面
            print(f"正在搜索: {keyword}")
            await page.goto(search_url, wait_until="networkidle", timeout=30000)
            
            # 等待内容加载 - 使用更通用的选择器
            await asyncio.sleep(5)  # 等待页面完全加载
            
            # 保存页面源码用于调试
            html = await page.content()
            with open('/tmp/xhs_debug.html', 'w', encoding='utf-8') as f:
                f.write(html[:50000])  # 保存前50KB
            print("页面源码已保存到 /tmp/xhs_debug.html")
            
            # 提取笔记信息 - 尝试多种可能的选择器
            notes = await page.query_selector_all('section.note-item, div.note-item, a[href*="/explore/"], .feeds-page .note-item, .search-result-item')
            
            print(f"找到 {len(notes)} 个笔记元素")
            
            for i, note in enumerate(notes[:limit]):
                try:
                    # 提取标题
                    title_elem = await note.query_selector('span.title, .title, h3, .note-title')
                    title = await title_elem.inner_text() if title_elem else ""
                    
                    # 提取内容摘要
                    content_elem = await note.query_selector('span.desc, .desc, .content, .note-content')
                    content = await content_elem.inner_text() if content_elem else ""
                    
                    # 提取链接
                    link_elem = await note.query_selector('a[href*="/explore/"]')
                    href = await link_elem.get_attribute('href') if link_elem else ""
                    if href and not href.startswith('http'):
                        href = f"https://www.xiaohongshu.com{href}"
                    
                    # 提取作者
                    author_elem = await note.query_selector('.author, .user-name, .nickname')
                    author = await author_elem.inner_text() if author_elem else ""
                    
                    # 提取点赞数
                    likes_elem = await note.query_selector('.like-count, .count, span:has-text("赞")')
                    likes = await likes_elem.inner_text() if likes_elem else ""
                    
                    if title or content:
                        results.append({
                            "title": title.strip(),
                            "content": content.strip(),
                            "url": href,
                            "author": author.strip(),
                            "likes": likes.strip()
                        })
                        
                except Exception as e:
                    print(f"提取第 {i+1} 个笔记时出错: {e}")
                    continue
            
        except Exception as e:
            print(f"抓取过程出错: {e}")
            
        finally:
            await browser.close()
    
    return results


async def fetch_xiaohongshu_note(url: str) -> Optional[Dict[str, Any]]:
    """
    抓取单篇小红书笔记详情
    
    Args:
        url: 笔记链接
        
    Returns:
        笔记详情，包含 title, content, images, author 等
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        
        page = await context.new_page()
        
        try:
            print(f"正在抓取笔记: {url}")
            await page.goto(url, wait_until="networkidle", timeout=30000)
            await asyncio.sleep(2)
            
            # 提取标题
            title_selectors = ['h1.title', '.title', 'h1', '.note-title']
            title = ""
            for selector in title_selectors:
                try:
                    elem = await page.query_selector(selector)
                    if elem:
                        title = await elem.inner_text()
                        if title.strip():
                            break
                except:
                    continue
            
            # 提取正文内容
            content_selectors = ['div.content', '.content', '.note-content', '.desc']
            content = ""
            for selector in content_selectors:
                try:
                    elem = await page.query_selector(selector)
                    if elem:
                        content = await elem.inner_text()
                        if content.strip():
                            break
                except:
                    continue
            
            # 提取作者
            author_selectors = ['.author-name', '.nickname', '.user-name']
            author = ""
            for selector in author_selectors:
                try:
                    elem = await page.query_selector(selector)
                    if elem:
                        author = await elem.inner_text()
                        if author.strip():
                            break
                except:
                    continue
            
            # 提取图片
            images = await page.query_selector_all('img[src*="xiaohongshu"], img[src*="xhscdn"]')
            image_urls = []
            for img in images[:9]:  # 最多9张图
                src = await img.get_attribute('src')
                if src:
                    image_urls.append(src)
            
            await browser.close()
            
            return {
                "title": title.strip(),
                "content": content.strip(),
                "author": author.strip(),
                "url": url,
                "images": image_urls
            }
            
        except Exception as e:
            print(f"抓取笔记出错: {e}")
            await browser.close()
            return None


async def main():
    """主函数 - 搜索雅加达餐厅"""
    keyword = "雅加达餐厅"
    
    print(f"=== 搜索小红书: {keyword} ===\n")
    
    results = await fetch_xiaohongshu_search(keyword, limit=10)
    
    if not results:
        print("未找到结果，尝试直接抓取具体笔记...")
        return
    
    print(f"\n=== 找到 {len(results)} 条结果 ===\n")
    
    for i, note in enumerate(results, 1):
        print(f"【{i}】{note.get('title', '无标题')}")
        print(f"    作者: {note.get('author', '未知')}")
        print(f"    内容: {note.get('content', '')[:100]}...")
        print(f"    链接: {note.get('url', '')}")
        print(f"    点赞: {note.get('likes', '')}")
        print()
    
    # 保存结果
    output_file = f"/root/.openclaw/workspace/xiaohongshu_{keyword}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"结果已保存到: {output_file}")


if __name__ == "__main__":
    asyncio.run(main())
