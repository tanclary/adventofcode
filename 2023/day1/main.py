# import a bunch of stuff you might use or maybe not
import sys
import numpy as np
import re


def find_ans(lines):
    # very nice dictionary that matches all word and digit forms very nice no need to pay much 
    # attention
    d = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    # store the number for each line
    ans = []
    # capturing groups that will match any of the above keys
    regex = "(" + "|".join(d.keys()) + ")"
    # go through the lines one by one
    for line in lines:
        # find the first match and multiply by 10 so you get the tens digit 
        first = d[re.search(regex, line).group(1)] * 10
        # find the last match using some regex magic
        second = d[re.search("(?s:.*)" + regex, line).group(1)]
        # append the "tota" for that line
        ans.append(first + second)
    # print ya answer
    print(sum(ans))


def part_1(lines):
    # just good code practices
    find_ans(lines)


def part_2(lines):
    # good stuff
    ans = 0

    for line in lines:
        ans += 0
    print(ans)


# read your input
with open('input.txt') as f:
    data = f.read().splitlines()
# do this for some reason
part_1(data)
part_2(data)
