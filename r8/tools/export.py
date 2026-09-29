"""Write each of Claude's mocks as a bare fragment, so preview.mjs (and Codex)
can render them exactly as the sheet hosts them."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'build'))
import mocks_i as I
OUT = os.path.join(HERE, '..', 'frag')
for name, fn in [('now', I.now), ('calendar', I.opt_calendar), ('wall', I.opt_wall), ('year', I.opt_year)]:
    open(os.path.join(OUT, name + '.html'), 'w').write(fn())
    print(name)
