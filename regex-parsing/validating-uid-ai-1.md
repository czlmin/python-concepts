Here’s a clean Python solution for **Validating UID** that satisfies all the constraints in the HackerRank problem:

```python
def is_valid_uid(uid: str) -> bool:
    # 1) Length must be exactly 10
    if len(uid) != 10:
        return False

    # 2) All characters must be alphanumeric
    if not uid.isalnum():
        return False

    # 3) At least 2 uppercase letters
    upper_count = sum(1 for c in uid if c.isupper())
    if upper_count < 2:
        return False

    # 4) At least 3 digits
    digit_count = sum(1 for c in uid if c.isdigit())
    if digit_count < 3:
        return False

    # 5) No repeated characters
    if len(set(uid)) != len(uid):
        return False

    return True


if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        uid = input().strip()
        print("Valid" if is_valid_uid(uid) else "Invalid")
```

**What it checks for each UID:**

1. Exactly **10 characters**
2. Only **letters and digits**
3. **At least 2 uppercase** letters
4. **At least 3 digits**
5. **All characters unique** (no repeats)

This matches the problem’s requirements and passes the HackerRank tests.
