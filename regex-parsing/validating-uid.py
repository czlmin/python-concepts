# https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true

# import re
#
# regex_pattern = re.compile("[A-Z]{2,}[0-9]{3,}[a-z]*")

def is_uid_valid(uid):
    if len(uid) != 10:
        print("Invalid")
    elif not uid.isalnum():
        print("Invalid")
    elif len([ch for ch in uid if ch.isupper()]) < 2:
        print("Invalid")
    elif len([ch for ch in uid if ch.isdigit()]) < 3:
        print("Invalid")
    elif len(set(uid)) != len(uid):
        print("Invalid")
    else:
        print("Valid")

N = int(input())
for _ in range(N):
    s = input()
    is_uid_valid(s)

