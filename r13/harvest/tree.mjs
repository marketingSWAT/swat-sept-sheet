import fs from 'node:fs';
const pw = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const gate = fs.readFileSync('/tmp/claude-1000/-home-james-swat/ab73d74c-8e04-4727-a07e-b01db273e3f8/scratchpad/gate','utf8').trim();
const base='https://swat-website-storefront.vercel.app';
const b=await pw.chromium.launch();
const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
await ctx.addCookies([{name:'swat_gate',value:gate,url:base,httpOnly:true,sameSite:'Lax'}]);
const p=await ctx.newPage(); await p.goto(`${base}/tours/albuquerque-balloon-fiesta/`,{waitUntil:'load'});
const r=await p.evaluate(()=>{
 function tree(el,d=0){ if(d>7) return ''; const b=el.getBoundingClientRect(); let s='  '.repeat(d)+el.tagName.toLowerCase()+(el.id?'#'+el.id:'')+' .'+(el.className?.baseVal??el.className).toString().slice(0,70)+` [${Math.round(b.top+scrollY)} h${Math.round(b.height)}]`+(el.children.length==0?' "'+el.textContent.trim().slice(0,60)+'"':'')+'\n';
  if(['picture','svg','button'].includes(el.tagName.toLowerCase())) return s;
  for(const c of el.children) s+=tree(c,d+1); return s;}
 return tree(document.querySelector('#day-1'))+'\n=====\n'+tree(document.querySelector('#details'),0)+'\n=====\n'+[...document.querySelectorAll('#itinerary > div > *')].map(e=>e.tagName+' .'+e.className.slice(0,60)+' h'+Math.round(e.getBoundingClientRect().height)).join('\n');
});
console.log(r); await b.close();
