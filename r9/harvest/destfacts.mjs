const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const paths = JSON.parse(fs.readFileSync('whitespace-1920.json')).map(r => r.href).filter(h => /^\/destinations\/./.test(h));
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1920, height: 1000 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const out = [];
const q = [...paths];
await Promise.all(Array.from({ length: 6 }, async () => { while (q.length) { const p = q.shift(); const page = await ctx.newPage(); await page.goto(base + p, { waitUntil: 'load' });
  await page.addStyleTag({ content: '*{content-visibility:visible!important}' });
  const r = await page.evaluate(() => {
    const secs = [...document.querySelectorAll('main section')];
    const find = t => secs.find(s => (s.querySelector('h2')?.innerText || '').toLowerCase().includes(t));
    const gal = secs.find(s => /in photographs/i.test(s.querySelector('h2')?.innerText || ''));
    const words = document.querySelector('.prose-trip');
    const trips = find('trips that go here');
    return { href: location.pathname, photos: gal ? gal.querySelectorAll('figure').length : 0,
      hikes: find('plan your') ? find('plan your').querySelectorAll('a').length : 0,
      journal: find('from the journal') ? find('from the journal').querySelectorAll('a').length : 0,
      trips: trips ? trips.querySelectorAll('article').length : 0,
      wordsH: words ? Math.round(words.getBoundingClientRect().height) : 0,
      tripsY: trips ? Math.round(trips.getBoundingClientRect().top + scrollY) : 0 };
  }); out.push(r); await page.close(); } }));
fs.writeFileSync('destfacts.json', JSON.stringify(out, null, 1));
const c = (f) => out.filter(f).length;
console.log('n', out.length, 'photos<3', c(r => r.photos < 3), 'photos==0', c(r => r.photos == 0), 'hikes sec', c(r => r.hikes > 0), 'journal', c(r => r.journal > 0), 'journal<3', c(r => r.journal > 0 && r.journal < 3), 'no trips', c(r => !r.trips));
console.log('wordsH median', out.map(r => r.wordsH).sort((a, b) => a - b)[19], 'max', Math.max(...out.map(r => r.wordsH)), 'tripsY median', out.map(r => r.tripsY).sort((a, b) => a - b)[19]);
console.log('gallery last row part-empty (4 col, lead=4 cells):', c(r => r.photos > 1 && ((r.photos - 1 + 4) % 4) != 0));
await browser.close();
