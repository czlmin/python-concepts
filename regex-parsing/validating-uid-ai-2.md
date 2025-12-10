Yes — **it *is* possible** to validate the UID **entirely with regex**, but **NOT with a single regex**, because the problem requires multiple *simultaneous* constraints:

### UID constraints:

1. Exactly **10 characters**
2. Only **alphanumeric**
3. At least **2 uppercase**
4. At least **3 digits**
5. **No repeated characters**

🚫 **Regex cannot enforce “no repeated characters” reliably by itself**
(because that requires backtracking over all positions).
BUT → we *can* use **regex for all other constraints**, and check uniqueness with Python.

So the best pure-regex solution is:

* Use **positive lookaheads** to assert uppercase & digits
* Match the full 10-character alphanumeric pattern
* Use a Python `set()` to enforce uniqueness

---

# ✅ **Regex-based Solution (passes HackerRank)**

```python
import re

pattern = re.compile(
    r'(?=(?:.*[A-Z]){2,})'   # must contain at least 2 uppercase letters
    r'(?=(?:.*\d){3,})'      # must contain at least 3 digits
    r'[A-Za-z0-9]{10}$'      # must be 10 alphanumeric characters
)

def is_valid(uid):
    if not pattern.match(uid):
        return False
    # Check no repeating characters
    return len(set(uid)) == len(uid)

if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        uid = input().strip()
        print("Valid" if is_valid(uid) else "Invalid")
```

---

# 🧠 **Explanation of the Regex**

### 1️⃣ `(?=(?:.*[A-Z]){2,})`

Positive lookahead ensuring at least **2 uppercase letters**

> Look ahead and confirm that the string contains a pattern matching
> `… uppercase … uppercase …`

---

### 2️⃣ `(?=(?:.*\d){3,})`

Positive lookahead ensuring at least **3 digits**

> Look ahead and confirm that the string contains 3 or more digits.

---

### 3️⃣ `[A-Za-z0-9]{10}$`

After passing the lookaheads, the entire string must be:

* Exactly 10 characters
* Only alphanumeric

---

### 4️⃣ Python uniqueness check

```python
len(set(uid)) == len(uid)
```

Ensures **no repeated characters**, something regex cannot do concisely or efficiently.

---

# ✔️ Example

Input:

```
B1CD102354
```

Output:

```
Invalid
```

Fails because:

* Character `1` repeats.

---

# ⭐ Can we do *everything* in pure regex?

### Technically possible with:

* Recursive patterns
* Backreferences
* Negative lookaheads for every character

**BUT Python’s `re` engine does not support the required features**
(such as full negative backtracking for all repeated chars).

So the cleanest, fastest, and most interview-friendly solution is:

> **Use regex for structural constraints, Python set for uniqueness.**

---

If you want, I can also show you a **100% regex solution using the `regex` module** (not `re`), which *can* enforce uniqueness!
