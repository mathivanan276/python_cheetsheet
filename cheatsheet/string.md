# 🔠 **Python String Functions**

---

## 📝 1. **Case Conversion**

| Function           | Use Case                                     | Example                                   |
| ------------------ | -------------------------------------------- | ----------------------------------------- |
| `str.lower()`      | Convert to lowercase (basic, ASCII-safe)     | `"HELLO".lower()` → `"hello"`             |
| `str.upper()`      | Convert to uppercase                         | `"hello".upper()` → `"HELLO"`             |
| `str.casefold()`   | Aggressive lowercase for Unicode comparisons | `"Straße".casefold()` → `"strasse"`       |
| `str.capitalize()` | Capitalize first letter, rest lowercase      | `"python".capitalize()` → `"Python"`      |
| `str.title()`      | Title case (capitalize each word)            | `"hello world".title()` → `"Hello World"` |
| `str.swapcase()`   | Swap upper ↔ lower                           | `"PyThOn".swapcase()` → `"pYtHoN"`        |

---

## 🧹 2. **Whitespace / Character Stripping**

| Function       | Use Case                                              | Example                           |
| -------------- | ----------------------------------------------------- | --------------------------------- |
| `str.strip()`  | Remove whitespace (or specified chars) from both ends | `"  hello  ".strip()` → `"hello"` |
| `str.lstrip()` | Remove leading whitespace                             | `"  hello".lstrip()` → `"hello"`  |
| `str.rstrip()` | Remove trailing whitespace                            | `"hello  ".rstrip()` → `"hello"`  |

---

## 🔍 3. **Searching**

| Function                 | Use Case                                   | Example                              |
| ------------------------ | ------------------------------------------ | ------------------------------------ |
| `str.find(sub)`          | Find index of substring (−1 if not found)  | `"hello".find("l")` → `2`            |
| `str.rfind(sub)`         | Find last occurrence index                 | `"hello".rfind("l")` → `3`           |
| `str.index(sub)`         | Like `find` but raises error if not found  | `"hello".index("l")` → `2`           |
| `str.rindex(sub)`        | Like `rfind` but raises error if not found | `"hello".rindex("l")` → `3`          |
| `str.startswith(prefix)` | Check if starts with prefix                | `"python".startswith("py")` → `True` |
| `str.endswith(suffix)`   | Check if ends with suffix                  | `"python".endswith("on")` → `True`   |
| `str.count(sub)`         | Count occurrences of substring             | `"banana".count("na")` → `2`         |

---

## ✂ 4. **Splitting & Joining**

| Function                    | Use Case                                | Example                                                               |
| --------------------------- | --------------------------------------- | --------------------------------------------------------------------- |
| `str.split(sep)`            | Split string into list                  | `"a,b,c".split(",")` → `["a","b","c"]`                                |
| `str.rsplit(sep, maxsplit)` | Split from right                        | `"a,b,c".rsplit(",", 1)` → `["a,b", "c"]`                             |
| `str.splitlines()`          | Split by line breaks                    | `"a\nb\nc".splitlines()` → `["a","b","c"]`                            |
| `sep.join(iterable)`        | Join iterable into string               | `",".join(["a","b","c"])` → `"a,b,c"`                                 |
| `str.partition(sep)`        | Split into 3 parts (before, sep, after) | `"hello=world".partition("=")` → `("hello","=","world")`              |
| `str.rpartition(sep)`       | Partition from right                    | `"hello=world=again".rpartition("=")` → `("hello=world","=","again")` |

---

## 🛠 5. **Replacing & Modifying**

| Function                   | Use Case                        | Example                                                      |
| -------------------------- | ------------------------------- | ------------------------------------------------------------ |
| `str.replace(old, new)`    | Replace substring               | `"hello world".replace("world","Python")` → `"hello Python"` |
| `str.removeprefix(prefix)` | Remove prefix if present (3.9+) | `"python3".removeprefix("python")` → `"3"`                   |
| `str.removesuffix(suffix)` | Remove suffix if present (3.9+) | `"script.py".removesuffix(".py")` → `"script"`               |

