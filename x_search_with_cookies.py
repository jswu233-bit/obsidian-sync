#!/usr/bin/env python3
"""
X (Twitter) 自动化脚本 - 使用 Cookies 登录
使用 Playwright
"""

import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

def search_x_with_cookies(search_query="openclaw"):
    """使用 cookies 登录 X 并搜索"""
    
    # 你的 cookies
    cookies = [
        {
            "name": "auth_token",
            "value": "b10b5cb100fa9c87db534746c4bf7b23d45eabc5",
            "domain": ".x.com",
            "path": "/",
            "httpOnly": True,
            "secure": True
        },
        {
            "name": "ct0",
            "value": "c607857c29764e3820c3cf17477306792697138d7c68548f709efcd2a4c1adbab59347842efc9c4c806586996b89f1439a390ba0f711fce6a6ea9e9abee6cefff97dbbb0efa3ba1cff13b9c24286bd94",
            "domain": ".x.com",
            "path": "/",
            "httpOnly": False,
            "secure": True
        },
        {
            "name": "guest_id",
            "value": "v1%3A177130196792033591",
            "domain": ".x.com",
            "path": "/",
            "httpOnly": False,
            "secure": True
        }
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        
        # 添加 cookies
        print("正在添加 cookies...")
        context.add_cookies(cookies)
        print("✓ Cookies 已添加")
        
        page = context.new_page()
        
        try:
            print("访问 X 首页...")
            page.goto("https://x.com/home", wait_until="networkidle")
            time.sleep(5)
            
            # 截图查看是否登录成功
            page.screenshot(path="/root/.openclaw/workspace/x_cookie_login.png")
            print(f"当前URL: {page.url}")
            
            # 检查是否已登录
            if "home" in page.url or "/x.com" in page.url:
                print("✅ Cookie 登录成功！")
                
                # 搜索 openclaw
                print(f"正在搜索: {search_query}")
                
                # 使用搜索框
                try:
                    search_input = page.locator('input[data-testid="SearchBox_Search_Input"]').first
                    search_input.wait_for(state="visible", timeout=10000)
                    search_input.fill(search_query)
                    search_input.press("Enter")
                    print("✓ 已提交搜索")
                    time.sleep(5)
                except Exception as e:
                    print(f"搜索框操作失败: {e}")
                    # 直接访问搜索URL
                    page.goto(f"https://x.com/search?q={search_query}&f=live")
                    time.sleep(5)
                
                # 等待加载
                page.wait_for_load_state("networkidle")
                time.sleep(3)
                
                # 截图保存
                screenshot_path = "/root/.openclaw/workspace/x_search_openclaw.png"
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"📸 搜索结果截图已保存")
                
                # 获取推文
                print("获取推文内容...")
                tweets_data = []
                try:
                    tweets = page.locator('article[data-testid="tweet"]').all()
                    print(f"找到 {len(tweets)} 条推文")
                    
                    for i, tweet in enumerate(tweets[:10]):
                        try:
                            text_elem = tweet.locator('[data-testid="tweetText"]').first
                            text = text_elem.inner_text(timeout=3000) if text_elem.is_visible() else ""
                            
                            author_elem = tweet.locator('a[role="link"] span').first
                            author = author_elem.inner_text(timeout=2000) if author_elem.is_visible() else "未知用户"
                            
                            time_elem = tweet.locator('time').first
                            tweet_time = time_elem.get_attribute('datetime') if time_elem.is_visible() else ""
                            
                            tweets_data.append({
                                "index": i + 1,
                                "author": author,
                                "time": tweet_time,
                                "text": text[:500] + "..." if len(text) > 500 else text
                            })
                            print(f"  推文 {i+1}: @{author} - {text[:100]}...")
                        except Exception as e:
                            print(f"  解析推文 {i+1} 失败: {e}")
                            continue
                except Exception as e:
                    print(f"获取推文列表失败: {e}")
                
                # 保存结果
                output = {
                    "success": True,
                    "query": search_query,
                    "url": page.url,
                    "tweet_count": len(tweets_data),
                    "tweets": tweets_data
                }
                
                # 保存到文件
                with open("/root/.openclaw/workspace/x_search_results_final.json", "w", encoding="utf-8") as f:
                    json.dump(output, f, ensure_ascii=False, indent=2)
                
                print("\n" + "="*60)
                print("搜索结果摘要:")
                print("="*60)
                print(f"关键词: {search_query}")
                print(f"找到推文: {len(tweets_data)} 条")
                print(f"截图: x_search_openclaw.png")
                print(f"详细结果: x_search_results_final.json")
                
                browser.close()
                return output
            else:
                print(f"❌ Cookie 登录失败，当前URL: {page.url}")
                # 可能是 cookies 过期
                output = {"success": False, "error": "Cookie login failed", "url": page.url}
                with open("/root/.openclaw/workspace/x_search_results_final.json", "w") as f:
                    json.dump(output, f)
                browser.close()
                return output
                
        except Exception as e:
            print(f"❌ 错误: {e}")
            page.screenshot(path="/root/.openclaw/workspace/x_cookie_error.png")
            browser.close()
            return {"success": False, "error": str(e)}

if __name__ == "__main__":
    query = os.environ.get("X_SEARCH_QUERY", "openclaw")
    print(f"开始执行 - 搜索关键词: {query}")
    print("="*60)
    
    result = search_x_with_cookies(query)
    print("\n" + "="*60)
    print("最终结果:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
