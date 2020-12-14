#!/usr/bin/env python3
import sys
import re


def part1(lines):
    result = 0
    lines = lines.split("\n\n")
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for l in lines:
        s = set()
        for pair in l.split():
            key, _ = pair.split(":")
            s.add(key)

        if all([x in s for x in required]):
            result += 1

    return result


def part2(lines):
    result = 0
    lines = lines.split("\n\n")
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for l in lines:
        d = {}
        for pair in l.split():
            key, value = pair.split(":")
            d[key] = value

        if all([x in d.keys() for x in required]) and all([validate(k, v) for k, v in d.items()]):
            result += 1

    return result


def validate(key, value):
    if key == "byr":
        return (1920 <= int(value)) and (int(value) <= 2002)
    elif key == "iyr":
        return (2010 <= int(value)) and (int(value) <= 2020)
    elif key == "eyr":
        return (2020 <= int(value)) and (int(value) <= 2030)
    elif key == "hgt":
        value, t = value[:-2] ,value[-2:]
        if t == "cm":
            return (150 <= int(value)) and (int(value) <= 193)
        elif t == "in":
            return (59 <= int(value)) and (int(value) <= 76)
    elif key == "hcl":
        return re.match("^#[0-9a-f]{6}$", value) is not None
    elif key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif key == "pid":
        return re.match("^[0-9]{9}$", value) is not None
    elif key == "cid":
        return True

    return False


lines = sys.stdin.read()

print(part1(lines))
print('-----')
print(part2(lines))

debug = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

assert(part1(debug) == 2)

invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

# assert(part2(invalid) == 0)
# assert(part2(valid) == 4)
