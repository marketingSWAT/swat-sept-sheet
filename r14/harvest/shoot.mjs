// node shoot.mjs : prototype every option of 82 + 83 on the live /find/ page, measure, and shoot.
import fs from 'node:fs';
const pw = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const gate = fs.readFileSync('/tmp/claude-1000/-home-james-swat/2a61cde8-ba55-46f4-b98a-f0655961e103/scratchpad/gate','utf8').trim();
const base='https://swat-website-storefront.vercel.app';
const proto=fs.readFileSync(new URL('./proto.js', import.meta.url),'utf8');
const counts=JSON.parse(fs.readFileSync('r14/data/counts-utah.json','utf8'));
const SD=JSON.parse(fs.readFileSync('r14/data/searchdata.json','utf8'));
const only=process.argv[2];
const b=await pw.chromium.launch();
const out=fs.existsSync('r14/data/shots.json')?JSON.parse(fs.readFileSync('r14/data/shots.json','utf8')):{};
const JOBS=[];
for (const v of ['a','b','c','d']) { JOBS.push({v,dev:'desk',w:1440,h:1640,url:'/find/?destination=Utah',data:{counts,total:28}}); JOBS.push({v,dev:'phone',w:390,h:1688,url:'/find/?destination=Utah',data:{counts,total:28}}); }
const sq={sa:SD.zb,sb:SD.zb,sc:SD.ta,sd:SD.y};
for (const v of ['sa','sb','sc','sd']) { const d={...sq[v], ta:SD.ta}; JOBS.push({v,dev:'desk',w:1440,h:1100,url:'/find/',data:d}); JOBS.push({v,dev:'phone',w:390,h:1200,url:'/find/',data:d}); }
for (const j of JOBS) {
  const key=`${j.v}-${j.dev}`; if (only && !key.startsWith(only)) continue;
  const phone=j.dev==='phone';
  const ctx=await b.newContext({viewport:{width:j.w,height:phone?844:900},deviceScaleFactor:phone?2:1.25,isMobile:phone,hasTouch:phone});
  await ctx.addCookies([{name:'swat_gate',value:gate,url:base,httpOnly:true,sameSite:'Lax'}]);
  const p=await ctx.newPage(); await p.goto(base+j.url,{waitUntil:'load'});
  await p.evaluate(()=>{document.documentElement.style.scrollBehavior='auto'; const c=document.querySelector('[class*="satisfi"], #satisfi_btn'); if(c) c.remove();});
  await p.waitForTimeout(1500);
  await p.addScriptTag({content:proto});
  const r=await p.evaluate(([v,d])=>window.__proto(v,d),[j.v,j.data]);
  await p.setViewportSize({width:j.w,height:j.h});
  await p.waitForTimeout(700);
  await p.evaluate(async()=>{for(const i of document.images){i.loading='eager'};await Promise.all([...document.images].filter(i=>!i.complete&&i.getBoundingClientRect().top<3000).map(i=>new Promise(r=>{i.onload=i.onerror=r;setTimeout(r,6000)})))});
  await p.waitForTimeout(300);
  await p.evaluate(()=>document.querySelectorAll('.satisfi_chat-button,#satisfi_chat-panel,[class*=satisfi]').forEach(e=>e.remove()));
  const m=await p.evaluate(()=>{
    const box=e=>{if(!e||!e.getClientRects().length)return null;const r=e.getBoundingClientRect();return {x:Math.round(r.left),y:Math.round(r.top),w:Math.round(r.width),h:Math.round(r.height)}};
    const q=s=>box(document.querySelector(s));
    const rail=document.querySelector('#trip-filters'); const bar=document.querySelector('.p14-bar');
    const bubbles=[...document.querySelectorAll('aside a.chip')].filter(a=>a.getClientRects().length).length;
    return {rail:box(bar||(rail&&rail.getClientRects().length?rail:null)), bubbles,
      rows:[...document.querySelectorAll('.p14-row,.p14-two li,.p14-rows li,.p14-seg span,.p14-lv span,aside a.chip')].filter(e=>e.getClientRects().length).length,
      firstCard:q('main a[href^="/tours/"]'), count:q('main .grid')?.y, form:q('#find-q'),
      S:{g1:q('#trip-filters > div'), ggroup:q('.p14-g'), utah:q('.p14-row.on, .p14-two li.on, .p14-dd.set, aside a[aria-current]'), more:q('.p14-more'),
        lv:q('.p14-lv'), seg:q('.p14-seg.s5'), menu:q('.p14-menu'), tags:q('.p14-tags'), bar:q('.p14-bar'), top:q('.p14-top'),
        closed:q('.p14-g:last-child'), dest:[...document.querySelectorAll('#trip-filters > div')].map(box).filter(Boolean)[3]||null,
        when:[...document.querySelectorAll('#trip-filters > div')].map(box).filter(Boolean)[4]||null,
        grid:q('main .grid'), input:q('#find-q'), ta:q('.p14-ta'), tahp:q('.p14-tah'), taf:q('.p14-taf'), tri:q('.p14-try'), und:q('.p14-und'),
        empty:q('main p.max-w-xl'), card1:q('main .grid > *'), count:q('main .grid')?{...q('main .grid'),y:q('main .grid').y-34,h:24}:null}};
  });
  out[key]={...m, r, W:j.w, H:j.h};
  await p.screenshot({path:`r14/shots/${key}.jpg`,type:'jpeg',quality:74});
  console.log(key, r, JSON.stringify({rail:m.rail,bubbles:m.bubbles,rows:m.rows}));
  await ctx.close();
}
fs.writeFileSync('r14/data/shots.json',JSON.stringify(out,null,1));
await b.close();
