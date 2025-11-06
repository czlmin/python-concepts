Here’s a clean Python solution for **Itertools Product** that matches HackerRank’s I/O and output formatting:

```python
from itertools import product

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = product(A, B)
    print(*result)
```

---

### ✅ Explanation

* `product(A, B)` from `itertools` produces the Cartesian product of the two lists.
  Example:

  ```
  A = [1, 2]
  B = [3, 4]
  ```

  → `product(A, B)` = `(1, 3) (1, 4) (2, 3) (2, 4)`
* `print(*result)` unpacks and prints the tuples separated by spaces.

---

### Example Input

```
1 2
3 4
```

### Output

```
(1, 3) (1, 4) (2, 3) (2, 4)
```
