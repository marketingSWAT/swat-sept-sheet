import json, os, sys, collections, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import search as S
D = S.D
def slugs(q): return [t['slug'] for t in S.smart(q)[0]]
zb = slugs('zion bryce')
y = slugs('yosemitee')
zt, _, _, _ = S.smart('zion')
parks = collections.Counter(p for t in S.CAT for p in t['parks'] if 'zion' in p.lower())
places = [(p.replace('Zion', '<mark>Zion</mark>'), 'National park' if 'National Park' in p else '', f'{n} trips') for p, n in parks.most_common(3)]
trips = [(t['name'].replace('Zion', '<mark>Zion</mark>').replace(' - Park', ''), (lambda d: '' if not d else ('1 day' if float(d) <= 1 else f"{float(d):.0f} days"))(t.get('duration_days')), '') for t in zt[:4]]
st = collections.Counter(t['style'] for t in zt)
PL = {'Guided small group': 'Small group tours', 'Day tour': 'Day tours', 'Self-drive': 'Self-drive trips'}
styles = [(f'{PL.get(s, s)} in <mark>Zion</mark>', '', f'{n} trips') for s, n in st.most_common(2)]
out = {'zb': {'q': 'zion bryce', 'slugs': zb},
       'y': {'q': 'yosemitee', 'slugs': y, 'understood': 'Showing trips for <b>Yosemite</b>. You typed &ldquo;yosemitee&rdquo;.',
             'tries': ['Zion and Bryce', 'Yellowstone in winter', 'A day from Salt Lake', 'River cruises', 'Backpacking']},
       'ta': {'q': 'zion', 'places': places, 'trips': trips, 'styles': styles, 'all': len(zt)}}
print(json.dumps(out, indent=1)[:2500])
json.dump(out, open(os.path.join(D, 'searchdata.json'), 'w'), indent=1)
