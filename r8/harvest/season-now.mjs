const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const slug = process.argv[2] || 'mighty-5-utah-from-las-vegas';
const W = Number(process.argv[3] || 1440);
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: W, height: 900 }, ...(W<500?{isMobile:true,hasTouch:true,deviceScaleFactor:2}:{}) });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const p = await ctx.newPage();
await p.goto(`${base}/tours/${slug}/`, { waitUntil: 'networkidle' });
const out = await p.evaluate(() => {
  const r = (el) => { const b = el.getBoundingClientRect(); return { x: Math.round(b.x), y: Math.round(b.y + scrollY), w: Math.round(b.width), h: Math.round(b.height) }; };
  const dep = document.getElementById('departures'), sea = document.getElementById('seasons');
  const tabs = [...dep.querySelectorAll('.dep-years > label')].map(l => ({ t: l.innerText, box: r(l) }));
  const panel = dep.querySelector('.dep-years input:checked + label + .dep-year-panel');
  const cards = panel ? [...panel.querySelectorAll('li, h3, h4')].slice(0,60).map(e => ({ tag: e.tagName, t: e.innerText.replace(/\n/g,' | ').slice(0,80), box: r(e) })) : [];
  const toc = [...document.querySelectorAll('h2')].map(h => ({ t: h.textContent, y: r(h).y }));
  const cs = panel && getComputedStyle(panel.querySelector('ul,ol,div'));
  return { docH: document.documentElement.scrollHeight, dep: r(dep), depText: dep.innerText.slice(0,1500), tabs, panelH: panel && r(panel), cards,
    seasons: sea ? { box: r(sea), text: sea.innerText } : null, toc };
});
fs.writeFileSync(new URL(`./season-now-${slug}-${W}.json`, import.meta.url), JSON.stringify(out, null, 1));
await p.locator('#departures').screenshot({ path: new URL(`./season-now-${slug}-${W}-dep.png`, import.meta.url).pathname });
if (out.seasons) await p.locator('#seasons').screenshot({ path: new URL(`./season-now-${slug}-${W}-sea.png`, import.meta.url).pathname });
console.log(JSON.stringify({docH: out.docH, dep: out.dep, tabs: out.tabs, panelH: out.panelH, seasons: out.seasons && out.seasons.box, toc: out.toc}, null, 0));
await browser.close();
