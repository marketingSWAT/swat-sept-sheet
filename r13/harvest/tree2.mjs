import fs from 'node:fs';
const pw = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const gate = fs.readFileSync('/tmp/claude-1000/-home-james-swat/ab73d74c-8e04-4727-a07e-b01db273e3f8/scratchpad/gate','utf8').trim();
const base='https://swat-website-storefront.vercel.app';
const slug=process.argv[2], sels=process.argv.slice(3);
const b=await pw.chromium.launch();
const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
await ctx.addCookies([{name:'swat_gate',value:gate,url:base,httpOnly:true,sameSite:'Lax'}]);
const p=await ctx.newPage(); await p.goto(`${base}/tours/${slug}/`,{waitUntil:'load'});
const r=await p.evaluate((sels)=>{
 function tree(el,d=0,max=4){ if(d>max) return ''; const b=el.getBoundingClientRect(); let s='  '.repeat(d)+el.tagName.toLowerCase()+(el.id?'#'+el.id:'')+' .'+(el.className?.baseVal??el.className).toString().slice(0,60)+` [${Math.round(b.top+scrollY)} h${Math.round(b.height)} w${Math.round(b.width)}]`+(el.children.length==0||el.tagName=='P'||el.tagName=='H3'?' "'+el.textContent.trim().replace(/\s+/g,' ').slice(0,90)+'"':'')+'\n';
  if(['picture','svg','button','p','h3'].includes(el.tagName.toLowerCase())) return s;
  for(const c of el.children) s+=tree(c,d+1,max); return s;}
 const top=[...document.querySelectorAll('main section')].filter(s=>!s.parentElement.closest('section')).map(s=>`${s.id||'-'} "${(s.querySelector('h2')?.textContent||'').trim()}" y${Math.round(s.getBoundingClientRect().top+scrollY)} h${Math.round(s.getBoundingClientRect().height)}`).join('\n');
 return 'H='+document.documentElement.scrollHeight+'\n'+top+'\n\n'+sels.map(s=>{const e=document.querySelector(s.split('@')[0]);return e?tree(e,0,+(s.split('@')[1]||4)):'MISSING '+s}).join('\n=====\n');
},sels);
console.log(r); await b.close();
