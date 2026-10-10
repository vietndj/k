import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        print("Visiting https://fedu.vn/k/banner.html?v=200 ...")
        # Wait for all network connections to finish
        await page.goto("https://fedu.vn/k/banner.html?v=200", wait_until="networkidle", timeout=120000)
        
        print("Taking full page screenshot...")
        await page.screenshot(path="/Users/vietmac/.gemini/antigravity/brain/b3d9f590-9e38-48e8-98cd-ba9653631fe4/nghiem_thu_final.png", full_page=True, timeout=120000)
        print("Done.")
        await browser.close()

asyncio.run(main())
