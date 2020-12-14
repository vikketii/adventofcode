#!/usr/bin/env python3
import sys
import re


def part1(lines):
    correct = 0

    for l in lines:
        m = re.match(r'([0-9]+)-([0-9]+).+?([a-z]):.+?([a-z]+)', l)
        if m:
            a, b, c, s = m.group(1, 2, 3, 4)
            if (int(a) <= s.count(c) and s.count(c) <= int(b)):
                correct += 1

    print(correct)


def part2(lines):
    correct = 0

    for l in lines:
        m = re.match(r'([0-9]+)-([0-9]+).+?([a-z]):.+?([a-z]+)', l)
        if m:
            a, b, c, s = m.group(1, 2, 3, 4)
            if ((s[int(a)-1] == c) ^ (s[int(b)-1] == c)):
                correct += 1

    print(correct)


lines = sys.stdin.readlines()
part1(lines)
print('-----')
part2(lines)
