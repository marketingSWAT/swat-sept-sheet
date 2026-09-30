// Applied to the LIVE /find/ page to prototype each option of decisions 82 and 83.
// window.__proto(variant, data). Variants: a b c d (filters), sa sb sc sd (search).
function __run(variant, D, css) {
  const T = {rust:'#e4622a', rust7:'#c24c18', rust1:'#fdece4', ink9:'#12212e', ink7:'#2c4356', ink5:'#42596c', ink3:'#7d93a3',
    s1:'#eef4f8', s2:'#dce8f0', s3:'#d6e1e9', navy8:'#0b2136', navy7:'#143352', navy3:'#7fa8c8', navy1:'#b9d0e2',
    pine:'#2b8566', amber:'#b8760d', alert:'#a32020'};
  const FILL = [T.pine, T.amber, T.rust, T.alert];
  const phone = innerWidth < 700;
  const filters = document.querySelector('#trip-filters');
  const aside = filters.closest('aside');
  css.push('#satisfi_btn,[id^=satisfi],[class*=satisfi],[data-chat-launcher],.satisfi_chat-button,.FloatingSearch{display:none!important}');
  const outer = aside.parentElement;
  const results = outer.children[1];
  const countP = results.querySelector('p');
  const tick = '<svg viewBox="0 0 16 16" width="12" height="12" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 8.5l3 3 6-7"/></svg>';
  const chev = (up) => `<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="${T.ink3}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transform:rotate(${up ? 180 : 0}deg)"><path d="m6 9 6 6 6-6"/></svg>`;
  const x = `<svg viewBox="0 0 16 16" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 4l8 8M12 4l-8 8"/></svg>`;
  const mark = (i, size) => `<span class="p14-mk">${[0,1,2,3].map(k => `<i style="width:${size[0]}px;height:${size[1]}px;background:${k <= i ? FILL[i] : T.s3}"></i>`).join('')}</span>`;

  // The four questions the rest of the site asks, in its order, then activity.
  const C = D.counts || {Destination: {}};                   // counts with Utah chosen (their own group ignores itself)
  const WHERE = Object.entries(C.Destination).sort((a, b) => b[1] - a[1]);
  const LEVELS = ['Easy', 'Moderate', 'Challenging', 'Strenuous'];
  const openPhone = () => { const b = aside.querySelector('button[aria-controls="trip-filters"]'); if (b && b.getAttribute('aria-expanded') !== 'true') b.click(); };

  css.push(`.p14-mk{display:inline-flex;gap:2px;vertical-align:middle}.p14-mk i{display:block;border-radius:1px}`);

  function setCount(n, label) { countP.innerHTML = `<b class="font-bold text-ink-900">${n}</b> trips ${label}`; }

  // ------------------------------------------------------------ A: as it ships
  if (variant === 'a') { if (phone) openPhone(); return 'ok'; }

  // ------------------------------------------------------------ B: tick-box list
  if (variant === 'b') {
    const row = (label, n, on) => `<li class="p14-row${on ? ' on' : ''}"><span class="p14-box">${on ? tick : ''}</span><span class="p14-lab">${label}</span><span class="p14-n">${n}</span></li>`;
    const group = (title, items, open, more) => `<div class="p14-g"><div class="p14-gh"><span>${title}</span>${chev(open)}</div>` +
      (open ? `<ul class="p14-list">${items.map(([l, n, on]) => row(l, n, on)).join('')}</ul>${more || ''}` : '') + `</div>`;
    const styles = Object.entries(C.Style).filter(([, n]) => n > 0);
    const durs = Object.entries(C.Duration).filter(([k, n]) => n > 0 && k !== 'Half day' && k !== '1 day');
    filters.innerHTML = `<div class="p14-top"><span>Filter</span><a>Clear all</a></div>` +
      group('Where', WHERE.slice(0, 7).map(([l, n]) => [l, n, l === 'Utah']), true, `<a class="p14-more">Show all ${WHERE.length} places</a>`) +
      group('When', Object.entries(C.When).map(([l, n]) => [l, n]), true) +
      group('How long', durs.map(([l, n]) => [l, n]), true) +
      group('How you travel', styles.map(([l, n]) => [l, n]), true) +
      group('Activity level', LEVELS.map((l) => [l, C['Activity level'][l]]), false);
    css.push(`#trip-filters{display:block!important}#trip-filters > *{margin-top:0!important;margin-bottom:0!important}
      @media (max-width:700px){.p14-top > span{visibility:hidden}}
      .p14-top{display:flex;justify-content:space-between;align-items:baseline;padding:0 0 10px;font:700 17px/1.2 var(--font-display);color:${T.ink9}}
      .p14-top a{font:600 13.5px/1 var(--font-display);color:${T.rust}}
      .p14-g{border-top:1px solid ${T.s3};padding:12px 0 10px}
      .p14-g:last-child{border-bottom:1px solid ${T.s3}}
      .p14-gh{display:flex;justify-content:space-between;align-items:center;font:700 14.5px/1.2 var(--font-display);color:${T.ink9};min-height:24px}
      .p14-list{margin:6px 0 0;padding:0;list-style:none}
      .p14-row{display:flex;align-items:center;gap:10px;min-height:31px;font:500 15px/1.2 var(--font-body);color:${T.ink7}}
      .p14-box{flex:none;width:18px;height:18px;border:1.5px solid ${T.ink3};border-radius:4px;display:grid;place-items:center;background:#fff}
      .p14-row.on .p14-box{background:${T.rust};border-color:${T.rust}}
      .p14-row.on .p14-lab{color:${T.ink9};font-weight:700}
      .p14-lab{flex:1}
      .p14-n{font:500 13px/1 var(--font-body);color:${T.ink3};font-variant-numeric:tabular-nums}
      .p14-more{display:inline-block;margin:6px 0 2px 28px;font:600 13.5px/1 var(--font-display);color:${T.rust}}`);
    setCount(D.total, 'in Utah');
    if (phone) openPhone();
    return 'ok';
  }

  // ------------------------------------------------------------ C: dropdown bar on top
  if (variant === 'c') {
    aside.style.display = 'none';
    outer.style.gridTemplateColumns = '1fr';
    const grid = results.querySelector('.grid');
    if (!phone) grid.style.gridTemplateColumns = 'repeat(4,minmax(0,1fr))';
    const dd = (k, v, set, open) => `<div class="p14-dd${set ? ' set' : ''}${open ? ' open' : ''}"><span class="p14-k">${k}</span><span class="p14-v">${v}</span>${chev(open)}</div>`;
    const styles = Object.entries(C.Style).filter(([, n]) => n > 0);
    const menu = `<div class="p14-menu">${styles.map(([l, n]) => `<div class="p14-mi"><span>${l}</span><span class="p14-n">${n}</span></div>`).join('')}</div>`;
    const bar = document.createElement('div');
    bar.className = 'p14-bar';
    bar.innerHTML = `<div class="p14-dds">${dd('Where', 'Utah', true)}${dd('When', 'Any time of year')}${dd('How long', 'Any length')}` +
      `<div class="p14-wrap">${dd('How you travel', 'Any style', false, !phone)}${phone ? '' : menu}</div>${dd('Activity', 'Any level')}</div>`;
    const tags = document.createElement('div');
    tags.className = 'p14-tags';
    tags.innerHTML = `<b>${D.total} trips</b><span class="p14-tag">Utah ${x}</span><a>Clear all</a>`;
    outer.parentElement.insertBefore(bar, outer);
    countP.replaceWith(tags);
    css.push(`.p14-bar{margin-top:28px;background:${T.navy8};border-radius:4px;padding:14px}
      .p14-dds{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
      .p14-wrap{position:relative}
      .p14-dd{position:relative;display:grid;grid-template-columns:1fr auto;grid-template-rows:auto auto;align-items:center;column-gap:8px;background:#fff;border:1px solid ${T.s3};border-radius:3px;padding:7px 12px 8px;min-height:52px}
      .p14-dd svg{grid-row:1 / span 2;grid-column:2}
      .p14-k{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font:700 11.5px/1.2 var(--font-display);letter-spacing:.1em;text-transform:uppercase;color:${T.ink3}}
      .p14-v{font:500 16px/1.3 var(--font-body);color:${T.ink7};white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
      .p14-dd.set .p14-v{color:${T.ink9};font-weight:700}
      .p14-dd.open{border-color:${T.rust};box-shadow:0 0 0 1px ${T.rust}}
      .p14-menu{position:absolute;z-index:40;left:0;right:0;top:calc(100% + 6px);background:#fff;border:1px solid ${T.s3};border-radius:4px;box-shadow:0 18px 40px rgba(5,18,31,.22);padding:6px 0}
      .p14-mi{display:flex;justify-content:space-between;align-items:center;padding:0 14px;min-height:40px;font:500 15px/1.2 var(--font-body);color:${T.ink7}}
      .p14-mi:hover,.p14-mi:first-child{background:${T.s1}}
      .p14-n{font:500 13px/1 var(--font-body);color:${T.ink3};font-variant-numeric:tabular-nums}
      .p14-tags{display:flex;flex-wrap:wrap;align-items:center;gap:10px;font:600 14px/1 var(--font-display);color:${T.ink5}}
      .p14-tags b{color:${T.ink9};margin-right:4px}
      .p14-tag{display:inline-flex;align-items:center;gap:8px;background:${T.rust1};color:${T.rust7};border-radius:3px;padding:7px 10px;font:600 13.5px/1 var(--font-display)}
      .p14-tags a{color:${T.rust};margin-left:4px}
      @media (max-width:700px){.p14-dds{grid-template-columns:1fr 1fr}.p14-dds > :last-child{grid-column:span 2}.p14-bar{margin-top:20px;padding:10px}}`);
    return 'ok';
  }

  // ------------------------------------------------------------ D: a control per question
  if (variant === 'd') {
    const g = (title, body) => `<div class="p14-g"><div class="p14-gh">${title}</div>${body}</div>`;
    const where = `<ul class="p14-two">${WHERE.slice(0, 10).map(([l, n]) => `<li class="${l === 'Utah' ? 'on' : ''}"><span>${l}</span><span class="p14-n">${n}</span></li>`).join('')}</ul><a class="p14-more">All ${WHERE.length} places</a>`;
    const seasons = `<div class="p14-seg s4">${Object.entries(C.When).map(([l, n]) => `<span><b>${l}</b><em>${n}</em></span>`).join('')}</div>`;
    const dmap = [['A day or less', 'A day'], ['2-3 days', '2&ndash;3'], ['4-6 days', '4&ndash;6'], ['7-10 days', '7&ndash;10'], ['11+ days', '11+']];
    const durs = `<div class="p14-seg s5">${dmap.map(([k, l]) => `<span><b>${l}</b><em>${C.Duration[k]}</em></span>`).join('')}</div><div class="p14-cap">days, or less</div>`;
    const styles = `<ul class="p14-rows">${Object.entries(C.Style).filter(([, n]) => n > 0).map(([l, n]) => `<li><span>${l}</span><span class="p14-n">${n}</span></li>`).join('')}</ul>`;
    const lv = `<div class="p14-lv">${LEVELS.map((l, i) => `<span>${mark(i, [9, 7])}<b>${l}</b><em>${C['Activity level'][l]}</em></span>`).join('')}</div>`;
    filters.innerHTML = `<div class="p14-top"><span>Filter</span><a>Clear all</a></div>` +
      g('Where', where) + g('When', seasons) + g('How long', durs) + g('How you travel', styles) + g('How active', lv);
    css.push(`#trip-filters{display:block!important}#trip-filters > *{margin-top:0!important;margin-bottom:0!important}
      @media (max-width:700px){.p14-top > span{visibility:hidden}}
      .p14-top{display:flex;justify-content:space-between;align-items:baseline;padding:0 0 10px;font:700 17px/1.2 var(--font-display);color:${T.ink9}}
      .p14-top a,.p14-more{font:600 13.5px/1 var(--font-display);color:${T.rust}}
      .p14-more{display:inline-block;margin-top:8px}
      .p14-g{border-top:1px solid ${T.s3};padding:13px 0 14px}
      .p14-g:last-child{border-bottom:1px solid ${T.s3}}
      .p14-gh{font:700 14.5px/1.2 var(--font-display);color:${T.ink9};margin-bottom:9px}
      .p14-n{font:500 12.5px/1 var(--font-body);color:${T.ink3};font-variant-numeric:tabular-nums}
      .p14-two{display:grid;grid-template-columns:1fr 1fr;column-gap:16px;margin:0;padding:0;list-style:none}
      .p14-two li,.p14-rows li{display:flex;justify-content:space-between;align-items:center;min-height:29px;font:500 14.5px/1.2 var(--font-body);color:${T.ink7};border-left:3px solid transparent;padding-left:7px;margin-left:-10px}
      .p14-two li.on{border-left-color:${T.rust};color:${T.ink9};font-weight:700}
      .p14-rows{margin:0;padding:0;list-style:none}
      .p14-seg{display:grid;border:1px solid ${T.s3};border-radius:4px;overflow:hidden;background:#fff}
      .p14-seg.s4{grid-template-columns:repeat(2,1fr)}.p14-seg.s5{grid-template-columns:repeat(5,1fr)}
      .p14-seg > span{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;min-height:48px;border-right:1px solid ${T.s3};border-bottom:1px solid ${T.s3};margin:0 -1px -1px 0}
      .p14-seg b{font:600 14px/1 var(--font-display);color:${T.ink7}}
      .p14-seg em,.p14-lv em{font:500 11.5px/1 var(--font-body);font-style:normal;color:${T.ink3}}
      .p14-cap{margin-top:6px;font:500 12px/1 var(--font-body);color:${T.ink3}}
      .p14-lv{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
      .p14-lv > span{display:flex;flex-direction:column;align-items:center;gap:6px;border:1px solid ${T.s3};border-radius:4px;padding:10px 2px 9px;background:#fff}
      .p14-lv b{font:600 12px/1 var(--font-display);color:${T.ink7}}`);
    setCount(D.total, 'in Utah');
    if (phone) openPhone();
    return 'ok';
  }

  // ------------------------------------------------------------ 83: search
  const input = document.querySelector('#find-q');
  const grid = results.querySelector('.grid');
  function showOnly(slugs) {
    const cells = [...grid.children];
    const bySlug = new Map(cells.map((c) => [c.querySelector('a[href^="/tours/"]')?.getAttribute('href').split('/')[2], c]));
    cells.forEach((c) => c.remove());
    slugs.forEach((s) => { const c = bySlug.get(s); if (c) { c.classList.remove('defer-offscreen'); grid.appendChild(c); } });
  }
  const q = D.q;
  if (variant === 'sa') {
    input.value = q;
    grid.innerHTML = '';
    countP.innerHTML = `<b class="font-bold text-ink-900">0</b> trips matching`;
    const p = document.createElement('p');
    p.className = 'max-w-xl text-ink-500';
    p.innerHTML = 'Nothing in the catalogue matches that. <a class="font-semibold text-rust-600">Clear the filters</a> and start again.';
    grid.replaceWith(p);
    return 'ok';
  }
  if (variant === 'sb' || variant === 'sd') {
    input.value = q;
    showOnly(D.slugs);
    countP.innerHTML = variant === "sd" ? `<b class="font-bold text-ink-900">${D.slugs.length}</b> trips for Yosemite` : `<b class="font-bold text-ink-900">${D.slugs.length}</b> trips matching &ldquo;${q}&rdquo;`;
    if (variant === 'sd') {
      const btn = input.parentElement.querySelector('button');
      btn.remove();
      input.parentElement.style.maxWidth = '640px';
      const tryRow = document.createElement('div');
      tryRow.className = 'p14-try';
      tryRow.innerHTML = `<span>Try</span>${D.tries.map((t) => `<a>${t}</a>`).join('')}`;
      input.parentElement.after(tryRow);
      if (D.understood) {
        const u = document.createElement('p');
        u.className = 'p14-und';
        u.innerHTML = D.understood;
        countP.after(u);
      }
      css.push(`.p14-try{display:flex;flex-wrap:wrap;gap:6px 18px;align-items:center;margin-top:12px;font:500 14.5px/1.3 var(--font-body)}
        .p14-try span{font:700 11.5px/1 var(--font-display);letter-spacing:.1em;text-transform:uppercase;color:${T.ink3}}
        .p14-try a{color:${T.ink7};text-decoration:underline;text-decoration-color:${T.s3};text-underline-offset:4px}
        .p14-und{margin-top:6px;font:500 14px/1.4 var(--font-body);color:${T.ink5}}
        .p14-und b{color:${T.ink9}}`);
    }
    return 'ok';
  }
  if (variant === 'sc') {
    input.value = q;
    input.style.borderColor = T.rust;
    const form = input.parentElement;
    form.style.position = 'relative';
    const box = document.createElement('div');
    box.className = 'p14-ta';
    const sec = (h, items) => `<div class="p14-tah">${h}</div>` + items.map(([l, s, n]) => `<div class="p14-tai"><span class="p14-tl">${l}</span><span class="p14-tas">${s || ''}</span><span class="p14-n">${n || ''}</span></div>`).join('');
    box.innerHTML = sec('Places', D.ta.places) + sec('Trips', D.ta.trips) + sec('Ways to travel', D.ta.styles) +
      `<div class="p14-taf">See all ${D.ta.all} trips for &ldquo;${q}&rdquo; &rarr;</div>`;
    form.appendChild(box);
    css.push(`.p14-ta{position:absolute;z-index:50;left:0;top:calc(100% + 6px);width:${phone ? '100%' : 'calc(100% - 96px)'};background:#fff;border:1px solid ${T.s3};border-radius:4px;box-shadow:0 20px 44px rgba(5,18,31,.24);padding:6px 0 0;text-align:left}
      .p14-tah{padding:10px 16px 4px;font:700 11.5px/1 var(--font-display);letter-spacing:.1em;text-transform:uppercase;color:${T.ink3}}
      .p14-tai{display:flex;align-items:baseline;gap:8px;padding:0 16px;min-height:38px;align-items:center;font:600 15px/1.25 var(--font-body);color:${T.ink9}}
      .p14-tai:nth-child(2){background:${T.s1}}
      .p14-tai mark{background:none;color:${T.rust7};font-weight:800}
      .p14-tas{flex:1;font:500 13.5px/1.2 var(--font-body);color:${T.ink3};white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
      .p14-n{font:500 13px/1 var(--font-body);color:${T.ink3};font-variant-numeric:tabular-nums}
      .p14-taf{margin-top:6px;border-top:1px solid ${T.s3};padding:12px 16px;font:600 14px/1 var(--font-display);color:${T.rust}}`);
    return 'ok';
  }
  return 'unknown';
}

window.__proto = function (v, d) {
  const css = [];
  const r = __run(v, d, css);
  const s = document.createElement('style');
  s.textContent = css.join('\n');
  document.head.appendChild(s);
  return r;
};
