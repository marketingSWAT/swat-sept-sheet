const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1440, height: 1000 } });
await p.goto('file:///home/james/swat/projects/swat-sept-sheet/site/index.html', { waitUntil: 'load' });
for (const n of [68, 69, 70, 71, 72]) {
  const r = await p.evaluate((n) => {
    const out = [];
    document.querySelectorAll(`#d${n} .mock-bar`).forEach(bar => { bar.querySelector('button[data-w=phone]').click(); });
    document.querySelectorAll(`#d${n} .mockwrap.phone .mock`).forEach(m => { let over = 0; m.querySelectorAll('*').forEach(e => { const w = e.scrollWidth; if (e.offsetWidth > 392) over++; }); out.push([m.scrollWidth, over]); });
    return out;
  }, n);
  console.log(n, JSON.stringify(r));
}
await p.locator('#d68').screenshot({ path: 'r9/check/d68-phone.png' });
await b.close();
