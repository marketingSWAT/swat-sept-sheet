import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'build'))
import mocks_about as a
out = os.path.join(os.path.dirname(__file__), '..', 'frag')
for n, f in [('B', a.opt_story), ('C', a.opt_people), ('D', a.opt_first)]:
    open(os.path.join(out, n + '.html'), 'w').write(f())
