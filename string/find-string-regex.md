Here’s a **regex-based solution** that correctly counts **overlapping** occurrences for HackerRank **Find a String**.

## ✅ Regex solution (overlaps included)

```python
import re

def count_substring(string, sub_string):
    # (?=...) is a positive lookahead that allows overlapping matches
    pattern = rf'(?={re.escape(sub_string)})'
    return len(re.findall(pattern, string))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    print(count_substring(string, sub_string))
```

### Why this works

* `(?=...)` is a **positive lookahead**: it checks that `sub_string` starts at the current position **without consuming characters**, so the next match can start one character later (overlap).
* `re.escape(sub_string)` ensures special characters in the substring (like `.` or `*`) are treated literally.

### Quick example

* `string = "AAAA"`, `sub_string = "AA"`
* Matches start at indices `0, 1, 2` → output `3` ✅
