// Dump a page's main sections: box, headings, paragraphs, images, cards — at a width.
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
await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } scrollTo(0, 0); });
await page.waitForTimeout(500);
const out = await page.evaluate(() => {
  const R = e => { const b = e.getBoundingClientRect(); return [Math.round(b.x), Math.round(b.y + scrollY), Math.round(b.width), Math.round(b.height)]; };
  const walk = (el, depth) => {
    const kids = [...el.children].filter(k => k.getBoundingClientRect().height > 0);
    return { tag: el.tagName, cls: String(el.className).slice(0, 140), box: R(el),
      text: kids.length ? undefined : el.innerText?.slice(0, 400),
      img: el.tagName === 'IMG' ? el.currentSrc : undefined,
      kids: depth < 7 ? kids.map(k => walk(k, depth + 1)) : undefined };
  };
  return { href: location.href, main: walk(document.querySelector('main'), 0) };
});
fs.writeFileSync(new URL(`./dump${p.replace(/\//g, '_')}${W}.json`, import.meta.url), JSON.stringify(out));
await browser.close();
