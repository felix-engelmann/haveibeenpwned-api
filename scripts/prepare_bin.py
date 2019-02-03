import sys

from struct import pack

if len(sys.argv) != 3:
    print("usage: %s <input.txt> <outout.dat>\n"
          % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1]) as src:
    with open(sys.argv[2], 'wb') as dst:
        for l in src:
            p = l.split(':')
            by = [int(p[0][i:i + 2], 16) for i in range(0, len(p[0]), 2)]
            print(by)
            binary = pack("<" + "B" * 20 + "I",
                          *[int(p[0][i:i + 2], 16) for i in
                            range(0, len(p[0]), 2)],
                          int(p[1]))
            dst.write(binary)
