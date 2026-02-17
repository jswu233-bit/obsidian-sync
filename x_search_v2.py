#!/usr/bin/env python3
"""
X (Twitter) 自动化脚本 - 登录并搜索 openclaw
使用 Playwright - 改进版
"""

import os
import sys
import json
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

def login_x(email, password, search_query="openclaw"):
    """登录 X 并搜索内容"""
    
    with sync_playwright() as p:
        # 启动浏览器（无头模式）
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-accelerated-2d-canvas',
                '--disable-gpu'
            ]
        )
        
        # 创建新页面
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = context.new_page()
        
        try:
            print("正在访问 X 登录页面...")
            page.goto("https://x.com/login", wait_until="domcontentloaded")
            time.sleep(5)
            
            # 截图查看初始页面
            page.screenshot(path="/root/.openclaw/workspace/x_step1_initial.png")
            print("✓ 页面已加载")
            
            # 输入邮箱/用户名 - 尝试多种选择器
            print("输入用户名...")
            try:
                # 尝试用户名输入框
                username_input = page.locator('input[autocomplete="username"], input[name="text"], input[type="text"]').first
                username_input.wait_for(state="visible", timeout=10000)
                username_input.fill("jswu255")  # 使用用户名而不是邮箱
                print("✓ 用户名已输入")
                time.sleep(2)
            except Exception as e:
                print(f"用户名输入失败: {e}")
                page.screenshot(path="/root/.openclaw/workspace/x_error_username.png")
                raise
            
            # 点击下一步
            print("点击下一步...")
            try:
                next_button = page.locator('button:has-text("Next"), button:has-text("下一步"), button[role="button"]').first
                next_button.click()
                print("✓ 已点击下一步")
                time.sleep(3)
            except Exception as e:
                print(f"点击下一步失败: {e}")
            
            # 截图查看当前状态
            page.screenshot(path="/root/.openclaw/workspace/x_step2_after_username.png")
            
            # 输入密码
            print("输入密码...")
            try:
                password_input = page.locator('input[type="password"], input[autocomplete="current-password"], input[name="password"]').first
                password_input.wait_for(state="visible", timeout=10000)
                password_input.fill(password)
                print("✓ 密码已输入")
                time.sleep(2)
            except Exception as e:
                print(f"密码输入失败: {e}")
                page.screenshot(path="/root/.openclaw/workspace/x_error_password.png")
                raise
            
            # 点击登录
            print("点击登录...")
            try:
                login_button = page.locator('button[data-testid="LoginForm_Login_Button"], button:has-text("Log in"), button:has-text("登录"), button[type="submit"]').first
                login_button.click()
                print("✓ 已点击登录")
            except Exception as e:
                print(f"点击登录失败: {e}")
                # 尝试按回车键
                page.keyboard.press("Enter")
            
            time.sleep(5)
            
            # 截图查看登录后状态
            page.screenshot(path="/root/.openclaw/workspace/x_step3_after_login.png")
            print(f"当前URL: {page.url}")
            
            # 检查是否登录成功
            if "home" in page.url or "/x.com/" in page.url or "twitter.com/home" in page.url:
                print("✅ 登录成功！")
                
                # 搜索 openclaw
                print(f"正在搜索: {search_query}")
                try:
                    # 点击搜索框
                    search_input = page.locator('input[data-testid="SearchBox_Search_Input"], input[placeholder*="Search"], input[type="text"]').first
                    search_input.wait_for(state="visible", timeout=10000)
                    search_input.fill(search_query)
                    search_input.press("Enter")
                    print("✓ 已提交搜索")
                    time.sleep(5)
                except Exception as e:
                    print(f"搜索失败: {e}")
                    # 直接访问搜索URL
                    page.goto(f"https://x.com/search?q={search_query}&f=live", wait_until="domcontentloaded")
                    time.sleep(5)
                
                # 等待搜索结果加载
                page.wait_for_load_state("networkidle", timeout=30000)
                time.sleep(3)
                
                # 截图保存
                screenshot_path = "/root/.openclaw/workspace/x_search_results.png"
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"📸 搜索结果截图已保存")
                
                # 获取推文内容
                print("获取推文内容...")
                tweets_data = []
                try:
                    tweets = page.locator('article[data-testid="tweet"]').all()
                    print(f"找到 {len(tweets)} 条推文")
                    
                    for i, tweet in enumerate(tweets[:5]):  # 获取前5条
                        try:
                            text_elem = tweet.locator('[data-testid="tweetText"]').first
                            text = text_elem.inner_text(timeout=3000) if text_elem.is_visible() else ""
                            
                            author_elem = tweet.locator('a[role="link"] span').first
                            author = author_elem.inner_text(timeout=2000) if author_elem.is_visible() else "未知用户"
                            
                            tweets_data.append({
                                "index": i + 1,
                                "author": author,
                                "text": text[:300] + "..." if len(text) > 300 else text
                            })
                        except Exception as e:
                            print(f"解析推文 {i+1} 失败: {e}")
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
                with open("/root/.openclaw/workspace/x_search_results.json", "w", encoding="utf-8") as f:
                    json.dump(output, f, ensure_ascii=False, indent=2)
                
                print("\n" + "="*50)
                print("搜索结果:")
                print("="*50)
                print(json.dumps(output, ensure_ascii=False, indent=2))
                
                browser.close()
                return output
            else:
                print(f"❌ 登录失败，当前URL: {page.url}")
                screenshot_path = "/root/.openclaw/workspace/x_login_failed.png"
                page.screenshot(path=screenshot_path)
                browser.close()
                return {"success": False, "error": f"Login failed, URL: {page.url}"}
                
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
            try:
                page.screenshot(path="/root/.openclaw/workspace/x_error_final.png")
                print("错误截图已保存")
            except:
                pass
            browser.close()
            return {"success": False, "error": str(e)}

if __name__ == "__main__":
    # 从环境变量获取凭证
    email = os.environ.get("X_EMAIL", "jingshanwu@126.com")
    password = os.environ.get("X_PASSWORD")
    query = os.environ.get("X_SEARCH_QUERY", "openclaw")
    
    if not password:
        print("错误: 请设置 X_PASSWORD 环境变量")
        sys.exit(1)
    
    print(f"开始执行 - 搜索关键词: {query}")
    print("="*50)
    
    result = login_x(email, password, query)
    sys.exit(0 if result.get("success") else 1)
