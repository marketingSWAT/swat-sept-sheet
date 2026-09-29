const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const b = await chromium.launch();
for (const w of [1920, 390]) {
  const ctx = await b.newContext({ viewport: { width: w, height: w===390?844:1080 }, deviceScaleFactor: 1 });
  await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
  const p = await ctx.newPage(); await p.goto(`${base}/about/`, { waitUntil: 'networkidle' });
  await p.addStyleTag({content:'html{scroll-behavior:auto!important} *{content-visibility:visible!important} [class*="satisfi" i],#satisfi,[id*="satisfi" i]{display:none!important} *,*::before{animation-play-state:paused!important}'});
  await p.evaluate(()=>document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager'));
  const H = await p.evaluate(()=>document.documentElement.scrollHeight);
  for (let y=0;y<H;y+=400){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(100);}
  await p.evaluate(()=>scrollTo(0,0)); await p.waitForTimeout(1500);
  const foot = await p.evaluate(()=>Math.round(document.querySelector('footer').getBoundingClientRect().top+scrollY));
  // hide fixed floaters that would repeat down a full-page shot
  await p.evaluate(()=>document.querySelectorAll('body *').forEach(e=>{const s=getComputedStyle(e); if(s.position==='fixed' && !e.closest('header')) e.style.display='none';}));
  await p.screenshot({ path: new URL(`./now-${w}.png`, import.meta.url).pathname, fullPage: true, clip: {x:0,y:0,width:w,height:foot} });
  const imgs = await p.evaluate(()=>[...document.images].filter(i=>i.getBoundingClientRect().width>40 && !i.naturalWidth).length);
  console.log(w, 'page', H, 'footer at', foot, 'unloaded imgs', imgs);
  await ctx.close();
}
await b.close();
