// Every live tour page at 1440: the booking rail's text and the departures section's text.
const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const paths = fs.readFileSync(new URL('./tours.txt', import.meta.url), 'utf8').trim().split('\n');
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const out = {};
async function one(p) {
  const page = await ctx.newPage();
  await page.goto(base + p, { waitUntil: 'load' });
  await page.waitForSelector('aside dl, #reserve, #departures', { timeout: 8000 }).catch(() => {});
  await page.waitForTimeout(1500);
  out[p] = await page.evaluate(() => {
    const aside = [...document.querySelectorAll('aside')].map(a => a.innerText).join('\n---\n');
    const dep = document.querySelector('#departures, #reserve');
    const h2s = [...document.querySelectorAll('main h2')].map(h => h.innerText.trim());
    const glance = [...document.querySelectorAll('dt')].map(d => [d.innerText.trim(), d.nextElementSibling?.innerText.trim()]);
    const book = [...document.querySelectorAll('a,button')].filter(e => /^Book$/.test(e.innerText.trim())).length;
    return { aside, dep: dep ? dep.innerText.slice(0, 4000) : null, h2s, glance, book };
  });
  await page.close();
}
for (let i = 0; i < paths.length; i += 4) await Promise.all(paths.slice(i, i + 4).map(one));
fs.writeFileSync(new URL('./crawl.json', import.meta.url), JSON.stringify(out, null, 1));
await browser.close();
console.log(Object.keys(out).length);