---

## 🧾 6. **Character Checks**

(All return `True`/`False`)

| Function             | Use Case                                         | Example                            |
| -------------------- | ------------------------------------------------ | ---------------------------------- |
| `str.isalpha()`      | Letters only                                     | `"abc".isalpha()` → `True`         |
| `str.isdigit()`      | Digits only                                      | `"123".isdigit()` → `True`         |
| `str.isdecimal()`    | Decimal digits only                              | `"²".isdecimal()` → `False`        |
| `str.isnumeric()`    | Numbers (includes fractions, superscripts, etc.) | `"²".isnumeric()` → `True`         |
| `str.isalnum()`      | Letters + digits                                 | `"abc123".isalnum()` → `True`      |
| `str.isspace()`      | Whitespace only                                  | `"   ".isspace()` → `True`         |
| `str.islower()`      | All lowercase                                    | `"abc".islower()` → `True`         |
| `str.isupper()`      | All uppercase                                    | `"ABC".isupper()` → `True`         |
| `str.istitle()`      | Title case                                       | `"Hello World".istitle()` → `True` |
| `str.isidentifier()` | Valid Python variable name                       | `"var_1".isidentifier()` → `True`  |
| `str.isprintable()`  | Printable chars only                             | `"abc\n".isprintable()` → `False`  |

---

## 🧩 7. **Alignment & Formatting**

| Function                  | Use Case                  | Example                                                           |
| ------------------------- | ------------------------- | ----------------------------------------------------------------- |
| `str.center(width, fill)` | Center align              | `"hi".center(6,"-")` → `"--hi--"`                                 |
| `str.ljust(width, fill)`  | Left align                | `"hi".ljust(6,"-")` → `"hi----"`                                  |
| `str.rjust(width, fill)`  | Right align               | `"hi".rjust(6,"-")` → `"----hi"`                                  |
| `str.zfill(width)`        | Pad with zeros            | `"42".zfill(5)` → `"00042"`                                       |
| `str.format()`            | Format with placeholders  | `"Hello {}".format("World")` → `"Hello World"`                    |
| `str.format_map(dict)`    | Format using dict mapping | `"Hello {name}".format_map({"name":"Python"})` → `"Hello Python"` |

---

## 🌍 8. **Encoding & Translation**

| Function               | Use Case                 | Example                                                         |
| ---------------------- | ------------------------ | --------------------------------------------------------------- |
| `str.encode(encoding)` | Encode to bytes          | `"hello".encode("utf-8")` → `b'hello'`                          |
| `str.maketrans()`      | Create translation table | `str.maketrans("aeiou","12345")`                                |
| `str.translate(table)` | Apply translation        | `"hello".translate(str.maketrans("aeiou","12345"))` → `"h2ll4"` |

---

## 🧮 9. **Miscellaneous**

| Function    | Use Case                   | Example              |
| ----------- | -------------------------- | -------------------- |
| `len(str)`  | Length of string           | `len("hello")` → `5` |
| `ord(char)` | Get Unicode code point     | `ord("A")` → `65`    |
| `chr(num)`  | Get char from Unicode code | `chr(65)` → `"A"`    |

---

## 🎯 Summary

* **Normalization & Comparison** → `casefold()`, `startswith()`, `endswith()`
* **Cleaning** → `strip()`, `replace()`, `removeprefix()`, `removesuffix()`
* **Searching** → `find()`, `index()`, `count()`
* **Validation** → `isalnum()`, `isalpha()`, `isdigit()`, etc.
* **Splitting & Joining** → `split()`, `join()`, `partition()`
* **Formatting** → `format()`, `center()`, `ljust()`, `rjust()`

---

👉 Do you want me to **prepare a cheat sheet PDF** with all these string methods + quick examples so you can keep it handy for interviews?
