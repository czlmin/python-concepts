Here are two accepted solutions for **The Captain’s Room**.

## 🚀 Fastest (math trick)

Uses the fact that every family room appears exactly **K times** but the captain’s appears **once**:
[
\text{captain}=\frac{K \cdot \sum(\text{unique rooms})-\sum(\text{all rooms})}{K-1}
]

```python
# Fastest solution
if __name__ == "__main__":
    K = int(input().strip())
    rooms = list(map(int, input().split()))
    unique_sum = sum(set(rooms))
    total_sum = sum(rooms)
    captain = (K * unique_sum - total_sum) // (K - 1)
    print(captain)
```

* Time: O(n)
* Space: O(u) for the set of unique rooms

## ✅ Pure set-logic (track seen vs duplicates)

Keep two sets: `seen` and `dupes`. The captain’s room is the one in `seen - dupes`.

```python
# Set-based solution
if __name__ == "__main__":
    K = int(input().strip())
    rooms = list(map(int, input().split()))
    seen, dupes = set(), set()
    for r in rooms:
        if r in seen:
            dupes.add(r)
        else:
            seen.add(r)
    print((seen - dupes).pop())
```

* Time: O(n)
* Space: O(u)

Pick the first for speed/simplicity; the second is a clear set-only approach without arithmetic.
