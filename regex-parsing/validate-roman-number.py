# https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true
# Roman numbers: (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
#         (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
#         (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
#         (1, "I")

import re

regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
# new_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
# s = input()
# result = re.findall(new_pattern, s)
# print(result)
# matches = re.compile(regex_pattern)
# print(matches.fullmatch(s))
print(str(bool(re.match(regex_pattern, input()))))