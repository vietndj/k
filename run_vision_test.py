import asyncio
from playwright.async_api import async_playwright
import json
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # Desktop
        context_desktop = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page_desktop = await context_desktop.new_page()
        console_errors_desk = []
        page_desktop.on('console', lambda msg: console_errors_desk.append(msg.text) if msg.type == 'error' else None)
        page_desktop.on('pageerror', lambda err: console_errors_desk.append(str(err)))
        
        url = f"file://{os.path.abspath('giai-ma-tam-ly-hoang-loan-sau-sac.html')}"
        await page_desktop.goto(url, wait_until='networkidle')
        await page_desktop.screenshot(path='vision_report_desktop.png')
        
        dom_report_desktop = await page_desktop.evaluate('''() => {
            const checks = {};
            checks.consoleErrors = window.__capturedErrors || [];
            const targets = document.querySelectorAll('[data-qa], header, nav, footer, h1, h2, .logo, img, button, a.cta, .ink-sidebar, .ink-overlay');
            checks.elements = [...targets].map(el => {
                const rect = el.getBoundingClientRect();
                const style = getComputedStyle(el);
                return {
                    tag: el.tagName,
                    id: el.id || el.dataset?.qa || '',
                    classes: el.className,
                    text: el.textContent?.slice(0, 80) || '',
                    visible: rect.width > 0 && rect.height > 0 
                             && style.display !== 'none' 
                             && style.visibility !== 'hidden'
                             && parseFloat(style.opacity) > 0,
                    rect: {x: Math.round(rect.x), y: Math.round(rect.y), w: Math.round(rect.width), h: Math.round(rect.height)},
                    font: style.fontFamily,
                    fontSize: style.fontSize,
                    position: style.position,
                    zIndex: style.zIndex,
                    left: style.left
                };
            });
            checks.page = {
                scrollWidth: document.documentElement.scrollWidth,
                clientWidth: document.documentElement.clientWidth
            };
            return checks;
        }''')
        dom_report_desktop['consoleErrors'].extend(console_errors_desk)
        with open('dom_probe_desktop.json', 'w') as f:
            json.dump(dom_report_desktop, f, indent=2)
            
        # Mobile
        context_mobile = await browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True)
        page_mobile = await context_mobile.new_page()
        console_errors_mob = []
        page_mobile.on('console', lambda msg: console_errors_mob.append(msg.text) if msg.type == 'error' else None)
        page_mobile.on('pageerror', lambda err: console_errors_mob.append(str(err)))
        
        await page_mobile.goto(url, wait_until='networkidle')
        # Simulate open menu for mobile screenshot
        # await page_mobile.click('.ink-menu-btn')
        await page_mobile.screenshot(path='vision_report_mobile.png')
        
        dom_report_mobile = await page_mobile.evaluate('''() => {
            const checks = {};
            checks.consoleErrors = window.__capturedErrors || [];
            const targets = document.querySelectorAll('[data-qa], header, nav, footer, h1, h2, .logo, img, button, a.cta, .ink-sidebar, .ink-overlay, .ink-mobile-nav');
            checks.elements = [...targets].map(el => {
                const rect = el.getBoundingClientRect();
                const style = getComputedStyle(el);
                return {
                    tag: el.tagName,
                    id: el.id || el.dataset?.qa || '',
                    classes: el.className,
                    text: el.textContent?.slice(0, 80) || '',
                    visible: rect.width > 0 && rect.height > 0 
                             && style.display !== 'none' 
                             && style.visibility !== 'hidden'
                             && parseFloat(style.opacity) > 0,
                    rect: {x: Math.round(rect.x), y: Math.round(rect.y), w: Math.round(rect.width), h: Math.round(rect.height)},
                    font: style.fontFamily,
                    fontSize: style.fontSize,
                    position: style.position,
                    zIndex: style.zIndex,
                    left: style.left
                };
            });
            checks.page = {
                scrollWidth: document.documentElement.scrollWidth,
                clientWidth: document.documentElement.clientWidth
            };
            return checks;
        }''')
        dom_report_mobile['consoleErrors'].extend(console_errors_mob)
        with open('dom_probe_mobile.json', 'w') as f:
            json.dump(dom_report_mobile, f, indent=2)
            
        await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
