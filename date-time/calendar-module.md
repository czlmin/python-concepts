Here is the clean Python solution for **Calendar Module** on HackerRank:

---

## ✅ **Solution**

```python
import calendar

if __name__ == "__main__":
    month, day, year = map(int, input().split())
    weekday = calendar.weekday(year, month, day)
    print(calendar.day_name[weekday].upper())
```

---

## 🧠 Explanation

* `calendar.weekday(year, month, day)` returns an integer:

  ```
  0 = Monday
  1 = Tuesday
  2 = Wednesday
  3 = Thursday
  4 = Friday
  5 = Saturday
  6 = Sunday
  ```
* `calendar.day_name` maps these integers to the correct weekday names.
* `.upper()` converts the result to uppercase, which HackerRank requires.

---

## ✔️ Example

**Input**

```
08 05 2015
```

**Output**

```
WEDNESDAY
```

---

This solution passes all HackerRank test cases.
