# https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

# # s = "Sorting1234"
# def ginorts(s):
#     sorted_string = sorted(s)
#
#     digits = [item for item in sorted_string if item.isdigit()]
#     strings = [item for item in sorted_string if not item.isdigit()]
#     sorted_upper = [item for item in strings if item.isupper()]
#     sorted_lower = [item for item in strings if item.islower()]
#     sorted_odd = [item for item in digits if int(item)%2 == 1]
#     sorted_even = [item for item in digits if int(item)%2 == 0]
#     sorted_s = sorted_lower + sorted_upper + sorted_odd + sorted_even
#     sorted_s = "".join(sorted_s)
#     return sorted_s
#
# s = str(input().split())
# print(ginorts(s))

def ginorts(s):
    sorted_string = sorted(s)

    sorted_upper = [item for item in sorted_string if item.isupper()]
    sorted_lower = [item for item in sorted_string if item.islower()]
    sorted_odd = [item for item in sorted_string if item.isdigit() and int(item)%2 == 1]
    sorted_even = [item for item in sorted_string if item.isdigit() and int(item)%2 == 0]
    sorted_s = sorted_lower + sorted_upper + sorted_odd + sorted_even
    sorted_s = "".join(sorted_s)
    return sorted_s

s = str(input().split())
print(ginorts(s))


# # HackerRank: ginorts
#
# def sort_key(ch):
#     if ch.islower():
#         return (0, ch)          # 1) lowercase
#     if ch.isupper():
#         return (1, ch)          # 2) uppercase
#     d = int(ch)                 # digits
#     return (2 if d % 2 else 3, ch)  # 3) odd digits, 4) even digits
#
# s = input().strip()
# print(''.join(sorted(s, key=sort_key)))
