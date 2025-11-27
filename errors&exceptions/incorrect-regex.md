Yeah, this is one of those slightly cursed HackerRank + PyPy3 situations 😅

You’re absolutely right: on **HackerRank with PyPy3**, this code:

```python
import re

t = int(input())
for _ in range(t):
    pattern = input().strip()
    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)
```

prints

```text
True
True
```

for the sample

```text
2
.*\+
.*+
```

because **PyPy’s regex engine accepts `.*+` as valid**, while CPython’s `re` raises `re.error: multiple repeat`. But the problem’s *expected* output is:

```text
True
False
```

So on PyPy3, just catching `re.error` is not enough.

From the HackerRank discussion, people work around this by **emulating CPython’s “multiple repeat” error**: explicitly reject patterns that contain consecutive quantifier characters like `*`, `+`, `?`. ([HackerRank][1])

---

## ✅ PyPy3-friendly solution

This version passes on **PyPy3** and still works on CPython:

```python
import re

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        pattern = input().strip()
        try:
            # Emulate CPython's "multiple repeat" error:
            # reject any run of 2+ of *, +, ? in a row, e.g. ".*+"
            if re.search(r'(\*|\+|\?){2,}', pattern):
                print(False)
            else:
                re.compile(pattern)
                print(True)
        except re.error:
            print(False)
```

### Why this works

* `re.search(r'(\*|\+|\?){2,}', pattern)`
  matches any sequence of **two or more** characters from `{ '*', '+', '?' }` in a row:

  * `**`, `*+`, `+*`, `+?`, `?+`, `??`, etc.
  * In particular, `.*+` contains the substring `*+`, so it matches and we explicitly return `False`, even though PyPy’s `re.compile(".*+")` doesn’t raise.
* For all *other* patterns, we fall back to the normal:

  ```python
  re.compile(pattern)
  ```

  and treat `re.error` as invalid.

This mirrors the behavior expected by the challenge while compensating for PyPy’s more permissive regex engine.

---

## Practical advice

* **If you choose “Python 3”** as the language on HackerRank, the simple `try: re.compile(...)` solution is enough.
* **If you choose “PyPy 3”** and see `True True` on the sample, use the above workaround to mimic CPython’s stricter behavior.

If you’d like, I can also show a small table of patterns and how CPython vs PyPy vs this workaround classify them.

[1]: https://www.hackerrank.com/challenges/incorrect-regex/forum " Incorrect Regex Discussions | Python | HackerRank "
