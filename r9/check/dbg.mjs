const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1440, height: 1000 } });
await p.goto('file:///home/james/swat/projects/swat-sept-sheet/site/index.html', { waitUntil: 'load' });
await p.waitForTimeout(1500);
console.log(await p.evaluate(() => { const m = document.querySelector('#d68 .mock'); m.style.height = 'auto'; const s = getComputedStyle(m).transform.match(/[\d.]+/g); const sc = +s[0]; const mt = m.getBoundingClientRect().top;
  return [m.scrollHeight, ...[...m.querySelectorAll('*')].map(e => [e.tagName, String(e.className).slice(0, 30), Math.round((e.getBoundingClientRect().bottom - mt) / sc), getComputedStyle(e).position]).sort((a, b) => b[2] - a[2]).slice(0, 6)]; }));
await b.close();
