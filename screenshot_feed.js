const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  
  await page.goto('http://localhost:8000/index.html');
  await page.waitForTimeout(3000); // Wait for feed to load and images to fetch
  
  await page.screenshot({ path: 'screenshot_final_feed.png', fullPage: true });
  
  await browser.close();
})();
