Here’s a clean Python solution for the **Designer Door Mat** problem:

```python
# HackerRank: Designer Door Mat

if __name__ == "__main__":
    N, M = map(int, input().split())   # N is rows (odd), M is columns (3*N)

    pattern_char = '.|.'
    fill_char = '-'

    # Top half (excluding middle line)
    for i in range(1, N, 2):
        pattern = pattern_char * i
        print(pattern.center(M, fill_char))

    # Middle line
    print("WELCOME".center(M, fill_char))

    # Bottom half (mirror of top)
    for i in range(N - 2, 0, -2):
        pattern = pattern_char * i
        print(pattern.center(M, fill_char))
```

**How it works:**

* The top half prints lines with `1, 3, 5, ...` occurrences of `".|."`, centered with `'-'`.
* The middle line is `"WELCOME"` centered.
* The bottom half mirrors the top with `... 5, 3, 1` occurrences of `".|."`.
