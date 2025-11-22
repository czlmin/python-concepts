Here is the clean and correct Python solution for **DefaultDict Tutorial** on HackerRank:

---

## ✅ **Python Solution Using `defaultdict(list)`**

```python
from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    groups = defaultdict(list)
    
    # Read Group A words and store their positions
    for i in range(1, n + 1):
        word = input().strip()
        groups[word].append(i)
    
    # For each Group B word, print indices or -1
    for _ in range(m):
        word = input().strip()
        if groups[word]:
            print(*groups[word])
        else:
            print(-1)
```

---

## 🧠 How it works

* Use `defaultdict(list)` so each key maps to a list of indices.
* For the **n** words of group A:

  * Append index `i` (1-based) into the list for that word.
* For each of the **m** words of group B:

  * If it exists in the dictionary → print all stored positions.
  * Otherwise → print `-1`.

---

## ✔️ Example

### Input:

```
5 2
a
a
b
a
b
a
b
```

### Output:

```
1 2 4
3 5
```

---

## 💡 Notes

* `print(*groups[word])` expands the stored list into space-separated values.
* Order is preserved because we always append positions in increasing order.
* This approach runs efficiently in **O(n + m)**.

---

If you want, I can also provide a version using **dict of lists manually** (without defaultdict) to show the difference.
