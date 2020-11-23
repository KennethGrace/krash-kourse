# Control Flow in Python
Control flow refers to the order in which the instructions of our program are executed. In Python we have a few options for controlling this flow. We will begin with a discussion on conditionals in Python. Following conditionals will be a discussion on exceptions.We will finish this section with a discussion on iteration. At the end of this section you will be introduced to a form of iteration called a comprehension which accelerates the generation of collection objects like a list and a dictionary.

The fundamental conditional is the `if` statement. When paired with an `else` clause the `if` statement gains even more power. Let's see it's behavior in action. The behavior should be fairly intuitive, but you may be surprised by somethings the Python `if` statement can do.

```python
condition = True
print(dir(condition))
if condition:
    print("The statement was true.")
else:
    print("The statement was false.")
```

```python
a = 2
b = 5
condition = a > 5
if condition:
    print("Condition is true.")
else:
    print("Condition is false.")
```

