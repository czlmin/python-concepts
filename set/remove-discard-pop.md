Here’s a clean solution that handles all three operations (`pop`, `remove`, `discard`) safely and prints the final sum:

```python
# HackerRank: py-set-discard-remove-pop

if __name__ == "__main__":
    _ = int(input().strip())                       # initial size (unused directly)
    s = set(map(int, input().split()))
    n = int(input().strip())

    for _ in range(n):
        parts = input().split()
        cmd = parts[0]
        if cmd == "pop":
            if s:                                  # avoid KeyError if set is empty
                s.pop()
        elif cmd == "remove":
            try:
                s.remove(int(parts[1]))           # KeyError if not present → ignore
            except KeyError:
                pass
        elif cmd == "discard":
            s.discard(int(parts[1]))              # no error if not present

    print(sum(s))
```

* `remove(x)` raises `KeyError` if `x` isn’t in the set → caught and ignored.
* `discard(x)` doesn’t raise if `x` is missing.
* `pop()` is guarded to avoid popping from an empty set.
