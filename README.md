### Table of content

* [Introduction](#introduction)
* [Variables](#variables)
* [Data Types](#datatypes)

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

## Variables

<p> Variables do not need to be declared with any particular type, and can even change type after they have been set. If you want to specify the data type of a variable, this can be done with casting.</p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> a = 2
>>> A = "python"
>>> c = str(2)
>>> print(a,type(a),c,type(c))
2 <class 'int'> 2 <class 'str'>
>>> print(a+c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(a+c)
          ~^~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> c = 2
>>> print(a+c)
4
>>> exit()
>
```
🔹Rules for Python variables:

* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
* Variable names are case-sensitive (age, Age and AGE are three different variables)
* A variable name cannot be any of the Python keywords.

<details><summary>Example</summary>

<br>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> 2var = 'python'
  File "<stdin>", line 1
    2var = 'python'
    ^
SyntaxError: invalid decimal literal
>>> var-1 = 'python'
  File "<stdin>", line 1
    var-1 = 'python'
    ^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> var 2 = 'python'
  File "<stdin>", line 1
    var 2 = 'python'
        ^
SyntaxError: invalid syntax
>>> var = 1
>>> Var = 2
>>> VAR = 3
>>> print(var,Var,VAR)
1 2 3
>>> exit()
>
```

</details>

🔹Unpack a Collection

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> a,b,c = 1,2,3
>>> print(a,b,c)
1 2 3
>>> pokemon = ["pikachu","blastoise","darkrai"]
>>> x,y,z = pokemon
>>> print(x,y,z)
pikachu blastoise darkrai
>>> exit()
>
```

🔹Global Variables

<p> Variables that are created outside of a function are known as global variables. Global variables can be used by everyone, both inside of functions and outside. </p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> a = 2
>>> def fun():
...     print(a)
...
>>> fun()
2
>>> exit()
>
```

<p> If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value. </p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> a = 2
>>> def fun():
...     a = 4
...     print(a+2)
... 
>>> fun()
6
>>> print(a+2)
4
>>> exit()
>
```

<p> Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To create a global variable inside a function, you can use the global keyword. </p>

<p> Also, use the global keyword if you want to change a global variable inside a function. </p>

```python
> python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> a = 1
>>> def fun():
...     global a
...     global b
...     a = 2
...     b = 2
...     print(a+b)
... 
>>> fun()
4
>>> print(a+b)
4
>>> exit()
> 
```

[🔝 Go to top](#table-of-content)
[🔝 Up](#variables)


## Code Challenge - Level 1

[Level 1](https://github.com/Sahill17/python/blob/main/Code%20Challenges/ReadMe/level1.md) - [Solution](https://github.com/Sahill17/python/blob/main/Code%20Challenges/Solution/level1)

## Data Types

<p> Python has the following data types built-in by default: </p>

| Category | Data Type | Example |
| -------- | --------- | ------- |
| Numeric Type | <b>int, float, complex</b> | 20, 20.5, 1j |
| Text Type | <b>str</b> | "Hello" |
| Sequence Type | <b>list, tuple, range</b> | [1,2,3], (1,2,3), range(3) |
| Mapping Type | <b>dict</b> | {"name" : "Sahil", "age" : 22}
| Set Types | <b>set, fronzenset</b> | {"a","b","c"}, fronzenset({"a","b","c"}) |
| Boolean Type | <b>bool</b> | True |
| Binary Type | <b>bytes, bytearray, memoryview</b> | b"Hello", bytearray(5), memoryview(bytes(5)) |
| None Type | <b>NoneType</b> | None |



🔹 Numeric Data Types

- <b>Int</b>
  - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
  ```python
  > python
  Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  Ctrl click to launch VS Code Native REPL
  >>> x = 162735
  >>> y = -178273
  >>> print(x,type(x),y,type(y))
  162735 <class 'int'> -178273 <class 'int'>
  >>> exit()
  ```

- <b>Float</b>
  - Float, or "floating point number" is a number, positive or negative, containing one or more decimals. Float can also be scientific numbers with an "e" to indicate the power of 10.
  ```python
  > python
  Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  Ctrl click to launch VS Code Native REPL
  >>> x = 1363.124
  >>> y = -12432.12
  >>> z = -73.3e100
  >>> print(type(x),x,type(y),y,type(z),z)
  <class 'float'> 1363.124 <class 'float'> -12432.12 <class 'float'> -7.33e+101
  >>> exit()
  ```

- <b>Complex</b>
  - Complex numbers are written with a "j" as the imaginary part.
  ```python
  > python
  Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  Ctrl click to launch VS Code Native REPL
  >>> x = 2+4j
  >>> y = -5j
  >>> print(x,type(x),y,type(y)) 
  (2+4j) <class 'complex'> (-0-5j) <class 'complex'>
  >>> exit()
  ```
