const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
await page.goto('file:///home/james/swat/projects/swat-sept-sheet/site/index.html', { waitUntil: 'load' });
await page.waitForTimeout(1500);
console.log(JSON.stringify(await page.evaluate((sels) => {
  const mk = document.querySelector('#d75 .mock'); const s = mk.getBoundingClientRect(); const k = s.width / 1440;
  return sels.map(q => { const e = mk.querySelector(q); if (!e) return [q, null]; const b = e.getBoundingClientRect(); return [q, Math.round((b.top - s.top) / k), Math.round(b.height / k)]; });
}, ['.w9-strip', '.w9-hd', '.w9-tick', '.w11-hero', '.w11-find', '.w11-pop', '.w11-map', '.w11-map h2', '.w9-nav'])));
await browser.close();
