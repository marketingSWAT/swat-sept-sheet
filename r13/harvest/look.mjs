const pw = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const [w,sel,out]=[+process.argv[2],process.argv[3],process.argv[4]];
const b=await pw.chromium.launch(); const p=await b.newPage({viewport:{width:w,height:900}});
await p.goto('http://127.0.0.1:8797/',{waitUntil:'load'}); await p.waitForTimeout(1500);
const e=await p.$(sel); await e.scrollIntoViewIfNeeded(); await p.waitForTimeout(800);
console.log(await p.evaluate(s=>{const d=document.querySelector(s);return JSON.stringify({h:d.getBoundingClientRect().height,rings:[...d.querySelectorAll('.ring')].map(r=>r.hasAttribute('data-on')?1:0).join(''),overflowX:document.documentElement.scrollWidth>innerWidth})},sel));
await e.screenshot({path:out}); await b.close();
