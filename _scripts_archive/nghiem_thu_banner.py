import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        failed_requests = []
        page.on("response", lambda response: failed_requests.append(response.url) if response.status >= 400 else None)
        
        print("Visiting https://fedu.vn/k/banner.html ...")
        await page.goto("https://fedu.vn/k/banner.html", wait_until="networkidle")
        
        # Scroll a bit to trigger lazy loaded images
        await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
        await page.wait_for_timeout(2000)
        
        await page.screenshot(path="nghiem_thu_banner.png", full_page=True)
        print(f"Captured screenshot to nghiem_thu_banner.png")
        if failed_requests:
            print("Failed requests:")
            for req in set(failed_requests):
                print(f"- {req}")
        else:
            print("No failed requests.")
            
        await browser.close()

asyncio.run(main())
