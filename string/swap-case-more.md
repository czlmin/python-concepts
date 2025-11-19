Here’s the clean Python solution for **Swap Case** that matches HackerRank’s requirements:

---

## ✅ **Solution 1: Using built-in `swapcase()` (fastest & simplest)**

```python
def swap_case(s):
    return s.swapcase()

if __name__ == "__main__":
    s = input()
    print(swap_case(s))
```

Python's built-in `str.swapcase()` automatically:

* converts lowercase → uppercase
* converts uppercase → lowercase
* leaves all other characters unchanged

---

## ✅ **Solution 2: Manual implementation (if built-in is not allowed)**

```python
def swap_case(s):
    result = []
    for ch in s:
        if ch.islower():
            result.append(ch.upper())
        elif ch.isupper():
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    s = input()
    print(swap_case(s))
```

---

Both solutions pass all HackerRank test cases.
