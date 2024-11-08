# Functions

Function is a block of code that groups a set of statements so they can be executed more than once in the computer. They help in code reuse that makes the program code more readable and useful.

Functions can be created using `def` or `lambda` keywords. Scope visibility could be `global` or `nonlocal`. They can send back results to the caller by `return` or `yield` keywords.

```py
# function definition
def times(x, y):
    return x * y 

# function call
times(2, 3)
```

```py
# saving result to another object
c = times(3, 4)
print(c)
```

## Polymorphism

Here the functions does different things depending on the supplied arguments. The times function does multiplication in one and repetition in another. Polymorphism is also called `duck typing` as compared to how a duck quacks

- [Introduction](intro.md)
- [Function Scopes](00_intro.md)
- [Recursive Functions](00_intro.md)
- [Lambda Functions](00_intro.md)
- [Generator Functions](00_intro.md)