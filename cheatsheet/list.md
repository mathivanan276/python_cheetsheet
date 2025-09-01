Perfect 👍 Let’s do a **complete catalog of Python list functions & methods**.
There are two categories:

1. **List Methods** → Called on list objects (`list.method()`)
2. **Built-in Functions** → Work with lists but are not methods

---

# 📌 1. List Methods (11 total)

| **Method**                      | **Description / Use Case**                            | **Example**                                |
| ------------------------------- | ----------------------------------------------------- | ------------------------------------------ |
| `append(x)`                     | Add a single element at the end                       | `[1,2].append(3) → [1,2,3]`                |
| `extend(iterable)`              | Add multiple elements from another iterable           | `[1,2].extend([3,4]) → [1,2,3,4]`          |
| `insert(i, x)`                  | Insert element `x` at index `i`                       | `[1,3].insert(1,2) → [1,2,3]`              |
| `remove(x)`                     | Remove first occurrence of value `x`                  | `[1,2,3,2].remove(2) → [1,3,2]`            |
| `pop([i])`                      | Remove and return element at index `i` (default last) | `[1,2,3].pop() → 3` (list becomes `[1,2]`) |
| `clear()`                       | Remove all elements                                   | `[1,2,3].clear() → []`                     |
| `index(x, [start, end])`        | Return index of first occurrence of `x`               | `[1,2,3,2].index(2) → 1`                   |
| `count(x)`                      | Count occurrences of `x`                              | `[1,2,2,3].count(2) → 2`                   |
| `sort(key=None, reverse=False)` | Sort list in place                                    | `[3,1,2].sort() → [1,2,3]`                 |
| `reverse()`                     | Reverse list in place                                 | `[1,2,3].reverse() → [3,2,1]`              |
| `copy()`                        | Shallow copy of list                                  | `a=[1,2]; b=a.copy()`                      |

---

# 📌 2. Built-in Functions for Lists

| **Function**                  | **Use Case**                                      | **Example**                                                   |
| ----------------------------- | ------------------------------------------------- | ------------------------------------------------------------- |
| `len(list)`                   | Number of elements                                | `len([1,2,3]) → 3`                                            |
| `max(list)`                   | Largest element                                   | `max([1,2,3]) → 3`                                            |
| `min(list)`                   | Smallest element                                  | `min([1,2,3]) → 1`                                            |
| `sum(list)`                   | Sum of elements                                   | `sum([1,2,3]) → 6`                                            |
| `sorted(list, reverse=False)` | Return new sorted list (does not modify original) | `sorted([3,1,2]) → [1,2,3]`                                   |
| `reversed(list)`              | Return iterator reversed                          | `list(reversed([1,2,3])) → [3,2,1]`                           |
| `enumerate(list)`             | Iterate with index & value                        | `[(i,x) for i,x in enumerate(['a','b'])] → [(0,'a'),(1,'b')]` |
| `zip(list1, list2, …)`        | Pair elements from multiple lists                 | `list(zip([1,2],[‘a’,‘b’])) → [(1,'a'),(2,'b')]`              |
| `map(func, list)`             | Apply function to each element                    | `list(map(str,[1,2,3])) → ['1','2','3']`                      |
| `filter(func, list)`          | Filter elements based on condition                | `list(filter(lambda x:x%2==0,[1,2,3,4])) → [2,4]`             |
| `any(list)`                   | True if any element is truthy                     | `any([0,0,1]) → True`                                         |
| `all(list)`                   | True if all elements are truthy                   | `all([1,2,3]) → True`                                         |
| `list(iterable)`              | Create a list from iterable                       | `list("abc") → ['a','b','c']`                                 |
| `del list[i]`                 | Delete element at index                           | `a=[1,2,3]; del a[1] → [1,3]`                                 |

---
