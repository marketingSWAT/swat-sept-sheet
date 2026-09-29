const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const p = await ctx.newPage(); await p.goto(`${base}/tours/mighty-5-utah-from-las-vegas/`, { waitUntil: 'networkidle' });
await p.click('.dep-years > label:nth-of-type(2)');
const t = await p.evaluate(() => ({ rail: [...document.querySelectorAll('aside')].map(a=>a.innerText.slice(0,500)),
  y27: document.querySelector('.dep-years input:checked + label + .dep-year-panel').innerText.slice(0,900),
  h27: Math.round(document.getElementById('departures').getBoundingClientRect().height),
  cardW: [...document.querySelectorAll('.dep-years input:checked + label + .dep-year-panel li')].slice(0,1).map(l=>l.parentElement.parentElement.getBoundingClientRect().width) }));
console.log(JSON.stringify(t, null, 1));
await p.locator('#departures').screenshot({ path: 'season-now-2027-1440.png' });
await b.close();
