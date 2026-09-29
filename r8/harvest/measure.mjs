const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const slug = process.argv[2] || 'mighty-5-utah-from-las-vegas';
const W = Number(process.argv[3] || 1440);
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: W, height: 900 }, deviceScaleFactor: 1 , ...(W<500?{isMobile:true,hasTouch:true,deviceScaleFactor:2}:{}) });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const p = await ctx.newPage();
await p.goto(`${base}/tours/${slug}/`, { waitUntil: 'networkidle' });
const out = await p.evaluate(() => {
  const sec = document.getElementById('departures');
  const r = (el) => { const b = el.getBoundingClientRect(); return { x: Math.round(b.x), y: Math.round(b.y + scrollY), w: Math.round(b.width), h: Math.round(b.height) }; };
  const rows = [...sec.querySelectorAll('li')].map(li => ({ text: li.innerText.replace(/\n/g,' | '), box: r(li), hidden: !li.offsetParent }));
  const months = [...sec.querySelectorAll('h3')].map(h => ({ t: h.textContent, box: r(h), hidden: !h.offsetParent }));
  const sum = sec.querySelector('summary');
  const rail = [...document.querySelectorAll('aside, [class*=sticky]')].map(e => ({ tag: e.tagName, cls: e.className.slice(0,80), box: r(e), text: e.innerText.slice(0,300) }));
  const toc = [...document.querySelectorAll('h2')].map(h => ({ t: h.textContent, y: r(h).y }));
  return { href: location.href, docH: document.documentElement.scrollHeight, section: r(sec), sectionClosedH: r(sec).h, summary: sum ? { t: sum.innerText, box: r(sum) } : null, months, rows, rail, toc, intro: [...sec.querySelectorAll(':scope p')].slice(0,3).map(p=>p.innerText) };
});
fs.writeFileSync(new URL(`./${slug}-${W}.json`, import.meta.url), JSON.stringify(out, null, 1));
await p.locator('#departures').screenshot({ path: new URL(`./${slug}-${W}-closed.png`, import.meta.url).pathname });
if (await p.locator('#departures summary').count()) {
  await p.locator('#departures summary').click();
  const h = await p.evaluate(() => ({ sec: Math.round(document.getElementById('departures').getBoundingClientRect().height), doc: document.documentElement.scrollHeight }));
  out.openH = h; fs.writeFileSync(new URL(`./${slug}-${W}.json`, import.meta.url), JSON.stringify(out, null, 1));
}
console.log(out.href, 'doc', out.docH, 'section', out.section, 'open', out.openH, 'rows', out.rows.length, 'months', out.months.length, 'summary', JSON.stringify(out.summary));
await browser.close();
