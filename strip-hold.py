#!/usr/bin/env python3
"""Strip HOLD-marked regions (local-only content, e.g. the simulations) from
nown-site.html to produce the public build. Usage: strip-hold.py IN OUT"""
import re, sys
s = open(sys.argv[1]).read()
s = re.sub(r'(/\*HOLD-START\*/|<!--HOLD-START-->).*?(/\*HOLD-END\*/|<!--HOLD-END-->)\n?', '', s, flags=re.S)
assert 'HOLD-START' not in s and 'HOLD-END' not in s
assert 'id="simulations"' not in s, 'simulations leaked into public build'
open(sys.argv[2], 'w').write(s)
print(f'public build written: {len(s):,} bytes')
