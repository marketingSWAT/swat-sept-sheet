const { chromium } = (await import('/home/james/swat/projects/pc-set-up/node_modules/playwright/index.js')).default;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
await page.goto('file:///home/james/swat/projects/swat-sept-sheet/site/index.html', { waitUntil: 'load' });
await page.waitForTimeout(1500);
const btns = await page.$$('#d75 .mockwrap, #d76 .mockwrap, #d77 .mockwrap, #d78 .mockwrap, #d79 .mockwrap');
const toggles = await page.$$eval('#d75 button, #d76 button, #d77 button, #d78 button, #d79 button', bs => bs.map(b => b.innerText.trim()));
console.log([...new Set(toggles)]);
for (const id of ['d75','d76','d77','d78','d79']) {
  await page.evaluate(id => { document.querySelectorAll(`#${id} button`).forEach(b => { if (/phone/i.test(b.innerText)) b.click(); }); }, id);
}
await page.waitForTimeout(2500);
console.log(JSON.stringify(await page.evaluate(() => ['d75','d76','d77','d78','d79'].map(id => [...document.querySelectorAll(`#${id} .mock`)].map(m => [m.scrollWidth, Math.round(m.getBoundingClientRect().height)])))));
for (const id of ['d76','d79']) { const el = await page.$(`#${id} .opt.rec`); await el.screenshot({ path: `/home/james/swat/projects/swat-sept-sheet/r11/check/${id}-phone.png` }); }
await browser.close();
