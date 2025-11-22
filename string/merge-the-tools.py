#

def merge_the_tools(string, k):
    # your code goes here
    from collections import Counter
    n = len(string)
    m = n // k
    for i in range(m):
        t = string[i * k:i * k + k]
        freq = Counter(t)
        keys = list(freq.keys())
        u = "".join(keys)
        print(u)


if __name__ == '__main__':
    # string, k = input(), int(input())
    string = "AABCAAADAC"
    k = 2
    merge_the_tools(string, k)