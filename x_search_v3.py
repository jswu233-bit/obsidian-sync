#!/usr/bin/env python3
"""
X (Twitter) 自动化脚本 - 登录并搜索 openclaw
使用 Playwright - v3 调试版
"""

import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

def login_x(email, password, search_query="openclaw"):
    """登录 X 并搜索内容"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )
        page = context.new_page()
        
        try:
            print("1. 访问 X 登录页面...")
            page.goto("https://x.com/i/flow/login", wait_until="networkidle")
            time.sleep(5)
            page.screenshot(path="/root/.openclaw/workspace/x_debug_1_initial.png")
            
            # 获取页面文本内容
            print("页面文本内容预览:")
            page_text = page.inner_text("body")[:500]
            print(page_text)
            print("-" * 50)
            
            print("2. 查找输入框...")
            # 查找所有输入框
            inputs = page.locator('input').all()
            print(f"找到 {len(inputs)} 个输入框")
            for i, inp in enumerate(inputs):
                try:
                    input_type = inp.get_attribute('type') or 'text'
                    input_name = inp.get_attribute('name') or ''
                    placeholder = inp.get_attribute('placeholder') or ''
                    print(f"  输入框 {i}: type={input_type}, name={input_name}, placeholder={placeholder[:30]}")
                except:
                    pass
            
            # 输入用户名
            print("3. 尝试输入用户名 jswu255...")
            try:
                # 尝试找到用户名输入框
                username_input = page.locator('input').first
                username_input.fill("jswu255")
                print("✓ 用户名已输入")
                time.sleep(2)
                page.screenshot(path="/root/.openclaw/workspace/x_debug_2_username_filled.png")
            except Exception as e:
                print(f"输入用户名失败: {e}")
                raise
            
            # 点击下一步按钮
            print("4. 查找并点击下一步按钮...")
            buttons = page.locator('button').all()
            print(f"找到 {len(buttons)} 个按钮")
            for i, btn in enumerate(buttons[:5]):
                try:
                    btn_text = btn.inner_text()
                    print(f"  按钮 {i}: {btn_text[:50]}")
                except:
                    pass
            
            # 点击第一个可见的按钮
            next_btn = page.locator('button').first
            next_btn.click()
            print("✓ 已点击按钮")
            time.sleep(5)  # 等待页面跳转
            
            print(f"当前URL: {page.url}")
            page.screenshot(path="/root/.openclaw/workspace/x_debug_3_after_click.png")
            
            # 再次获取页面文本
            print("点击后的页面内容:")
            page_text2 = page.inner_text("body")[:500]
            print(page_text2)
            print("-" * 50)
            
            # 查找密码输入框
            print("5. 查找密码输入框...")
            time.sleep(3)
            
            inputs2 = page.locator('input').all()
            print(f"找到 {len(inputs2)} 个输入框")
            for i, inp in enumerate(inputs2):
                try:
                    input_type = inp.get_attribute('type') or 'text'
                    input_name = inp.get_attribute('name') or ''
                    print(f"  输入框 {i}: type={input_type}, name={input_name}")
                except:
                    pass
            
            # 尝试输入密码
            print("6. 尝试输入密码...")
            password_input = None
            for inp in inputs2:
                try:
                    input_type = inp.get_attribute('type')
                    if input_type == 'password':
                        password_input = inp
                        break
                except:
                    continue
            
            if password_input:
                password_input.fill(password)
                print("✓ 密码已输入")
                time.sleep(2)
                page.screenshot(path="/root/.openclaw/workspace/x_debug_4_password_filled.png")
            else:
                print("未找到密码输入框，可能是需要处理其他步骤")
                # 尝试按回车或查找其他按钮
                page.keyboard.press("Enter")
                time.sleep(3)
                page.screenshot(path="/root/.openclaw/workspace/x_debug_5_after_enter.png")
            
            print("7. 尝试登录...")
            # 查找登录按钮
            login_buttons = page.locator('button').all()
            for btn in login_buttons:
                try:
                    btn_text = btn.inner_text().lower()
                    if 'log in' in btn_text or '登录' in btn_text or 'sign in' in btn_text:
                        btn.click()
                        print(f"✓ 点击登录按钮: {btn_text}")
                        break
                except:
                    pass
            else:
                # 如果没有找到特定按钮，按回车
                page.keyboard.press("Enter")
                print("✓ 按回车键登录")
            
            time.sleep(5)
            print(f"登录后URL: {page.url}")
            page.screenshot(path="/root/.openclaw/workspace/x_debug_6_after_login.png")
            
            # 检查是否成功
            if "home" in page.url or "/x.com" in page.url:
                print("✅ 登录成功！")
                
                # 搜索
                print(f"8. 搜索: {search_query}")
                page.goto(f"https://x.com/search?q={search_query}&f=live")
                time.sleep(5)
                page.screenshot(path="/root/.openclaw/workspace/x_search_results.png")
                
                output = {
                    "success": True,
                    "query": search_query,
                    "url": page.url
                }
                
                with open("/root/.openclaw/workspace/x_search_results.json", "w") as f:
                    json.dump(output, f)
                
                browser.close()
                return output
            else:
                print(f"❌ 登录可能失败，当前URL: {page.url}")
                return {"success": False, "url": page.url}
                
        except Exception as e:
            print(f"❌ 错误: {e}")
            page.screenshot(path="/root/.openclaw/workspace/x_debug_error.png")
            browser.close()
            return {"success": False, "error": str(e)}

if __name__ == "__main__":
    password = os.environ.get("X_PASSWORD")
    query = os.environ.get("X_SEARCH_QUERY", "openclaw")
    
    if not password:
        print("错误: 请设置 X_PASSWORD 环境变量")
        sys.exit(1)
    
    result = login_x("jingshanwu@126.com", password, query)
    print(json.dumps(result, indent=2))
