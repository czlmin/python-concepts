
def count_substring(string, sub):
    count = 0
    n, m = len(string), len(sub)
    for i in range(n - m + 1):
        if string[i:i+m] == sub:
            count += 1
    return count

if __name__ == "__main__":
    string = input().strip()
    sub = input().strip()
    print(count_substring(string, sub))
