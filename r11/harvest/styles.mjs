const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const styles = ['backpacking','guided-small-group','day-tour','self-drive','private-and-custom','large-group','rail-and-cruise','winter','special-event'];
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const out = {};
await Promise.all(styles.map(async s => {
  const page = await ctx.newPage();
  await page.goto(`${base}/trips/${s}/`, { waitUntil: 'load' });
  await page.addStyleTag({ content: '*{content-visibility:visible!important}' });
  await page.waitForTimeout(1200);
  out[s] = await page.evaluate(() => ({
    h1: document.querySelector('h1')?.innerText, lede: document.querySelector('h1')?.parentElement?.querySelector('p')?.innerText,
    cards: [...document.querySelectorAll('main article')].map(a => a.innerText.split('\n').filter(Boolean)),
    img: document.querySelector('main img')?.currentSrc,
  }));
  await page.close();
}));
fs.writeFileSync(new URL('./styles.json', import.meta.url), JSON.stringify(out, null, 1));
await browser.close();
