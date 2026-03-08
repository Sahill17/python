### Table of content

* [Introduction](#introduction)

## Introduction

<p> Python is a very popular general-purpose interpreted, interactive, object-oriented, and high-level programming language. Python is dynamically-typed and garbage-collected programming language. </p>

<p> Python is an interpreted programming language, this means that as a developer you write Python (.py) files in a text editor and then put those files into the python interpreter to be executed. </p>

<p> To test a short amount of code in python sometimes it is quickest and easiest not to write the code in a file. This is made possible because Python can be run as a command line itself. </p>

🔹 Say Hello to the world

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> print("Hello World")
Hello World
>>> exit()
>
```

🔹 Indentation

<p> Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. </p>

<p>Python uses indentation to indicate a block of code. </p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> if 5 > 2:
...     print("YES")
... 
YES
>>> exit()
> 
```

<p> You have to use the same number of spaces in the same block of code, otherwise Python will give you an error. </p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> 
>>> if 5 > 2:
...     print("YES")
...             print("YES YES")
  File "<stdin>", line 3
                print("YES YES")
        ^
IndentationError: unexpected indent
>>> 
>>> exit()
> 
```

🔹 Comments

<p> Comments start with a #, and Python will render the rest of the line as a comment. </p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> # This is comment 
>>> 
>>> This is not a comment 
  File "<stdin>", line 1
    This is not a comment
                  ^^^^^^^
SyntaxError: invalid syntax
>>> exit()
> 
```

🔹 Semicolons

<p> In Python, a statement usually ends when the line ends. You do not need to use a semicolon (;) like in many other programming languages (for example, Java or C). </p>

<p> Semicolons are optional in Python. You can write multiple statements on one line by separating them with ; but this is rarely used because it makes it hard to read. </p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> print("Hello World");
Hello World
>>> print("Hello") print("World")
  File "<stdin>", line 1
    print("Hello") print("World")
                   ^^^^^
SyntaxError: invalid syntax
>>> print("Hello"); print("World")
Hello
World
>>> exit()
>
```

🔹Print Without a New Line

<p> By default, the print() function ends with a new line. If you want to print multiple words on the same line, you can use the end parameter. </p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> print("Hello",end=" "); print("World")
Hello World
>>> print("Hello"); print("World")
Hello
World
>>> exit()
> 
```

<p> You can combine text and numbers along with doing math as well. </p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> print(2+2)
4
>>> print("Hello, I am", 22, "years ", end="old\n") 
Hello, I am 22 years old
>>> exit()
> 
```

[🔝 Go to top](#table-of-content)
[🔝 Up](#introduction)