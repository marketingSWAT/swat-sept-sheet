// Harvest one deployed storefront page at a width: first-screen + full PNG, text blocks with boxes.
const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const [p, W = 1440, H = 900] = process.argv.slice(2);
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: +W, height: +H } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const page = await ctx.newPage();
await page.goto(base + p, { waitUntil: 'load' });
await page.addStyleTag({ content: '*{content-visibility:visible!important;scroll-behavior:auto!important}' });
await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } scrollTo(0, 0); });
await page.waitForTimeout(1200);
const tag = `${p.replace(/\//g, '_')}${W}`;
await page.screenshot({ path: new URL(`./first${tag}.png`, import.meta.url).pathname });
await page.screenshot({ path: new URL(`./full${tag}.png`, import.meta.url).pathname, fullPage: true });
const out = await page.evaluate(() => {
  const R = e => { const b = e.getBoundingClientRect(); return [Math.round(b.x), Math.round(b.y + scrollY), Math.round(b.width), Math.round(b.height)]; };
  const main = document.querySelector('main') || document.body;
  const secs = [...main.querySelectorAll('section, [id]')].filter(e => e.getBoundingClientRect().height > 60).map(e => ({ tag: e.tagName, id: e.id, cls: String(e.className).slice(0, 80), box: R(e), head: (e.querySelector('h1,h2,h3')?.innerText || '').slice(0, 120) }));
  const blocks = [...main.querySelectorAll('h1,h2,h3,h4,p,li,dt,dd,a.btn,button,summary,figcaption,blockquote')].filter(e => e.innerText.trim()).map(e => ({ tag: e.tagName, box: R(e), text: e.innerText.trim().slice(0, 600) }));
  const imgs = [...main.querySelectorAll('img')].map(i => ({ box: R(i), src: i.currentSrc || i.src, alt: i.alt }));
  return { href: location.href, docH: document.documentElement.scrollHeight, secs, blocks, imgs };
});
fs.writeFileSync(new URL(`./dump${tag}.json`, import.meta.url), JSON.stringify(out, null, 1));
await browser.close();
console.log(tag, out.docH);
