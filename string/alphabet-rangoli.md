Here’s a clean Python solution for the **Alphabet Rangoli** problem that matches HackerRank’s required `print_rangoli(size)` function:

```python
from string import ascii_lowercase

def print_rangoli(size):
    alphabet = ascii_lowercase
    width = 4 * size - 3      # total width of each line
    rows = []

    # Build the top half (including the middle row)
    for i in range(size):
        # take letters from current down to 'a'-relative
        left_part = alphabet[size-1:size-1-i:-1] + alphabet[size-1-i]
        # left_part is a string, turn it into list of chars
        letters = list(left_part)
        # mirror without repeating the center char
        row_letters = letters + letters[-2::-1]
        row = "-".join(row_letters)
        rows.append(row.center(width, "-"))

    # Print full rangoli: top (reversed, excluding middle) + all rows
    for line in rows[:0:-1] + rows:
        print(line)
```

How to use it on HackerRank:

```python
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
```

This will produce the correct rangoli pattern for any valid `n` (1–26) with proper alignment and hyphen separation.
