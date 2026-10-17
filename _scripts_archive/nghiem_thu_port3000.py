import asyncio
from playwright.async_api import async_playwright
import sys

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        url = "http://localhost:3000/anh.html"
        print(f"Loading {url}...")
        try:
            await page.goto(url)
            await page.wait_for_timeout(2000)
            await page.screenshot(path="nghiem_thu_3000.jpg", full_page=False)
            print("Screenshot saved to nghiem_thu_3000.jpg")
        except Exception as e:
            print("Error:", e)
        await browser.close()
        
asyncio.run(main())
