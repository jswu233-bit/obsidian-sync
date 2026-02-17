#!/usr/bin/env python3
"""
X (Twitter) 自动化脚本 - 登录并搜索 openclaw
使用 Playwright
"""

import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

def login_x(email, password, search_query="openclaw"):
    """登录 X 并搜索内容"""
    
    with sync_playwright() as p:
        # 启动浏览器（无头模式）
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        
        # 创建新页面
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page = context.new_page()
        
        try:
            print("正在访问 X 登录页面...")
            page.goto("https://x.com/i/flow/login", wait_until="networkidle")
            time.sleep(3)
            
            # 输入邮箱
            print("输入邮箱...")
            email_input = page.locator('input[autocomplete="username"]').first
            email_input.fill(email)
            time.sleep(1)
            
            # 点击下一步
            next_button = page.locator('button:has-text("Next")').first
            next_button.click()
            time.sleep(2)
            
            # 检查是否需要输入用户名（异常检测）
            try:
                username_input = page.locator('input[data-testid="ocfEnterTextTextInput"]').first
                if username_input.is_visible(timeout=3000):
                    print("需要输入用户名...")
                    username_input.fill("jswu255")
                    page.locator('button:has-text("Next")').first.click()
                    time.sleep(2)
            except:
                pass
            
            # 输入密码
            print("输入密码...")
            password_input = page.locator('input[name="password"]').first
            password_input.fill(password)
            time.sleep(1)
            
            # 点击登录
            login_button = page.locator('button[data-testid="LoginForm_Login_Button"]').first
            login_button.click()
            print("正在登录...")
            time.sleep(5)
            
            # 检查是否登录成功
            if "home" in page.url or "x.com" in page.url:
                print("✅ 登录成功！")
                
                # 搜索 openclaw
                print(f"正在搜索: {search_query}")
                search_box = page.locator('input[data-testid="SearchBox_Search_Input"]').first
                search_box.fill(search_query)
                search_box.press("Enter")
                time.sleep(5)
                
                # 等待搜索结果加载
                page.wait_for_load_state("networkidle")
                time.sleep(3)
                
                # 获取页面内容
                print("获取搜索结果...")
                tweets = page.locator('article[data-testid="tweet"]').all()
                
                results = []
                for i, tweet in enumerate(tweets[:10]):  # 获取前10条
                    try:
                        text = tweet.locator('[data-testid="tweetText"]').first.inner_text(timeout=3000)
                        author = tweet.locator('a[role="link"] span').first.inner_text(timeout=2000)
                        results.append({
                            "author": author,
                            "text": text[:200] + "..." if len(text) > 200 else text
                        })
                    except:
                        continue
                
                # 截图保存
                screenshot_path = "/root/.openclaw/workspace/x_search_results.png"
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"📸 截图已保存: {screenshot_path}")
                
                # 保存结果
                output = {
                    "success": True,
                    "query": search_query,
                    "tweet_count": len(results),
                    "tweets": results
                }
                
                print(json.dumps(output, ensure_ascii=False, indent=2))
                
                # 保存到文件
                with open("/root/.openclaw/workspace/x_search_results.json", "w", encoding="utf-8") as f:
                    json.dump(output, f, ensure_ascii=False, indent=2)
                
                browser.close()
                return output
            else:
                print("❌ 登录失败")
                screenshot_path = "/root/.openclaw/workspace/x_login_failed.png"
                page.screenshot(path=screenshot_path)
                browser.close()
                return {"success": False, "error": "Login failed"}
                
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
            try:
                page.screenshot(path="/root/.openclaw/workspace/x_error.png")
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
    
    result = login_x(email, password, query)
    sys.exit(0 if result.get("success") else 1)
