const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = 'https://swat-website-storefront.vercel.app';
const b = await chromium.launch();
const w = +process.argv[2] || 1920;
const ctx = await b.newContext({ viewport: { width: w, height: w===390?844:1080 } });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const p = await ctx.newPage(); await p.goto(`${base}/about/`, { waitUntil: 'networkidle' });
await p.addStyleTag({content:'html{scroll-behavior:auto!important} *{content-visibility:visible!important} [class*="satisfi" i],#satisfi{display:none!important}'});
await p.evaluate(()=>document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager'));
const H = await p.evaluate(()=>document.documentElement.scrollHeight);
for (let y=0;y<H;y+=500){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(120);}
await p.waitForTimeout(1500);
const names = await p.evaluate(()=>[...document.querySelectorAll('main li')].filter(l=>l.querySelector('img')).map(l=>l.innerText.trim()+' || '+l.querySelector('img').alt));
console.log(names.join('\n'));
const vids = await p.evaluate(()=>[...document.querySelectorAll('main iframe, main video, main a[href*="youtu"]')].map(e=>e.outerHTML.slice(0,200)));
console.log('videos', vids);
const links = await p.evaluate(()=>[...document.querySelectorAll('main a')].map(a=>a.innerText.trim().slice(0,40)+' -> '+a.getAttribute('href')));
console.log(links.join('\n'));
await p.evaluate(()=>scrollTo(0,0)); await p.waitForTimeout(300);
await p.screenshot({ path: new URL(`./about-${w}-full.png`, import.meta.url).pathname, fullPage: true });
for (const [i,y] of [[1,0],[2,1080],[3,2160],[4,3240],[5,4320],[6,5400],[7,6480]]) { if (w!==1920) break; await p.evaluate(y=>scrollTo(0,y),y); await p.waitForTimeout(400); await p.screenshot({ path: new URL(`./about-${w}-screen${i}.png`, import.meta.url).pathname }); }
await b.close();
