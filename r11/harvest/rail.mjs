const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const page = await ctx.newPage();
const res = {};
for (const p of process.argv.slice(2)) {
  await page.goto(base + p, { waitUntil: 'load' });
  await page.waitForTimeout(800);
  res[p] = await page.evaluate(() => {
    const R = e => { const b = e.getBoundingClientRect(); return [Math.round(b.x), Math.round(b.y + scrollY), Math.round(b.width), Math.round(b.height)]; };
    const aside = [...document.querySelectorAll('aside')].map(a => ({ box: R(a), text: a.innerText.slice(0, 900) }));
    const ctas = [...document.querySelectorAll('a,button')].filter(e => { const b = e.getBoundingClientRect(); return b.x > 900 && b.y + scrollY < 1600 && b.width > 80 && e.innerText.trim(); }).map(e => ({ t: e.innerText.trim().slice(0, 60), box: R(e), href: e.getAttribute('href') }));
    const first = [...document.querySelectorAll('a,button')].filter(e => { const b = e.getBoundingClientRect(); return b.top >= 0 && b.bottom <= innerHeight && b.width > 60 && e.innerText.trim(); }).map(e => e.innerText.trim().slice(0, 40));
    return { aside, ctas, first };
  });
}
fs.writeFileSync(new URL('./rails.json', import.meta.url), JSON.stringify(res, null, 1));
await browser.close();
