N = int(input())
nums = list(map(int, input().split()))

all_positive = all(num > 0 for num in nums)
any_palindrome = any(str(num) == str(num)[::-1] for num in nums)

print(all_positive and any_palindrome)
