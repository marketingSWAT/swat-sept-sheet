// Render mockup fragments exactly as the decision sheet hosts them and
// screenshot them at 1920 and at phone width (390).
//   node r8/tools/preview.mjs now calendar            (Claude's, r8/frag/)
//   node r8/tools/preview.mjs codex/E codex/F          (Codex's, r8/codex/mocks/)
// Writes r8/preview/<name>-desk.png / -phone.png and prints the natural height
// at each width, any horizontal overflow on the phone, and broken images.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire('/home/james/swat/projects/pc-set-up/package.json');
const { chromium } = require('playwright');
const R8 = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const BUILD = path.resolve(R8, '..', 'build');
const cssDir = path.join(R8, 'codex', 'css');
const css = () => [fs.readFileSync(path.join(BUILD, 'sheet.css'), 'utf8'), fs.readFileSync(path.join(BUILD, 'r9.css'), 'utf8'), fs.readFileSync(path.join(BUILD, 'about.css'), 'utf8'),
  ...fs.readdirSync(cssDir).filter(f => f.endsWith('.css')).sort().map(f => fs.readFileSync(path.join(cssDir, f), 'utf8'))].join('\n');
const names = process.argv.slice(2);
if (!names.length) { console.error('usage: preview.mjs <name> ...'); process.exit(1); }
const browser = await chromium.launch();
for (const name of names) {
  const src = name.startsWith('codex/') ? path.join(R8, 'codex', 'mocks', name.slice(6) + '.html') : path.join(R8, 'frag', name + '.html');
  const frag = fs.readFileSync(src, 'utf8');
  const tag = name.replace('/', '-');
  for (const [mode, w] of [['desk', 1920], ['phone', 390]]) {
    const html = `<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>${css()}\nbody{margin:0;background:#0b1117}
.mockwrap{position:relative;width:${w}px;overflow:visible}
.mockwrap .mock{position:relative!important;transform:none!important;width:${w}px!important;height:auto!important}</style></head>
<body><div class="mockwrap ${mode === 'phone' ? 'phone' : ''}"><div class="mock aw1920">${frag}</div></div></body></html>`;
    const f = path.join(R8, 'preview', `${tag}-${mode}.html`);
    fs.writeFileSync(f, html);
    const page = await browser.newPage({ viewport: { width: w, height: 1080 }, deviceScaleFactor: 1 });
    await page.goto('file://' + f, { waitUntil: 'networkidle' }).catch(() => {});
    await page.waitForTimeout(300);
    const m = await page.evaluate((w) => {
      const mk = document.querySelector('.mock');
      const over = [];
      mk.querySelectorAll('*').forEach(e => {
        const r = e.getBoundingClientRect();
        if (r.width && r.right > w + 1 && getComputedStyle(e).display !== 'none' && over.length < 8) over.push((e.className?.baseVal ?? e.className) + ' right=' + Math.round(r.right));
      });
      const broken = [...mk.querySelectorAll('img')].filter(i => !i.naturalWidth).map(i => i.getAttribute('src'));
      return { h: Math.round(mk.scrollHeight), sw: mk.scrollWidth, over, broken };
    }, w);
    await page.screenshot({ path: path.join(R8, 'preview', `${tag}-${mode}.png`), fullPage: true });
    await page.close();
    console.log(`${name} ${mode}: height ${m.h}px, scrollWidth ${m.sw}` + (m.over.length ? `, OVERFLOW: ${m.over.join('; ')}` : '') + (m.broken.length ? `, BROKEN IMG: ${m.broken.join(', ')}` : ''));
  }
}
await browser.close();
