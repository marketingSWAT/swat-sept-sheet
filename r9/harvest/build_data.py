"""Turn the production harvest (content_*.json, 1920 wide, 29 Sep) into the
data the round-nine mockups draw from. Nothing here is invented: every title,
price, badge, photo and paragraph is read off the deployed page."""
import json, re
def small(u, w='w640'):
    return re.sub(r'/derived/w\d+/', f'/derived/{w}/', u) if u else u
def card(c):
    t = [x for x in c['text']]
    style, dur = t[0], t[1]; i = 2; deal = None
    if t[i].startswith('🔥'): deal = t[i].replace('🔥', '').strip(); i += 1
    title = t[i]; i += 1
    route = t[i] if '→' in t[i] else ''; i += 1 if route else 0
    places, activity, group = t[i], t[i+1], t[i+2]; i += 3
    price = t[i]; i += 1; unit = ''
    if price.startswith('$'): unit = t[i]; i += 1
    custom = t[i] == 'Custom-priced'
    action = [x for x in t if x in ('Check dates', 'Request a quote')]
    return dict(style=style, dur=dur, deal=deal, title=title, route=route, places=places,
                activity=activity, group=group, price=price, unit=unit, custom=custom,
                action=action[0] if action else 'Check dates', img=small(c['img']))
D = {}
a = json.load(open('content_destinations_arches-canyonlands-national-parks_1920.json'))
D['arches'] = dict(
    cards=[card(c) for c in a['cards']],
    prose=[b['text'] for b in a['blocks'] if b['tag'] == 'P' and 1000 < b['box'][1] < 1460],
    hikes_p=[b['text'] for b in a['blocks'] if b['tag'] == 'P' and 1500 < b['box'][1] < 1560][0],
    gallery=[small(i['src'], 'w828') for i in a['imgs'] if 3690 <= i['box'][1] < 4700 and i['box'][2] > 300 and i['box'][1] < 4650],
    hikes_card=dict(title='Hikes in Arches National Park', img=small([i['src'] for i in a['imgs'] if i['box'][1] == 4772][0])),
    journal=[dict(title=t, img=small(i['src'])) for t, i in zip(
        ["The Ultimate Four-Season Guide to Utah's Mighty 5",
         'Arches National Park Lifts Timed-Entry Update 2026: What Travelers Need to Know'],
        [i for i in a['imgs'] if i['box'][1] == 5182])],
    departing=['Bryce', 'Las Vegas', 'Moab', 'Salt Lake City'],
    hero=small([i['src'] for i in a['imgs'] if i['box'][1] < 800][0], 'w828') if [i for i in a['imgs'] if i['box'][1] < 800] else None,
)
b = json.load(open('content_departing-from_bryce_1920.json'))
D['bryce'] = dict(cards=[card(c) for c in b['cards']],
    intro=[x['text'] for x in b['blocks'] if x['tag'] == 'P' and x['box'][1] < 450],
    words=[x['text'] for x in b['blocks'] if x['tag'] == 'P' and 2450 < x['box'][1] < 2800],
    groups=['4-6 days', '7-10 days', '11+ days'])
d = json.load(open('content_deals_1920.json'))
D['deals'] = dict(intro=[x['text'] for x in d['blocks'] if x['tag'] == 'P' and 690 < x['box'][1] < 800][0],
    img=small([i['src'] for i in d['imgs'] if i['box'][1] == 822][0], 'w828'))
j = json.load(open('content_journal_exploring-the-last-frontier-my-alaskan-adventure_1920.json'))
art = j['cards'][0]['text']
D['journal'] = dict(meta=art[0], paras=art[1:12], img1=small([i['src'] for i in j['imgs'] if i['box'][1] == 2128][0], 'w828'),
    go=[card(c) for c in j['cards'][1:]],
    keep=[dict(title=x['text'], img=small(i['src'])) for x, i in zip(
        [x for x in j['blocks'] if x['tag'] == 'P' and x['box'][1] > 10400],
        [i for i in j['imgs'] if i['box'][1] == 10380])])
json.dump(D, open('../data.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: {kk: (len(vv) if isinstance(vv, list) else vv if isinstance(vv, str) and len(vv) < 90 else '…') for kk, vv in v.items()} for k, v in D.items()}, indent=1))
print(D['arches']['cards'][5]); print(D['journal']['paras'][:2]); print(D['journal']['keep'])
