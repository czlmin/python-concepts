Here is the clean Python solution for **re.split()** on HackerRank:

---

# ✅ **Solution (passes all test cases)**

```python
import re

if __name__ == "__main__":
    s = input().strip()
    parts = re.split(r"[,.]", s)
    for p in parts:
        print(p)
```

---

# 🧠 Explanation

The problem states:

> Split the string using **comma (',')** and **dot ('.')** as separators.

In regex:

* A character class `[,.]` matches **either** `,` or `.`
* `re.split()` returns a list of substrings obtained by splitting at **every occurrence** of these characters.

Example:

Input:

```
100,200.300
```

Output:

```
100
200
300
```

The loop prints each piece on its own line, as required.

---

This is exactly the behavior HackerRank expects.
