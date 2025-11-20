Here is the correct Python solution for **Python String Formatting**, matching HackerRank’s expected output exactly:

---

## ✅ **Solution**

```python
def print_formatted(number):
    width = len(bin(number)) - 2    # width of the largest binary number

    for i in range(1, number + 1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        print(deci.rjust(width),
              octa.rjust(width),
              hexa.rjust(width),
              bina.rjust(width))
            

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
```

---

## 🧠 Why this works

* The problem wants numbers from **1 to n** printed in **aligned columns**, with:

  | Type        | Example          |
  | ----------- | ---------------- |
  | Decimal     | `17`             |
  | Octal       | `21`             |
  | Hexadecimal | `11` (uppercase) |
  | Binary      | `10001`          |

* The **right width** for alignment is determined by the length of the **binary representation of `n`**, without the `'0b'` prefix:

  ```python
  width = len(bin(n)) - 2
  ```

* Each value is right-justified using `.rjust(width)`.

---

## ✔️ Example

**Input**

```
17
```

**Output**

```
    1     1     1     1
    2     2     2    10
    3     3     3    11
...
   17    21    11 10001
```

---

If you'd like, I can also provide a **one-liner variant**, or show a **table-format version** using f-strings.
