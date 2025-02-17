# Introduction

This section centers on how to get started with python programming language

Software is a set of instructions for the computer to perform a task. Here is a binary program below

10001011011000010001000001001110

## Python interactive shell

We can also enter code and run them in python shell without creating any files.

```py
>>> print("Hello!');
# Hello!
```

```py
print("    *    ")
print("   ***   ")
print("  *****  ")
print("    *    ")
print("    *    ")
print("    *    ")
```

Running a simple Program

```py
print('Hello World!)
```

## What is python

## Where do we need python in computing

## Who is using python

## Python keywords

and asassert break class continue def
del from None elif global nonlocal else
if not except import or False in pass finally
is raise forlambda return try True while with
yield

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not  

How do you get this from the command line?

```py
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
35
```

## Comments

## Capturing user input

## Conceptual Hierarchy

1. Programs are composed of modules.
2. Modules contain statements.
3. Statements contain expressions.
4. Expressions create and process objects.

## Virtual environment

Virtual environment can help us to create an isolated or separate environment. This will help us to avoid conflicts in dependencies across projects. Setting up virtual environments depend on the operating system. Mac/Linux for example can be setup with

```sh
pip3 install virtualenv
```
