# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true

import email.utils, re

N = int(input())

regex_pattern = r"^[a-zA-Z]{1}[a-zA-Z\d\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
for _ in range(N):
    email_address = input()
    email_string = email.utils.parseaddr(email_address)[1]
    match = re.match(regex_pattern, email_string)
    if match:
        print(email_address)