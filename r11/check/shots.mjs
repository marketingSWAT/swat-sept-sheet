const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
const url = process.argv[2] || 'file:///home/james/swat/projects/swat-sept-sheet/site/index.html';
await page.goto(url, { waitUntil: 'load' });
await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 900) { scrollTo(0, y); await new Promise(r => setTimeout(r, 30)); } });
await page.waitForTimeout(4000);
const ids = ['r11s', 'd75', 'd76', 'd77', 'd78', 'd79', 'r11w'];
for (const id of ids) {
  const el = await page.$('#' + id);
  await el.screenshot({ path: `/home/james/swat/projects/swat-sept-sheet/r11/check/${id}-${process.env.V || 0}.png` });
}
const rep = await page.evaluate(() => {
  const out = [];
  for (const id of ['d75', 'd76', 'd77', 'd78', 'd79']) {
    const d = document.getElementById(id);
    const imgs = [...d.querySelectorAll('.mock img')];
    const broken = imgs.filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(-60));
    const rings = [...d.querySelectorAll('.ring')];
    const shown = rings.filter(r => getComputedStyle(r).display !== 'none' && r.offsetWidth > 0).length;
    const heights = [...d.querySelectorAll('.mockwrap')].map(w => Math.round(w.getBoundingClientRect().height));
    out.push({ id, imgs: imgs.length, broken, rings: rings.length, shown, heights });
  }
  return out;
});
console.log(JSON.stringify(rep, null, 1));
await browser.close();
