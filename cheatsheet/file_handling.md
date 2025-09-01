Perfect 👌 You want a **comprehensive list of file handling and OS functions in Python** that are widely used, along with **use cases and examples**. Let’s break it down into two main categories:

---

# 📂 1. File Handling Functions (`open`, file object methods)

### 🔹 `open()`

Opens a file and returns a file object.

```python
f = open("data.txt", "r")  # read mode
```

---

### 🔹 `read()`

Reads the entire file (or specified number of characters).

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

---

### 🔹 `readline()`

Reads one line at a time.

```python
with open("data.txt", "r") as f:
    line = f.readline()
    print(line)
```

---

### 🔹 `readlines()`

Reads all lines into a list.

```python
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```

---

### 🔹 `write()`

Writes a string to the file.

```python
with open("data.txt", "w") as f:
    f.write("Hello, World!\n")
```

---

### 🔹 `writelines()`

Writes a list of strings to the file.

```python
with open("data.txt", "w") as f:
    f.writelines(["Line 1\n", "Line 2\n"])
```

---

### 🔹 `seek(offset, whence)`

Moves the file pointer to a specific position.

```python
with open("data.txt", "r") as f:
    f.seek(5)  # move to 5th character
    print(f.read())
```

---

### 🔹 `tell()`

Returns the current position of the file pointer.

```python
with open("data.txt", "r") as f:
    f.read(5)
    print(f.tell())  # shows 5
```

---

### 🔹 `close()`

Closes the file (though `with` handles this automatically).

```python
f = open("data.txt", "r")
f.close()
```

---

# 🗂 2. OS Module Functions (`os`, `os.path`)

The `os` module helps interact with the file system and operating system.

---

### 🔹 `os.getcwd()`

Get the current working directory.

```python
import os
print(os.getcwd())
```

---

### 🔹 `os.chdir(path)`

Change the current working directory.

```python
os.chdir("/tmp")
print(os.getcwd())
```

---

### 🔹 `os.listdir(path)`

List files and directories in a path.

```python
print(os.listdir("."))  # list in current dir
```

---

### 🔹 `os.mkdir(path)`

Create a new directory.

```python
os.mkdir("new_folder")
```

---

### 🔹 `os.makedirs(path)`

Create a directory and intermediate directories.

```python
os.makedirs("parent/child/grandchild")
```

---

### 🔹 `os.rmdir(path)`

Remove an empty directory.

```python
os.rmdir("new_folder")
```

---

### 🔹 `os.remove(path)`

Delete a file.

```python
os.remove("data.txt")
```

---

### 🔹 `os.rename(src, dst)`

Rename a file or directory.

```python
os.rename("old.txt", "new.txt")
```

---

### 🔹 `os.stat(path)`

Get file/directory metadata (size, modification time, etc.).

```python
info = os.stat("data.txt")
print(info.st_size)  # file size in bytes
```

---

### 🔹 `os.path.abspath(path)`

Get the absolute path.

```python
print(os.path.abspath("data.txt"))
```

---

### 🔹 `os.path.basename(path)`

Get the file name from a path.

```python
print(os.path.basename("/home/user/file.txt"))  # file.txt
```

---

### 🔹 `os.path.dirname(path)`

Get the directory name from a path.

```python
print(os.path.dirname("/home/user/file.txt"))  # /home/user
```

---

### 🔹 `os.path.exists(path)`

Check if a file or directory exists.

```python
print(os.path.exists("data.txt"))
```

---

### 🔹 `os.path.isfile(path)`

Check if path is a file.

```python
print(os.path.isfile("data.txt"))
```

---

### 🔹 `os.path.isdir(path)`

Check if path is a directory.

```python
print(os.path.isdir("my_folder"))
```

---

### 🔹 `os.path.join(path, *paths)`

Join paths in an OS-independent way.

```python
path = os.path.join("folder", "file.txt")
print(path)  # folder/file.txt (Linux)
```

---

### 🔹 `os.path.getsize(path)`

Get file size in bytes.

```python
print(os.path.getsize("data.txt"))
```

---

### 🔹 `os.path.splitext(path)`

Split file name and extension.

```python
print(os.path.splitext("data.txt"))  # ('data', '.txt')
```

---

# 📌 Bonus (Modern Alternative)

Python’s `pathlib` (introduced in 3.4) is a cleaner alternative for file system paths:

```python
from pathlib import Path

file = Path("data.txt")
print(file.exists())      # check existence
print(file.is_file())     # check file
print(file.suffix)        # .txt
print(file.read_text())   # read content
```