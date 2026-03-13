#!/usr/bin/env python3
"""
X (Twitter) 自动化脚本 - 使用 Cookies 快速搜索
"""

import os
import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

def _resolve_output_dir() -> Path:
    """Resolve a writable output directory with safe fallbacks."""
    candidates = []

    env_dir = os.environ.get("X_SEARCH_OUTPUT_DIR")
    if env_dir:
        candidates.append(Path(env_dir).expanduser())

    candidates.extend([
        Path(__file__).resolve().parent,
        Path.cwd(),
        Path.home() / ".openclaw" / "tmp",
        Path("/tmp"),
    ])

    for candidate in candidates:
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            probe = candidate / ".x_quick_write_test"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink(missing_ok=True)
            return candidate
        except Exception:
            continue

    raise RuntimeError("No writable output directory found for x_quick_search")


def quick_search_x(search_query="openclaw"):
    """使用 cookies 快速搜索 X"""

    output_dir = _resolve_output_dir()
    screenshot_path = output_dir / "x_search_final.png"
    summary_path = output_dir / "x_search_summary.json"
    error_path = output_dir / "x_quick_error.png"

    cookies = [
        {
            "name": "auth_token",
            "value": "1888150ab680b69516e9900c084294ec46802ccd",
            "domain": ".x.com",
            "path": "/",
            "httpOnly": True,
            "secure": True
        },
        {
            "name": "ct0",
            "value": "b2423ca9468b32039c444fe7c1e510d16f91b036160037b7677eb7a8ed1fc44dee932d461aeacdaadd9515b676697932ea598b66e68ddc911c0389527dc3a6845786e28fb34d326e6634231beb6c4875",
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
            viewport={'width': 1920, 'height': 1080}
        )
        
        context.add_cookies(cookies)
        page = context.new_page()
        
        try:
            print("访问 X 并搜索...")
            # 直接访问搜索页面
            search_url = f"https://x.com/search?q={search_query}&f=live"
            page.goto(search_url, wait_until="domcontentloaded")
            time.sleep(8)  # 等待内容加载
            
            # 截图
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"✓ 截图已保存: {screenshot_path}")
            
            # 快速获取可见推文
            print("获取推文...")
            tweets = []
            try:
                articles = page.locator('article').all()
                for i, article in enumerate(articles[:5]):
                    try:
                        # 直接获取整个 article 的文本
                        text = article.inner_text(timeout=5000)
                        tweets.append(text[:400])
                    except:
                        continue
            except Exception as e:
                print(f"获取推文失败: {e}")
            
            result = {
                "success": True,
                "query": search_query,
                "url": page.url,
                "tweet_count": len(tweets),
                "tweets": tweets
            }
            
            with open(summary_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            print(f"\n✅ 完成！找到 {len(tweets)} 条推文")
            print(f"截图: {screenshot_path}")
            print(f"摘要: {summary_path}")
            
            browser.close()
            return result
            
        except Exception as e:
            print(f"❌ 错误: {e}")
            try:
                page.screenshot(path=str(error_path))
                print(f"错误截图: {error_path}")
            except Exception as screenshot_error:
                print(f"保存错误截图失败: {screenshot_error}")
            browser.close()
            return {"success": False, "error": str(e)}

if __name__ == "__main__":
    query = os.environ.get("X_SEARCH_QUERY", "openclaw")
    print(f"搜索: {query}")
    result = quick_search_x(query)
    print(json.dumps(result, ensure_ascii=False, indent=2)[:2000])
