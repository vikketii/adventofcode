#!/usr/bin/env python3
import sys


def parts(lines):
    result = 0
    ids = []

    for l in lines.splitlines():
        rows, columns = l[:7], l[7:]

        r = (0, 127)
        for i in rows:
            if i == "F":
                r = (r[0], r[1] - ((r[1] - r[0]+1) // 2))
            elif i == "B":
                r = (r[0] + ((r[1] - r[0] + 1) // 2), r[1])

        c = (0, 7)
        for i in columns:
            if i == "L":
                c = (c[0], c[1] + (-(c[1] - c[0]) // 2))
            elif i == "R":
                c = (c[0] - (-(c[1] - c[0]) // 2), c[1])

        result = max(result, r[0]*8 + c[0])
        ids.append(r[0]*8+c[0])

    print([x for x in range(min(ids),max(ids)) if x not in ids])
    return result


lines = sys.stdin.read()
print(parts(lines))
