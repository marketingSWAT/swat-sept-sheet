const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const [p, W = 1920] = process.argv.slice(2);
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: +W, height: 1000 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const page = await ctx.newPage();
await page.goto(base + p, { waitUntil: 'load' });
await page.addStyleTag({ content: '*{content-visibility:visible!important}' });
await page.waitForTimeout(800);
const out = await page.evaluate(() => {
  const R = e => { const b = e.getBoundingClientRect(); return [Math.round(b.x), Math.round(b.y + scrollY), Math.round(b.width), Math.round(b.height)]; };
  const secs = [...document.querySelectorAll('main [id], main section, main aside')].map(e => ({ id: e.id, tag: e.tagName, cls: String(e.className).slice(0, 90), box: R(e), pos: getComputedStyle(e).position, h: e.querySelector('h2,h3')?.innerText.slice(0, 60) }));
  return { docH: document.documentElement.scrollHeight, secs };
});
console.log(JSON.stringify(out.docH)); for (const s of out.secs) if (s.box[3] > 30) console.log(s.tag, s.id, s.box.join(','), s.pos, s.cls.slice(0, 70), '|', s.h);
await browser.close();
