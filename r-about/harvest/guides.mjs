const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const out = {};
for (const s of ['ann-evans','chris-vander-wilt','dennis-bailey','jason-murray','julie-burton-ray','kirk-douglass','phil-douglass','robin-luse','shawn-horman','shybree-richens']) {
  const p = await ctx.newPage(); await p.goto(`${base}/about/${s}/`, { waitUntil: 'domcontentloaded' });
  out[s] = await p.evaluate(()=>document.querySelector('main').innerText); await p.close();
}
fs.writeFileSync(new URL('./guides.json', import.meta.url), JSON.stringify(out,null,1));
await b.close();
