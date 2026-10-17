import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("http://localhost:8000/anh.html")
        await page.wait_for_timeout(2000)
        
        full_text_norm = await page.evaluate("""() => {
            let p = allPosters.find(x => x.style === "Google Flow");
            if (!p) return "Not found Google Flow item";
            let arr = [p.title, p.poem, p.id, p.prompt, p.category, p.style, p.movie_reference];
            let str = arr.filter(Boolean).join(' ');
            return removeAccents(str);
        }""")
        print(f"Google Flow item: {full_text_norm[:200]}")
        
        await browser.close()
        
asyncio.run(main())
