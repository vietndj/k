import asyncio
from playwright.async_api import async_playwright
import sys

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        url = "http://localhost:8000/anh.html"
        print(f"Loading {url}...")
        await page.goto(url)
        await page.wait_for_timeout(2000)
        
        # Type "tướng" into search box
        print("Searching for 'tướng'...")
        await page.fill('#searchInput', 'tướng')
        await page.wait_for_timeout(1000)
        
        count = await page.evaluate("document.querySelectorAll('.poster-card').length")
        print(f"Cards found for 'tướng': {count}")
        
        # Type "google flow" into search box
        print("Searching for 'google flow'...")
        await page.fill('#searchInput', 'google flow')
        await page.wait_for_timeout(1000)
        
        count = await page.evaluate("document.querySelectorAll('.poster-card').length")
        print(f"Cards found for 'google flow': {count}")
        
        await browser.close()
        
asyncio.run(main())
