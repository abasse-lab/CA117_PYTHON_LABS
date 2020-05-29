#!/usr/bin/env python3

import sys

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
words = ['zero']
nums = list(range(101))
for word in digits + teens:
    words.append(word)

for tens_word in tens:
    words.append(tens_word)

    for digit_word in digits:
        words.append(tens_word + '-' + digit_word)
words.append('one hundred')
thebigdic = {}
i = 0
while i < len(nums):
    thebigdic[str(nums[i])] = words[i]
    i += 1

lines = sys.stdin.readlines()
for line in lines:
    a = []
    line = line.strip().split()
    i = 0
    while i < len(line):
        a.append(thebigdic[line[i]])
        i += 1

    print(" ".join(a))
