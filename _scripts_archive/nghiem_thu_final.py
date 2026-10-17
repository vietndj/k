import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        failed_requests = []
        page.on("response", lambda response: failed_requests.append(response.url) if response.status >= 400 else None)
        
        print("Visiting https://fedu.vn/k/banner.html?v=3 ...")
        await page.goto("https://fedu.vn/k/banner.html?v=3", wait_until="networkidle")
        
        await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
        await page.wait_for_timeout(2000)
        
        await page.screenshot(path="/Users/vietmac/.gemini/antigravity/brain/b3d9f590-9e38-48e8-98cd-ba9653631fe4/nghiem_thu_final.png", full_page=True)
        print("Captured screenshot.")
        if failed_requests:
            print("Failed requests:", set(failed_requests))
        await browser.close()

asyncio.run(main())
