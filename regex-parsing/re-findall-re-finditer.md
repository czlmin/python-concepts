Here is the correct Python solution for **Re.findall() & Re.finditer()** on HackerRank.

The task:

* Given a string **S**, find all **vowel substrings** that are **2 or more characters long**,
* Each substring must be **surrounded by consonants**,
* Print each such substring on a new line,
* If no match exists → print **-1**.

---

# ✅ **Correct Solution**

```python
import re

s = input().strip()

# Pattern:
# (?<=[^aeiouAEIOU])   → preceded by a non-vowel
# ([aeiouAEIOU]{2,})   → capture 2+ vowels
# (?=[^aeiouAEIOU])    → followed by a non-vowel
pattern = r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])'

matches = re.findall(pattern, s)

if matches:
    for m in matches:
        print(m)
else:
    print(-1)
```

---

# 🧠 Explanation

### Regex breakdown:

```
(?<=[^aeiouAEIOU])
```

Positive lookbehind → ensures the vowel substring is *preceded* by a consonant.

```
([aeiouAEIOU]{2,})
```

Capture group → matches a sequence of **2 or more vowels**.

```
(?=[^aeiouAEIOU])
```

Positive lookahead → ensures the vowel substring is *followed* by a consonant.

Together, this extracts only valid vowel substrings surrounded by consonants.

---

# ✔️ Example

### Input:

```
rabcdeefgyYhFjkIoomnpOeorteeeeet
```

### Output:

```
ee
Ioo
Oeo
eeeee
```

---

# 🎯 Notes

* Works with uppercase and lowercase vowels.
* Does not match vowels at the beginning or end of the string (because they are not surrounded by consonants).
* Avoids matching overlapping sequences incorrectly (handled by regex engine).

---

If you'd like, I can show an expanded visualization of how the regex matches step-by-step.
