Here’s a clean Python solution for **py-collections-namedtuple** that matches HackerRank’s I/O and uses `namedtuple` correctly:

```python
from collections import namedtuple

if __name__ == "__main__":
    n = int(input().strip())
    fields = input().split()              # e.g. ["ID", "MARKS", "NAME", "CLASS"]
    Student = namedtuple('Student', fields)

    total_marks = 0

    for _ in range(n):
        row = input().split()
        student = Student(*row)
        total_marks += int(student.MARKS)

    print(f"{total_marks / n:.2f}")
```

### How it works

* Reads the number of students `n`.
* Reads the header line (field names) and builds a `Student` namedtuple type from it.
* For each of the next `n` lines:

  * Creates a `Student` instance.
  * Adds `int(student.MARKS)` to `total_marks`.
* Prints the **average MARKS** with **2 decimal places**.
