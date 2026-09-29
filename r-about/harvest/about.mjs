const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const b = await chromium.launch();
for (const w of [1920, 1440, 390]) {
  const ctx = await b.newContext({ viewport: { width: w, height: w===390?844:1080 } });
  await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
  const p = await ctx.newPage(); await p.goto(`${base}/about/`, { waitUntil: 'networkidle' });
  await p.addStyleTag({content:'html{scroll-behavior:auto!important}'});
  for (let y=0;y<20000;y+=600){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(80);} await p.evaluate(()=>scrollTo(0,0));
  await p.waitForTimeout(500);
  const t = await p.evaluate(() => {
    const main = document.querySelector('main');
    const blocks = [...main.querySelectorAll('h1,h2,h3,h4,p,li,figcaption,img,iframe,video,a.button,a[class*="rounded"],blockquote,section')].map(e => {
      const r = e.getBoundingClientRect();
      return { tag: e.tagName, cls: (e.className?.baseVal ?? e.className ?? '').toString().slice(0,120), y: Math.round(r.top+scrollY), x: Math.round(r.left), w: Math.round(r.width), h: Math.round(r.height),
        text: e.tagName==='IMG' ? (e.currentSrc||e.src)+' | alt='+e.alt+' | nat='+e.naturalWidth+'x'+e.naturalHeight : e.tagName==='SECTION'? '' : (e.innerText||'').slice(0,400), fs: getComputedStyle(e).fontSize };
    });
    return { url: location.href, title: document.title, H: document.documentElement.scrollHeight, mainText: main.innerText, blocks,
      nav: [...document.querySelectorAll('header nav a, header a')].map(a=>a.innerText.trim()).filter(Boolean), crumbs: document.querySelector('nav[aria-label*="read" i]')?.innerText };
  });
  fs.writeFileSync(new URL(`./about-${w}.json`, import.meta.url), JSON.stringify(t, null, 1));
  await p.evaluate(()=>document.querySelectorAll('[class*="satisfi" i],#satisfi, iframe[src*="satisfi"]').forEach(e=>e.style.display='none'));
  await p.screenshot({ path: new URL(`./about-${w}.png`, import.meta.url).pathname, fullPage: true });
  console.log(w, 'H=', t.H, 'blocks', t.blocks.length);
  await ctx.close();
}
await b.close();
