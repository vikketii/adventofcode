#!/usr/bin/env python3
import sys


def part1(lines):
    result = 0

    for l in lines.split("\n\n"):
        s = set()
        for c in l.rstrip():
            if (97 <= ord(c) <= 122):
                s.add(c)
        result += len(s)

    return result


def part2(lines):
    result = 0

    for group in lines.split("\n\n"):
        d = {}
        people = group.split("\n")
        print(group)
        for person in people:
            for c in person:
                if (97 <= ord(c) <= 122):
                    d[c] = d.get(c, 0) + 1

        result += len([x for x in d if d[x] == len(people)])
        print(result)
        print("----")

    return result

lines = sys.stdin.read()
# print(part1(lines))
print(part2(lines))

debug = """abc

a
b
c

ab
ac

a
a
a
a

b"""

assert(part1(debug) == 11)
assert(part2(debug) == 6)
