// Applied to the LIVE phone page to prototype each option. Returns nothing.
window.__proto = function (variant) {
  const css = [];
  const T = {rust:'#e4622a', ink9:'#12212e', ink7:'#2c4356', ink5:'#42596c', ink3:'#7d93a3', s1:'#eef4f8', s3:'#d6e1e9'};
  const chev = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="'+T.ink3+'" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>';
  const it = document.querySelector('#itinerary');
  const days = it ? [...it.querySelectorAll('li[id^="day-"]')] : [];
  function dayInfo(li) {
    const img = li.querySelector('figure img');
    const chip = [...li.querySelectorAll('.mt-4.flex.flex-wrap.gap-2 > span')].find(s => /^Overnight/.test(s.textContent.trim()));
    return {src: img ? (img.currentSrc || img.src) : '', label: (li.querySelector('p')?.textContent || '').trim(),
      title: (li.querySelector('h3')?.textContent || '').trim(),
      night: chip ? chip.textContent.trim().replace(/^Overnight/, '').trim() : ''};
  }
  function fold() {
    days.forEach((li, i) => {
      const d = dayInfo(li);
      const row = document.createElement('div');
      row.className = 'pr-row';
      row.innerHTML = (d.src ? '<img src="' + d.src + '" alt="">' : '<span class="pr-noimg"></span>') +
        '<span class="pr-t"><span class="pr-l">' + d.label + (d.night ? ' <em>&middot; ' + d.night + '</em>' : '') + '</span>' +
        '<span class="pr-h">' + d.title + '</span></span><span class="pr-c">' + chev + '</span>';
      [...li.children].forEach(c => c.style.display = 'none');
      li.appendChild(row);
    });
    css.push(`#itinerary li[id^="day-"]{border-top:1px solid ${T.s3};margin:0!important;padding:0!important}
      #itinerary li[id^="day-"]:last-child{border-bottom:1px solid ${T.s3}}
      #itinerary ol:has(> li[id^="day-"]), #itinerary ul:has(> li[id^="day-"]){gap:0!important;row-gap:0!important}
      #itinerary ol:has(> li[id^="day-"]) > * + *, #itinerary ul:has(> li[id^="day-"]) > * + *{margin-top:0!important}
      .pr-row{display:flex;align-items:center;gap:14px;padding:12px 0;min-height:44px}
      .pr-row img,.pr-noimg{width:76px;height:57px;object-fit:cover;border-radius:2px;flex:none;background:${T.s1}}
      .pr-t{flex:1;min-width:0;display:block}
      .pr-l{display:block;font:600 12px/1.4 var(--font-display);text-transform:uppercase;letter-spacing:.05em;color:${T.rust}}
      .pr-l em{font-style:normal;color:${T.ink3};text-transform:none;letter-spacing:0;font-weight:500;font-size:13px}
      .pr-h{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;margin-top:2px;font:700 16.5px/1.3 var(--font-display);color:${T.ink9}}
      .pr-c{flex:none;width:32px;display:grid;place-items:center}`);
  }
  function shortDays() {
    days.forEach((li, i) => {
      const d = dayInfo(li);
      const fig = li.querySelector('figure');
      const figWrap = fig && fig.parentElement;
      if (figWrap) figWrap.style.display = 'none';
      const head = li.querySelector('p');
      const h3 = li.querySelector('h3');
      const top = document.createElement('div');
      top.className = 'pr-top';
      top.innerHTML = d.src ? '<img src="' + d.src + '" alt="">' : '';
      const tt = document.createElement('div'); tt.className = 'pr-tt';
      head.parentElement.insertBefore(top, head);
      tt.appendChild(head); tt.appendChild(h3); top.appendChild(tt);
      const prose = li.querySelector('.prose-trip');
      if (prose) {
        prose.classList.add('pr-clamp');
        const more = document.createElement('a');
        more.className = 'pr-more'; more.textContent = 'Read all of ' + d.label;
        prose.after(more);
      }
    });
    css.push(`.pr-top{display:flex;gap:14px;align-items:center}
      .pr-top img{width:112px;height:84px;object-fit:cover;border-radius:2px;flex:none}
      .pr-tt{min-width:0}.pr-tt h3{font-size:18px!important;margin-top:2px!important}
      .pr-clamp{max-height:${16*1.625*4}px;overflow:hidden;-webkit-mask-image:linear-gradient(#000 60%,transparent)}
      .pr-more{display:inline-block;margin-top:6px;font:600 15px/1.4 var(--font-display);color:${T.rust};text-decoration:underline;text-underline-offset:3px}
      #itinerary li[id^="day-"] > div{gap:12px!important}`);
    // the day list's own spacing stays as it ships
  }
  function dropGlance() {
    // The trip-at-a-glance strip: the folded rows ARE the glance now.
    const glance = it && it.querySelector('nav[aria-label="Trip at a glance"]');
    if (glance) { const w = glance.closest('div.mt-5'); const p = w && w.querySelector(':scope > p');
      if (p) p.style.display = 'none'; glance.parentElement.style.display = 'none'; }
  }
  function tighten(photos) {
    // 2. Tour details: first five included items, the rest behind one line; everything else a closed row.
    const det = document.querySelector('#details');
    if (det) {
      const cards = det.querySelectorAll(':scope > div:first-of-type > div');
      cards.forEach((c, i) => {
        const lis = [...c.querySelectorAll('li')];
        const n = lis.length;
        if (i === 0) { lis.slice(5).forEach(l => l.style.display = 'none');
          if (n > 5) { const a = document.createElement('a'); a.className = 'pr-more'; a.textContent = 'Show all ' + n + ' things included'; c.appendChild(a); } }
        else { c.querySelector('div.mt-3').style.display = 'none'; c.classList.add('pr-closed');
          c.querySelector('h3').insertAdjacentHTML('beforeend', '<span class="pr-c pr-cr">' + chev + '</span>'); }
      });
      const rest = det.querySelector(':scope > div.grid.gap-8');
      if (rest) {
        const hs = [...rest.querySelectorAll('h3')].map(h => h.textContent.trim());
        rest.innerHTML = hs.map(h => '<div class="pr-line"><span>' + h + '</span>' + chev + '</div>').join('');
        rest.className = 'pr-lines';
      }
    }
    // 3. Photo sections: one sideways row each instead of a grid.
    if (photos) ['#gallery', '#more-photos'].forEach(s => { const g = document.querySelector(s + ' .grid'); if (g) g.classList.add('pr-swipe'); });
    // 4. Trip protection: the lead paragraph, then the five questions behind one line.
    const pro = document.querySelector('#protection');
    if (pro) { const q = pro.querySelector(':scope > div.grid'); const n = q ? q.children.length : 0;
      if (q) q.outerHTML = '<div class="pr-line pr-line1"><span>' + n + ' questions answered: what it covers, when to buy, refunds</span>' + chev + '</div>';
      const lead = pro.querySelector(':scope > p'); if (lead) lead.classList.add('pr-clamp3'); }
    css.push(`.pr-closed{padding-top:14px!important;padding-bottom:14px!important}
      .pr-closed h3{display:flex!important;align-items:center}.pr-cr{margin-left:auto}
      #details .pr-more{margin-top:12px}
      .pr-lines{margin-top:16px;border-top:1px solid ${T.s3}}
      .pr-line{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:52px;border-bottom:1px solid ${T.s3};font:600 12px/1.4 var(--font-display);text-transform:uppercase;letter-spacing:.05em;color:${T.ink9}}
      .pr-line1{margin-top:16px;border-top:1px solid ${T.s3};text-transform:none;letter-spacing:0;font-size:15px;color:${T.ink7};padding:6px 0}
      .pr-clamp3{max-height:${17*1.75*3}px;overflow:hidden;-webkit-mask-image:linear-gradient(#000 55%,transparent)}
      .pr-swipe{display:flex!important;overflow-x:auto;gap:8px!important;margin-right:-20px;padding-right:20px;scrollbar-width:none}
      .pr-swipe > figure{flex:0 0 250px!important;grid-column:auto!important;aspect-ratio:4/3}`);
  }
  css.push(`.pr-more{display:inline-block;margin-top:6px;font:600 15px/1.4 var(--font-display);color:${T.rust}!important;text-decoration:underline;text-underline-offset:3px}`);
  if (variant === 'fold') { fold(); dropGlance(); }
  if (variant === 'short') shortDays();
  if (variant === 'lists') tighten(false);
  if (variant === 'photos') tighten(true);
  const st = document.createElement('style'); st.textContent = css.join('\n'); document.head.appendChild(st);
};
