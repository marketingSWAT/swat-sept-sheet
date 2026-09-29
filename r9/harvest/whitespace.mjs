// Dead-right-side audit: for every sitemap page, how much of the page's height
// leaves the right part of the content column blank, at a given viewport width.
//   node whitespace.mjs 1920 [pathFilter]
const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
import fs from 'node:fs';
const gate = fs.readFileSync(new URL('./gate.txt', import.meta.url), 'utf8').trim();
const base = process.env.BASE || 'https://swat-website-storefront.vercel.app';
const W = Number(process.argv[2] || 1920);
const filt = process.argv[3] || '';
const sm = await (await fetch(base + '/sitemap.xml', { headers: { cookie: 'swat_gate=' + gate } })).text();
const paths = [...sm.matchAll(/<loc>https?:\/\/[^/]+([^<]*)<\/loc>/g)].map(m => m[1] || '/').filter(p => p.includes(filt));
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: W, height: 1000 }, deviceScaleFactor: 1 });
await ctx.addCookies([{ name: 'swat_gate', value: gate, url: base }]);
const out = [];
async function one(p) {
  const page = await ctx.newPage();
  try {
    await page.goto(base + p, { waitUntil: 'load', timeout: 60000 });
    await page.addStyleTag({ content: '*{content-visibility:visible!important}' });
    await page.waitForTimeout(400);
    if (process.env.DBG) await page.evaluate(() => { window.__dbg = [] });
    const r = await page.evaluate(() => {
      const hdr = document.querySelector('header');
      const main = document.querySelector('main') || document.body;
      const foot = document.querySelector('footer');
      const logo = hdr.querySelector('a');
      const links = [...hdr.querySelectorAll('a,button')].filter(e => e.offsetParent);
      const cL = Math.round(logo.getBoundingClientRect().left);
      const cR = Math.round(Math.max(...links.map(e => e.getBoundingClientRect().right)));
      const top = main.getBoundingClientRect().top + scrollY;
      const bot = (foot ? foot.getBoundingClientRect().top : main.getBoundingClientRect().bottom) + scrollY;
      const boxes = [];
      const skip = (el) => { for (let e = el; e; e = e.parentElement) { const s = getComputedStyle(e); if (s.position === 'fixed' || s.visibility === 'hidden' || s.display === 'none') return true; if (e.hasAttribute && (e.hasAttribute('data-phone-bar') || e.id === 'satisfi')) return true; } return false; };
      const tw = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
      let n; while ((n = tw.nextNode())) { if (!n.textContent.trim()) continue; const rg = document.createRange(); rg.selectNodeContents(n); for (const b of rg.getClientRects()) if (b.width > 1) boxes.push([b.left, b.right, b.top + scrollY, b.bottom + scrollY, 't']); }
      for (const e of main.querySelectorAll('img,video,iframe,svg,canvas,input,select,textarea,button,picture,[style*="background-image"]')) { const b = e.getBoundingClientRect(); if (b.width > 4 && b.height > 4) boxes.push([b.left, b.right, b.top + scrollY, b.bottom + scrollY, 'm']); }
      for (const e of main.querySelectorAll('*')) { const s = getComputedStyle(e); const bg = s.backgroundColor; const filled = (bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'rgb(255, 255, 255)') || s.backgroundImage !== 'none' || parseFloat(s.borderRightWidth) > 0; if (!filled) continue; const b = e.getBoundingClientRect(); if (b.width > 40 && b.height > 20) boxes.push([b.left, b.right, b.top + scrollY, b.bottom + scrollY, 'f', e.tagName + '.' + String(e.className).slice(0, 60)]); }
      const B = boxes.filter(b => b[1] > b[0]);
      const band = 20, cw = cR - cL; let deadPx = 0, worst = 0, runs = [], cur = null;
      for (let y = top; y < bot; y += band) {
        const inBand = B.filter(b => b[3] > y && b[2] < y + band);
        if (!inBand.length) { if (cur) cur.h += band; continue; }  // blank band: vertical gap, not a right-side gap
        const right = Math.max(...inBand.map(b => Math.min(b[1], window.innerWidth)));
        const gap = cR - right;
        if (gap > 0.35 * cw) { deadPx += band; worst = Math.max(worst, gap); if (!cur) cur = { y: Math.round(y), h: 0, gap: 0 }; cur.h += band; cur.gap = Math.max(cur.gap, Math.round(gap)); }
        else if (cur) { runs.push(cur); cur = null; }
        if (window.__dbg && y > 900 && y < 1400) window.__dbg.push([Math.round(y), Math.round(gap), inBand.filter(b => Math.min(b[1], innerWidth) === right).map(b => b[4] + (b[5]||'')).join(',')]);
      }
      if (cur) runs.push(cur);
      runs = runs.filter(r => r.h >= 100).sort((a, b) => b.h - a.h);
      return { href: location.pathname, cL, cR, cw, pageH: Math.round(bot - top), deadPx, worst: Math.round(worst), runs: runs.slice(0, 4), dbg: window.__dbg };
    });
    out.push(r);
    console.log(p, 'dead', r.deadPx, 'of', r.pageH, 'worstGap', r.worst, JSON.stringify(r.runs.slice(0, 2)));
  } catch (e) { console.log(p, 'ERR', e.message.slice(0, 100)); }
  await page.close();
}
const q = [...paths]; await Promise.all(Array.from({ length: 6 }, async () => { while (q.length) await one(q.shift()); }));
fs.writeFileSync(new URL(`./whitespace-${W}${filt ? '-' + filt.replace(/\W/g, '') : ''}.json`, import.meta.url), JSON.stringify(out, null, 1));
await browser.close();
