import asyncio
from playwright.async_api import async_playwright
import sys

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # 1920x1080 resolution for better UI preview
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        url = "http://localhost:8000/anh.html"
        print(f"Loading {url}...")
        await page.goto(url)
        await page.wait_for_timeout(3000) # Wait for fetch, render and fonts
        
        # Take a screenshot
        await page.screenshot(path="nghiem_thu_ui.jpg", full_page=False)
        print("Screenshot saved to nghiem_thu_ui.jpg")
        
        await browser.close()
        
asyncio.run(main())
