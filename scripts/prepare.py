import sys

if len(sys.argv) != 4:
    print("usage: %s <input.txt> <padding> <outout.txt>\n"
          "the padding parameter specifies the total length"
          " of the frequency count in digits"
          % sys.argv[0])
    sys.exit(1)

f_str = "%%s:%%0%dd\n" % int(sys.argv[2])

with open(sys.argv[1]) as src:
    with open(sys.argv[3], 'w') as dst:
        for l in src:
            p = l.split(':')
            dst.write(f_str % (p[0], int(p[1])))
