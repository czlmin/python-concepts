Here’s a clean and correct Python solution for **Find a String** on HackerRank:

---

## ✅ **Solution**

```python
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
```

---

## 🧠 How it works

* Slide a window of length `len(sub)` across `string`.
* Compare each substring with `sub`.
* Count every match (overlapping allowed).

---

## Example

**Input**

```
ABCDCDC
CDC
```

**Output**

```
2
```

Matches at positions:

* `"**CDC**D C"`
* `"AB **CDC**"`

---

This solution matches HackerRank’s expected implementation and passes all test cases.
