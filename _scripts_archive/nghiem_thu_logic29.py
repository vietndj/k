import asyncio
from playwright.async_api import async_playwright
import os
import shutil
import time
import requests

async def main():
    # Wait for the page to be accessible
    url = "https://fedu.vn/k/logic29.html"
    print(f"Checking deployment at {url}...")
    for i in range(5):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print("Page is live!")
                break
        except:
            pass
        print("Waiting...")
        time.sleep(10)

    # Output directory
    artifact_dir = "/Users/vietmac/.gemini/antigravity/brain/58267a6f-e34f-433e-a316-1939a01b12fe"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # 1. Desktop Test
        print("\n--- Testing Desktop ---")
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        js_errors = []
        page.on("pageerror", lambda err: js_errors.append(err.message))
        
        print("Navigating to URL...")
        response = await page.goto(url, wait_until="networkidle")
        if response.status != 200:
            print(f"Error: Server returned {response.status}")
        
        if js_errors:
            print(f"JS Errors: {js_errors}")
        else:
            print("No JS errors detected.")
            
        # Test TOC jump
        print("Clicking TOC link for Phần 2...")
        await page.click("a[href='#phan-2']")
        await page.wait_for_timeout(1000) # Give it a second to render
        
        # Check scroll position
        scroll_y = await page.evaluate("window.scrollY")
        print(f"Scroll position after jump: {scroll_y}")
        
        await page.screenshot(path=os.path.join(artifact_dir, "vision_logic29_desktop.png"))
        print("Screenshot saved.")
        await context.close()
        
        # 2. Mobile Test
        print("\n--- Testing Mobile ---")
        context_mobile = await browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1')
        page_mobile = await context_mobile.new_page()
        
        await page_mobile.goto(url, wait_until="networkidle")
        
        # Open TOC
        print("Opening Mobile TOC...")
        await page_mobile.click(".ink-menu-btn")
        await page_mobile.wait_for_timeout(500)
        
        # Click a link
        print("Clicking Q&A link...")
        await page_mobile.click("a[href='#p2_q5']")
        await page_mobile.wait_for_timeout(1000)
        
        scroll_y_mobile = await page_mobile.evaluate("window.scrollY")
        print(f"Scroll position after jump: {scroll_y_mobile}")
        
        await page_mobile.screenshot(path=os.path.join(artifact_dir, "vision_logic29_mobile.png"))
        print("Screenshot saved.")
        await context_mobile.close()
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
