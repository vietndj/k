import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        requests = []
        page.on("request", lambda req: requests.append(req.url))
        page.on("response", lambda res: print(f"{res.status} {res.url}") if "media.fedu.vn" in res.url else None)
        
        await page.goto("https://fedu.vn/k/banner.html?v=11")
        
        # Scroll down completely
        height = await page.evaluate("document.body.scrollHeight")
        for i in range(0, height, 500):
            await page.evaluate(f"window.scrollTo(0, {i})")
            await page.wait_for_timeout(100)
            
        print(f"Total requests: {len(requests)}")
        
        await browser.close()

asyncio.run(main())
