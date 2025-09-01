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


Perfect 👍 You asked for a deeper dive into **`pathlib`** — let’s break it down in detail.

---

# 📂 What is `pathlib`?

* `pathlib` is a modern, object-oriented library for **file system paths** in Python (introduced in Python 3.4).
* It’s part of the standard library (`pathlib.Path`) and is designed to **replace `os` and `os.path`** functions with a cleaner, more intuitive API.
* Works consistently across **Windows, Linux, and macOS**, handling path separators automatically.

---

# 🛠️ Key Features of `pathlib`

### 🔹 Creating Path Objects

```python
from pathlib import Path

# Current directory
p = Path(".")

# Absolute path
print(p.resolve())
```

---

### 🔹 Checking File/Directory Properties

```python
file = Path("example.txt")
print(file.exists())   # True if file exists
print(file.is_file())  # True if it's a file
print(file.is_dir())   # True if it's a directory
```

---

### 🔹 Reading & Writing Files

```python
file = Path("data.txt")

# Write text
file.write_text("Hello, Pathlib!")

# Read text
print(file.read_text())

# Write bytes
file.write_bytes(b"binary data")

# Read bytes
print(file.read_bytes())
```

---

### 🔹 Iterating Over Directories

```python
folder = Path(".")

# List all files/folders
for item in folder.iterdir():
    print(item)

# List only Python files
for py_file in folder.glob("*.py"):
    print(py_file)

# Recursive search
for txt_file in folder.rglob("*.txt"):
    print(txt_file)
```

---

### 🔹 Path Operations (Joining, Parents, Parts)

```python
file = Path("/home/user/docs/file.txt")

print(file.name)       # file.txt
print(file.stem)       # file
print(file.suffix)     # .txt
print(file.parent)     # /home/user/docs
print(file.parents[1]) # /home/user

# Joining paths
new_path = file.parent / "new_file.txt"
print(new_path)
```

---

### 🔹 File System Operations

```python
# Create a directory
Path("new_folder").mkdir(exist_ok=True)

# Remove a file
Path("old.txt").unlink(missing_ok=True)

# Rename or move
Path("data.txt").rename("archive/data_old.txt")
```

---

### 🔹 Metadata

```python
file = Path("data.txt")

print(file.stat().st_size)   # size in bytes
print(file.stat().st_mtime)  # last modified time
```

---

# 📌 Why Use `pathlib` Instead of `os`?

| Task                 | Using `os` / `os.path`               | Using `pathlib`                |
| -------------------- | ------------------------------------ | ------------------------------ |
| Join paths           | `os.path.join("folder", "file.txt")` | `Path("folder") / "file.txt"`  |
| Check if file exists | `os.path.exists("file.txt")`         | `Path("file.txt").exists()`    |
| Get file extension   | `os.path.splitext("file.txt")[1]`    | `Path("file.txt").suffix`      |
| Read file            | `open("file.txt").read()`            | `Path("file.txt").read_text()` |

👉 As you see, `pathlib` is **shorter, cleaner, and more Pythonic**.

---

# 📂 Example Project: Copy All `.txt` Files

```python
from pathlib import Path
import shutil

src = Path("source_folder")
dst = Path("backup_folder")
dst.mkdir(exist_ok=True)

for file in src.glob("*.txt"):
    shutil.copy(file, dst / file.name)
    print(f"Copied {file} -> {dst/file.name}")
```

---

✅ **Summary**:

* Use `pathlib` instead of `os.path` for **modern, clean, and cross-platform path handling**.
* It supports everything: creating, reading, writing, traversing, searching, and metadata handling.

---

Perfect 👍 Let’s build a **side-by-side cheat sheet** comparing the traditional **`os` / `os.path`** way with the modern **`pathlib`** way.

---

# 📝 Python File Handling & Paths Cheat Sheet

| **Task**                          | **os / os.path**                        | **pathlib (Recommended)**                                            |
| --------------------------------- | --------------------------------------- | -------------------------------------------------------------------- |
| **Get current working directory** | `import os`<br>`os.getcwd()`            | `from pathlib import Path`<br>`Path.cwd()`                           |
| **Change directory**              | `os.chdir("/tmp")`                      | `Path("/tmp").chdir()` ❌ (not built-in)<br>➡️ Still use `os.chdir()` |
| **Join paths**                    | `os.path.join("folder", "file.txt")`    | `Path("folder") / "file.txt"`                                        |
| **Get absolute path**             | `os.path.abspath("file.txt")`           | `Path("file.txt").resolve()`                                         |
| **Check if path exists**          | `os.path.exists("file.txt")`            | `Path("file.txt").exists()`                                          |
| **Check if file**                 | `os.path.isfile("file.txt")`            | `Path("file.txt").is_file()`                                         |
| **Check if directory**            | `os.path.isdir("folder")`               | `Path("folder").is_dir()`                                            |
| **Get file name**                 | `os.path.basename("/home/u/file.txt")`  | `Path("/home/u/file.txt").name`                                      |
| **Get directory name**            | `os.path.dirname("/home/u/file.txt")`   | `Path("/home/u/file.txt").parent`                                    |
| **Get file extension**            | `os.path.splitext("file.txt")[1]`       | `Path("file.txt").suffix`                                            |
| **Split name & extension**        | `os.path.splitext("file.txt")`          | `(Path("file.txt").stem, Path("file.txt").suffix)`                   |
| **File size**                     | `os.path.getsize("file.txt")`           | `Path("file.txt").stat().st_size`                                    |
| **List directory**                | `os.listdir(".")`                       | `list(Path(".").iterdir())`                                          |
| **Recursive glob**                | `glob.glob("**/*.txt", recursive=True)` | `Path(".").rglob("*.txt")`                                           |
| **Open file for reading**         | `with open("f.txt") as f:`              | `Path("f.txt").open("r")`                                            |
| **Read all text**                 | `open("f.txt").read()`                  | `Path("f.txt").read_text()`                                          |
| **Write text**                    | `open("f.txt","w").write("hi")`         | `Path("f.txt").write_text("hi")`                                     |
| **Read bytes**                    | `open("f.txt","rb").read()`             | `Path("f.txt").read_bytes()`                                         |
| **Write bytes**                   | `open("f.txt","wb").write(b"hi")`       | `Path("f.txt").write_bytes(b"hi")`                                   |
| **Make directory**                | `os.mkdir("folder")`                    | `Path("folder").mkdir()`                                             |
| **Make nested dirs**              | `os.makedirs("a/b/c")`                  | `Path("a/b/c").mkdir(parents=True)`                                  |
| **Remove empty directory**        | `os.rmdir("folder")`                    | `Path("folder").rmdir()`                                             |
| **Delete file**                   | `os.remove("file.txt")`                 | `Path("file.txt").unlink()`                                          |
| **Rename/Move file**              | `os.rename("old.txt","new.txt")`        | `Path("old.txt").rename("new.txt")`                                  |
| **Check file permissions**        | `os.access("file.txt", os.R_OK)`        | `Path("file.txt").stat().st_mode`                                    |

---

# 🚀 Key Takeaways

* `pathlib` is **cleaner** and **object-oriented**.
* Common file operations (`read`, `write`, `exists`, `glob`) are **one-liners** with `pathlib`.
* Some functions (`chdir`, permissions) are still only in `os`.
* For new projects: **prefer `pathlib`**, fall back to `os` when needed.

---