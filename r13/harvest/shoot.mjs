// node shoot.mjs <slug> : prototype each variant on the live page, measure, and shoot a 3-screen window.
import fs from 'node:fs';
const pw = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const gate = fs.readFileSync('/tmp/claude-1000/-home-james-swat/ab73d74c-8e04-4727-a07e-b01db273e3f8/scratchpad/gate','utf8').trim();
const base='https://swat-website-storefront.vercel.app';
const slug=process.argv[2]; const shoot=process.argv[3]!=='noshot';
const proto=fs.readFileSync(new URL('./proto.js', import.meta.url),'utf8');
const b=await pw.chromium.launch();
const out={slug};
const VS=['now','fold','short','lists','photos'];
for (const v of VS) {
  const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
  await ctx.addCookies([{name:'swat_gate',value:gate,url:base,httpOnly:true,sameSite:'Lax'}]);
  const p=await ctx.newPage(); await p.goto(`${base}/tours/${slug}/`,{waitUntil:'load'});
  await p.evaluate(async()=>{document.documentElement.style.scrollBehavior='auto';for(let y=0;y<document.documentElement.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,70))}scrollTo(0,0);await new Promise(r=>setTimeout(r,900))});
  await p.addScriptTag({content:proto});
  await p.evaluate(v=>window.__proto(v), v);
  await p.waitForTimeout(700);
  if (shoot) await p.evaluate(async()=>{await Promise.all([...document.images].filter(i=>!i.complete&&i.getClientRects().length).map(i=>new Promise(r=>{i.onload=i.onerror=r;setTimeout(r,5000)})))});
  const m=await p.evaluate(()=>{
    const Y=e=>e?Math.round(e.getBoundingClientRect().top+scrollY):null, Hh=e=>e?Math.round(e.getBoundingClientRect().height):0;
    const secs=[...document.querySelectorAll('main section')].filter(s=>!s.parentElement.closest('section')).map(s=>({id:s.id,t:(s.querySelector('h2')?.textContent||'').trim().slice(0,40),y:Y(s),h:Hh(s)}));
    const it=document.querySelector('#itinerary');
    const box=sel=>{const e=document.querySelector(sel); if(!e||!e.getClientRects().length) return null; const r=e.getBoundingClientRect(); return {x:Math.round(r.left),y:Math.round(r.top+scrollY),w:Math.round(r.width),h:Math.round(r.height)}};
    return {href:location.href,H:document.documentElement.scrollHeight,vh:innerHeight,footer:Hh(document.querySelector('footer')),secs,itY:Y(it),
      days:it?it.querySelectorAll('li[id^="day-"]').length:0,
      boxes:{glance:box('#itinerary nav[aria-label="Trip at a glance"]'),day1:box('#day-1'),day2:box('#day-2'),row1:box('#day-1 .pr-row'),rowLast:box('#itinerary li[id^="day-"]:last-child'),
        fig1:box('#day-1 figure'),clamp1:box('#day-1 .pr-clamp'),more1:box('#day-1 .pr-more'),top1:box('#day-1 .pr-top'),
        rfy:box('#right-for-you'),rowsAll:box('#day-1'),inPrice:box('#details > div:first-of-type > div:first-child'),notPrice:box('#details .pr-closed'),gal1:box('#gallery .grid'),mp1:box('#more-photos .grid'),proLine:box('#protection .pr-line1'),dep:box('#departures'),pricing:box('#pricing'),details:box('#details'),detMore:box('#details .pr-more'),lines:box('#details .pr-lines'),gallery:box('#gallery'),photos:box('#more-photos'),protection:box('#protection')}};
  });
  out[v]=m;
  if (shoot) {
    // Shoot and measure in ONE state: a 3-screen-tall viewport scrolled to the
    // window. A fullPage clip re-lays the page and shifts it ~20px against any
    // box measured beforehand, which put every ring below its element.
    const wins=[];
    if (['now','fold','short'].includes(v)) wins.push(['days', '#itinerary']);
    if (['now','lists','photos'].includes(v)) wins.push(['lower', '#details']);
    out[v].win={};
    await p.setViewportSize({width:390,height:844*3});
    await p.waitForTimeout(400);
    for (const [w,sel] of wins) {
      await p.evaluate(sel=>{const hh=document.querySelector('header').getBoundingClientRect().height;
        const y=document.querySelector(sel).getBoundingClientRect().top+scrollY; scrollTo(0,y-hh-14);},sel);
      await p.waitForTimeout(600);
      await p.evaluate(async()=>{await Promise.all([...document.images].filter(i=>!i.complete&&i.getClientRects().length).map(i=>new Promise(r=>{i.onload=i.onerror=r;setTimeout(r,5000)})))});
      out[v].win[w]=await p.evaluate(()=>{const box=sel=>{const e=document.querySelector(sel); if(!e||!e.getClientRects().length) return null; const r=e.getBoundingClientRect(); return {x:Math.round(r.left),y:Math.round(r.top),w:Math.round(r.width),h:Math.round(r.height)}};
        const S={glance:'#itinerary nav[aria-label="Trip at a glance"]',fig1:'#day-1 figure',day2:'#day-2',row1:'#day-1 .pr-row',rowLast:'#itinerary li[id^="day-"]:last-child',rfy:'#right-for-you',
          top1:'#day-1 .pr-top',clamp1:'#day-1 .pr-clamp',more1:'#day-1 .pr-more',inPrice:'#details > div:first-of-type > div:first-child',gal1:'#gallery .grid',
          detMore:'#details .pr-more',notPrice:'#details .pr-closed',lines:'#details .pr-lines',mp1:'#more-photos .grid'};
        const o={}; for (const k in S) o[k]=box(S[k]); return o;});
      await p.screenshot({path:`r13/shots/${slug}-${w}-${v}.jpg`,type:'jpeg',quality:72});
    }
  }
  await ctx.close();
}
fs.mkdirSync('r13/data',{recursive:true});
fs.writeFileSync(`r13/data/${shoot?'':'sweep/'}${slug}.json`,JSON.stringify(out,null,1));
console.log(slug, VS.map(v=>v+':'+(out[v].H/844).toFixed(1)).join(' '));
await b.close();
