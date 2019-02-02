# v4 = 23174662
#     000000004

import sys

if len(sys.argv) != 2:
    print("usage: %s <input.txt>\ndetermines the largest frequency"%sys.argv[0])
    sys.exit(1)

largest = 0
with open(sys.argv[1]) as src:
    for l in src:
        p = l.split(':')
        if int(p[1]) > largest:
            largest=int(p[1])

print(largest)