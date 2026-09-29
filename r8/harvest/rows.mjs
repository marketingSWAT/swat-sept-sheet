const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const slug = process.argv[2];
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const p = await ctx.newPage();
await p.goto(`${base}/tours/${slug}/`, { waitUntil: 'domcontentloaded' });
const out = await p.evaluate(() => {
  const sec = document.getElementById('departures');
  const rows = [...sec.querySelectorAll('li')].map(li => {
    const a = li.querySelector('a'); const date = li.querySelector('p')?.textContent;
    return { date, extra: [...li.querySelectorAll('p')].slice(1).map(x=>x.textContent), sold: /Sold out/i.test(li.textContent), label: a?.textContent.trim(), href: a?.getAttribute('href'), popup: a?.hasAttribute('data-softrip-popup') };
  });
  const pr = document.getElementById('pricing');
  return { title: document.querySelector('h1')?.textContent, rows, pricing: pr?.innerText, hero: document.querySelector('main img')?.currentSrc };
});
fs.writeFileSync(new URL(`./${slug}-rows.json`, import.meta.url), JSON.stringify(out, null, 1));
console.log(out.title, out.rows.length);
for (const r of out.rows) console.log(r.date, r.sold?'SOLD':'', r.label, (r.href||'').slice(0,70), r.popup?'POPUP':'', r.extra.join(' / '));
console.log(out.pricing);
await browser.close();
