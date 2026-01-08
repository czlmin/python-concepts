
def merge_the_tools(string, k):
    # Split into substrings of length k
    for i in range(0, len(string), k):
        chunk = string[i:i+k]
        seen = set()
        out = []
        # Keep first occurrence of each character (order preserved)
        for ch in chunk:
            if ch not in seen:
                seen.add(ch)
                out.append(ch)
        print(''.join(out))

if __name__ == '__main__':
    string = input().strip()
    k = int(input().strip())
    merge_the_tools(string, k)

