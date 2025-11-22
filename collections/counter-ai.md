Here is the clean and correct Python solution for **Collections.Counter** (HackerRank shoe shop problem):

---

# ✅ **Solution Using `Counter` (most Pythonic & fastest)**

```python
from collections import Counter

if __name__ == "__main__":
    _ = int(input())  # number of shoes (unused directly)
    shoes = Counter(map(int, input().split()))
    
    n_customers = int(input())
    earnings = 0
    
    for _ in range(n_customers):
        size, price = map(int, input().split())
        if shoes[size] > 0:        # shoe available
            earnings += price
            shoes[size] -= 1       # reduce stock
    
    print(earnings)
```

---

## 🧠 How it works

* `Counter` stores the number of shoes per size.
* For each customer request:

  * If the requested size is in stock, the shop earns the money and the stock decreases by 1.
  * If not in stock, skip the customer.
* Print total earnings.

---

## ✔️ Example

### Input:

```
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
```

### Output:

```
200
```

---

This version is efficient (O(n)) and passes all HackerRank test cases.

----------------------------------------------------------------------
Great question — this is an important detail about **`Counter` behavior**.

---

# ✅ **What happens if the shoe size is not in `shoes`?**

With a normal dictionary:

```python
normal_dict[size]   # ❌ would raise KeyError if size not present
```

But with **`Counter`**, accessing a missing key:

```python
shoes[size]
```

returns **0 automatically** — *never a KeyError*.

---

# 📌 Why?

`Counter` is a subclass of `dict` but overrides `__missing__` to return **0** for any key not present.

Example:

```python
from collections import Counter
c = Counter({7: 2, 8: 1})

print(c[7])   # 2
print(c[9])   # 0 (NOT KeyError)
```

---

# 🧠 What does this mean in our shoe shop logic?

We check:

```python
if shoes[size] > 0:
    earnings += price
    shoes[size] -= 1
```

If the size doesn’t exist:

* `shoes[size]` is `0`
* Condition fails
* We **correctly ignore the customer**
* No KeyError raised

This is exactly what we want.

---

# ✔️ Example of missing shoe size

### Input:

```
5
2 3 4 5 6
3
1 50
6 70
10 100
```

* Sizes available: `{2,3,4,5,6}`
* Customers ask for: 1, 6, 10

Outcome:

* Size 1 not found → skip
* Size 6 available → earn 70
* Size 10 not found → skip

Total = **70**

The code handles this perfectly because:

```python
shoes[1] == 0
shoes[10] == 0
```

---

# 🎯 Summary

| Feature               | Normal dict | Counter     |
| --------------------- | ----------- | ----------- |
| Missing key access    | ❌ KeyError  | ✅ returns 0 |
| Safe for this problem | No          | **Yes**     |

Your solution using Counter is safe, correct, and optimal.

---

If you want, I can show the exact internal mechanism of `Counter.__missing__`, or rewrite the solution without Counter for comparison.
