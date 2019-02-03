import os


class Pwned():

    def __init__(self, file):

        with open(file) as f:
            self.record_len = len(f.readline())
        self.records = os.stat(file).st_size // self.record_len
        self.file = file
        self.jumpsize = 100

    def lookup(self, query):

        query = ("%%0%dX" % (len(query))) % (int(query, 16))

        with open(self.file) as f:
            L = 0
            R = self.records - 1

            contained = False
            m = 0
            while L <= R:
                m = (L + R) // 2
                f.seek(self.record_len * m)
                content = f.read(len(query))

                if content < query:
                    L = m + 1
                elif content > query:
                    R = m - 1
                else:
                    contained = True
                    break

            if not contained:
                return []
            else:
                if m - self.jumpsize >= 0:
                    start = m - self.jumpsize
                else:
                    start = 0
                f.seek(self.record_len * start)
                content = f.read(len(query))

                while content == query:
                    if start - 100 >= 0:
                        start -= 100
                    else:
                        start = 0
                        break
                    f.seek(self.record_len * start)
                    content = f.read(len(query))

                f.seek(self.record_len * start)
                hits = []
                for l in f:
                    if l[:len(query)] < query:
                        continue
                    elif l[:len(query)] > query:
                        break
                    else:
                        hits.append("%s:%s" % (l[len(query):40], int(l[41:])))
                return hits
