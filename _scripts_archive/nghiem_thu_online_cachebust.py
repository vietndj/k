import asyncio
from playwright.async_api import async_playwright
import time

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        url = f"https://fedu.vn/k/anh.html?v={time.time()}"
        print(f"Loading {url}...")
        
        await page.goto(url)
        await page.wait_for_timeout(3000)
        
        header_text = await page.evaluate("() => { const h1 = document.querySelector('h1'); return h1 ? h1.innerText : ''; }")
        print(f"Header found: '{header_text}'")
        
        await page.screenshot(path="nghiem_thu_online.jpg", full_page=False)
        print("Screenshot saved to nghiem_thu_online.jpg")
        await browser.close()
        
asyncio.run(main())
