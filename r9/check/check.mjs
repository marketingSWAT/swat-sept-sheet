const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const url = process.argv[2] || 'file:///home/james/swat/projects/swat-sept-sheet/site/index.html';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1440, height: 1000 } });
await p.goto(url, { waitUntil: 'load' });
for (const n of [68, 69, 70, 71, 72]) {
  await p.locator('#d' + n).scrollIntoViewIfNeeded();
  await p.evaluate(async (n) => { const d = document.getElementById('d' + n); for (const i of d.querySelectorAll('img')) { i.loading = 'eager'; } await Promise.all([...d.querySelectorAll('img')].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 8000); }))); }, n);
  await p.waitForTimeout(600);
  const r = await p.evaluate((n) => {
    const d = document.getElementById('d' + n);
    const rings = [...d.querySelectorAll('.ring')].map(x => ({ n: x.dataset.n, sel: x.dataset.sel, shown: getComputedStyle(x).display !== 'none' && x.offsetWidth > 0 }));
    const broken = [...d.querySelectorAll('img')].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(-60));
    const mocks = [...d.querySelectorAll('.mockwrap')].map(w => Math.round(w.getBoundingClientRect().height));
    return { rings: rings.filter(x => !x.shown), broken, mocks };
  }, n);
  console.log(n, JSON.stringify(r));
  await p.locator('#d' + n).screenshot({ path: `/home/james/swat/projects/swat-sept-sheet/r9/check/d${n}.png` });
}
await b.close();
