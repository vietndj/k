import asyncio
from playwright.async_api import async_playwright
import time

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        url = f"https://fedu.vn/k/anh.html?v={time.time()}"
        print(f"Loading {url}...")
        
        for i in range(3):
            await page.goto(url)
            await page.wait_for_timeout(3000)
            # check if Triết Lý / Văn Học is in the dropdown
            has_trietly = await page.evaluate("() => document.body.innerHTML.includes('Triết Lý')")
            if has_trietly:
                break
            print("Waiting for deploy...")
            await page.wait_for_timeout(10000)
        
        print("Deploy detected. Selecting Anime...")
        await page.select_option('#categoryFilter', 'Anime')
        await page.wait_for_timeout(1000)
        
        card_count = await page.evaluate("() => document.querySelectorAll('.poster-card').length")
        print(f"Cards found for Anime: {card_count}")
        
        await page.screenshot(path="nghiem_thu_filter_anime.jpg", full_page=False)
        print("Screenshot saved to nghiem_thu_filter_anime.jpg")
        await browser.close()
        
asyncio.run(main())
