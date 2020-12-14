#!/usr/bin/env python3
import sys
import re


def get_rules(lines):
    rules = {}
    pattern1 = re.compile(r".+no other bags.$")

    for l in lines.splitlines():
        if not re.match(pattern1, l):
            l = l.split()
            key = " ".join(l[:3])
            contains = []
            l = " ".join(l[4:])

            for x in l.split(","):
                x = x.split()
                n, color = int(x[0]), " ".join(x[1:3])
                contains.append((color, n))

            rules[key] = contains

    return rules


def bags_containing(name, rules, s):
    for i in rules.keys():
        for j in rules[i]:
            if j[0] == name:
                s.add(i)
                s = s.union(bags_containing(i, rules, s))

    return s


def count_bags(name, rules):
    result = 1
    if not rules.get(name):
        return result

    for bag in rules.get(name):
        for i in range(bag[1]):
            result += count_bags(bag[0], rules)

    return result


def part1(lines):
    result = 0
    rules = get_rules(lines)
    result = len(bags_containing("shiny gold", rules, set()))
    return result


def part2(lines):
    result = 0
    rules = get_rules(lines)
    print(rules)

    result = count_bags("shiny gold", rules) - 1
    return result

def main():
    lines = sys.stdin.read().rstrip()
    # print(part1(lines))
    print(part2(lines))

    debug = """light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags."""

    # print(part1(debug))

    debug2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

    # print(part2(debug2))

main()
