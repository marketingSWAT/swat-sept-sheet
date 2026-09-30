import fs from 'node:fs';
const pw = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const gate = fs.readFileSync('/tmp/claude-1000/-home-james-swat/ab73d74c-8e04-4727-a07e-b01db273e3f8/scratchpad/gate','utf8').trim();
const base='https://swat-website-storefront.vercel.app';
const slug=process.argv[2]||'albuquerque-balloon-fiesta';
const b=await pw.chromium.launch();
const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
await ctx.addCookies([{name:'swat_gate',value:gate,url:base,httpOnly:true,sameSite:'Lax'}]);
const p=await ctx.newPage(); await p.goto(`${base}/tours/${slug}/`,{waitUntil:'load'});
const r=await p.evaluate(()=>{
  const it=document.querySelector('#itinerary');
  const day=it.querySelector('li[id^="day-"]');
  const secs=[...document.querySelectorAll('main section, main > div > section')].filter(s=>!s.parentElement.closest('section')).map(s=>{const b=s.getBoundingClientRect();return {id:s.id,cls:s.className.slice(0,80),h2:(s.querySelector('h2')?.textContent||'').trim().slice(0,50),top:Math.round(b.top+scrollY),h:Math.round(b.height)}});
  return {href:location.href,H:document.documentElement.scrollHeight,secs,itHTML:it.outerHTML.slice(0,6000),day:day?.outerHTML.slice(0,5000)};
});
console.log(JSON.stringify({href:r.href,H:r.H,secs:r.secs},null,0));
fs.writeFileSync('r13/harvest/it.html',r.itHTML); fs.writeFileSync('r13/harvest/day.html',r.day||'');
await b.close();
