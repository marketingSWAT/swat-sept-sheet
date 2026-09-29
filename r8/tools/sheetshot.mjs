// Screenshot one decision on the built sheet (site/index.html or a URL).
//   node r8/tools/sheetshot.mjs d67 [url] [--phone]
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire('/home/james/swat/projects/pc-set-up/package.json');
const { chromium } = require('playwright');
const R8 = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const id = process.argv[2] || 'd67';
const url = process.argv[3] && !process.argv[3].startsWith('--') ? process.argv[3] : 'file://' + path.resolve(R8, '..', 'site', 'index.html');
const phone = process.argv.includes('--phone');
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
await p.goto(url, { waitUntil: 'networkidle' });
await p.waitForTimeout(800);
if (phone) {
  await p.evaluate((id) => document.querySelectorAll(`#${id} .mock-bar .seg button[data-w=phone]`).forEach(b => b.click()), id);
  await p.waitForTimeout(500);
}
const info = await p.evaluate((id) => {
  const d = document.getElementById(id);
  const ws = [...d.querySelectorAll('.mockwrap')];
  const rings = [...d.querySelectorAll('.ring')].map(r => ({ n: r.dataset.n, sel: r.dataset.sel, on: r.hasAttribute('data-on') }));
  const imgs = [...d.querySelectorAll('img')].filter(i => !i.naturalWidth).length;
  return { panels: ws.length, mh: ws.map(w => w.style.getPropertyValue('--mh') + '/' + Math.round(w.getBoundingClientRect().height)), rings, brokenImgs: imgs, letters: [...d.querySelectorAll('.opt')].map(o => o.dataset.letter + ':' + o.dataset.name) };
}, id);
console.log(JSON.stringify(info, null, 1));
const el = await p.$('#' + id);
await el.screenshot({ path: path.join(R8, 'preview', `sheet-${id}${phone ? '-phone' : ''}.png`) });
await b.close();
