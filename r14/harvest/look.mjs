import fs from 'node:fs';
const pw = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const gate = fs.readFileSync('/tmp/claude-1000/-home-james-swat/2a61cde8-ba55-46f4-b98a-f0655961e103/scratchpad/gate','utf8').trim();
const base='https://swat-website-storefront.vercel.app';
const b=await pw.chromium.launch();
for (const [w,h] of [[1440,900],[390,844]]) {
  const ctx=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:1,isMobile:w<500,hasTouch:w<500});
  await ctx.addCookies([{name:'swat_gate',value:gate,url:base,httpOnly:true,sameSite:'Lax'}]);
  const p=await ctx.newPage(); await p.goto(`${base}/find/`,{waitUntil:'load'});
  const m=await p.evaluate(()=>{
    const R=e=>{if(!e)return null;const r=e.getBoundingClientRect();return {x:Math.round(r.left),y:Math.round(r.top+scrollY),w:Math.round(r.width),h:Math.round(r.height)}};
    const aside=document.querySelector('aside');
    const chips=[...document.querySelectorAll('aside a.chip')];
    const groups=[...document.querySelectorAll('#trip-filters > div')].map(g=>({label:g.querySelector('p')?.textContent,n:g.querySelectorAll('a').length,box:R(g),values:[...g.querySelectorAll('a')].map(a=>a.textContent.trim())}));
    const cs=chips[0]?getComputedStyle(chips[0]):null;
    return {H:document.documentElement.scrollHeight,aside:R(aside),filters:R(document.querySelector('#trip-filters')),form:R(document.querySelector('form[action="/find/"]')),h1:R(document.querySelector('h1')),
      count:document.querySelector('main p b')?.textContent, grid:R(document.querySelector('main ul.grid, main .grid')),
      chips:chips.length, chip:cs&&{r:cs.borderRadius,h:chips[0].getBoundingClientRect().height,font:cs.font,border:cs.border,bg:cs.backgroundColor,color:cs.color,pad:cs.padding},
      groups, header:R(document.querySelector('header')), footer:R(document.querySelector('footer')),
      cards:[...document.querySelectorAll('main a[href^="/tours/"]')].slice(0,12).map(a=>a.getAttribute('href')),
      gridCols: (()=>{const g=[...document.querySelectorAll('main *')].find(e=>getComputedStyle(e).display==='grid'&&e.querySelectorAll('a[href^="/tours/"]').length>3);return g?getComputedStyle(g).gridTemplateColumns:null})()};
  });
  console.log(w, JSON.stringify(m,null,0).slice(0,4000));
  fs.writeFileSync(`r14/data/look-${w}.json`,JSON.stringify(m,null,1));
  await p.screenshot({path:`r14/shots/find-${w}-top.jpg`,type:'jpeg',quality:70});
  await ctx.close();
}
await b.close();
