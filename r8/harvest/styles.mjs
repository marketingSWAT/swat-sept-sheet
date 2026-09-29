const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const p = await ctx.newPage();
await p.goto(`${base}/tours/mighty-5-utah-from-las-vegas/`, { waitUntil: 'networkidle' });
const o = await p.evaluate(() => {
  const s = (el) => { if(!el) return null; const c = getComputedStyle(el); const b = el.getBoundingClientRect(); return { t: el.textContent.trim().slice(0,40), fs: c.fontSize, fw: c.fontWeight, lh: c.lineHeight, ff: c.fontFamily.slice(0,40), col: c.color, bg: c.backgroundColor, pad: c.padding, rad: c.borderRadius, w: Math.round(b.width), h: Math.round(b.height), x: Math.round(b.x), y: Math.round(b.y+scrollY) }; };
  const sec = document.getElementById('departures');
  const h2 = sec.closest('section')?.querySelector('h2') || document.evaluate("//h2[text()='Departures']", document, null, 9).singleNodeValue;
  return {
    h2: s(h2), intro: s(sec.querySelector('p')), month: s(sec.querySelector('h3')), date: s(sec.querySelector('li p')),
    reserve: s(sec.querySelector('li a.bg-rust-600, li a')), sold: s([...sec.querySelectorAll('li span span')].find(x=>/Sold/i.test(x.textContent))),
    join: s([...sec.querySelectorAll('li a')].find(x=>/Join/.test(x.textContent))), summary: s(sec.querySelector('summary')),
    li: s(sec.querySelector('li')), railCta: s([...document.querySelectorAll('aside a, aside button')].find(x=>/Choose your date/.test(x.textContent))),
    pricingH2: s(document.evaluate("//h2[text()='Pricing']", document, null, 9).singleNodeValue),
    sectionTop: s(h2?.parentElement), body: getComputedStyle(document.body).fontFamily
  };
});
console.log(JSON.stringify(o, null, 1));
await browser.close();
