#!/usr/bin/env python3
import sys
from functools import reduce


def part1(lines):
    result = 0
    x = 0
    for l in lines[1:]:
        l = l.rstrip()
        x += 3
        if (x >= len(l)):
            x %= len(l)

        if (l[x] == '#'):
            result += 1

    return result


def part2(lines):
    results = [0,0,0,0,0]
    x = [0,0,0,0,0]

    for count, l in enumerate(lines[1:]):
        l = l.rstrip()

        for i in range(4):
            x[i] += i*2 + 1
            if (x[i] >= len(l)):
                x[i] %= len(l)

            if (l[x[i]] == '#'):
                results[i] += 1

        if ((count+1) % 2 == 0):
            x[4] += 1

            if (x[4] >= len(l)):
                x[4] = 0

            if (l[x[4]] == '#'):
                results[4] += 1

    return reduce(lambda x, y: x*y, results)


lines = sys.stdin.readlines()

print(part1(lines))
print('-----')
print(part2(lines))

debug = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

assert(part1(debug.splitlines()) == 7)
assert(part2(debug.splitlines()) == 336)
