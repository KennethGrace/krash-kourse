# Objects in Python
The first thing to recognize in Python is that everything exists as an object, even methods exist as objects! The prevalence and importance of Objects in Python is one reason I've chosen to start this course with a detailed discussion of Objects. Before we get ahead of ourselves though, let us begin with the two simplest useful object types numbers and strings.

All Objects have some properties and methods. At a high level, we could say the methods of a number are the mathematical operations we can perform on it. The numeric value could be described as a property of the number object. Let's see this process in action before further examination.

[*number-and-strings.py*](/krash-kourse/objects/numbers-and-strings.py) - Figure 1.1
```python
a = 1
b = 2
c = a + b
print(c)
```
```commandline
3
```
This seems simple enough for numbers, but this same methodology can be extended to all types of objects. For another simple example, let's imagine how a string object handles the addition method. A string can be declared with either double quotes, `""`, or single quotes, `''`, and represents an ordered set of letters. As such a string has no direct numeric value, so it may be confusing at first how a numeric operator like addition can even apply to a string.

[*number-and-strings.py*](/krash-kourse/objects/numbers-and-strings.py) - Figure 1.2
```python
message_one = 'Krash'
message_two = "Kourse"
full_message = message_one + message_two
print(full_message)
```
```commandline
KrashKourse
```
You may have expected this result. It seems intuitive that strings when added would be concatenated, but how does Python know to perform a concatenation instead of trying to perform numeric addition as we saw earlier? Let's see what's going on "under the hood" here. The `dir()` function provides us with a means to crack open the juicy secrets of our objects. For starters, we'll look inside our integer `a` and our string `message_one`.

[*number-and-strings.py*](/krash-kourse/objects/numbers-and-strings.py) - Figure 1.3
```python
print(dir(a))
print(dir(message_one))
print(a.__add__)
print(message_one.__add__)
```
```commandline
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
<method-wrapper '__add__' of int object at 0x8a48e0>
<method-wrapper '__add__' of str object at 0x7f476dccc1b8>
```
We can see here that both objects have unique instances of a method called `__add__`. The definition of `__add__` is unique to each object and so their functionality is entirely independent. This `__add__` method is invoked whenever python encounters the `+` operator. Similarly, the `__repr__` method is invoked whenever python encounters the `print()` function.

Now that we've seen the basic nature and methodology of Python Objects. Let's see some of the other important Objects Python provides us to play with out of the box. I won't be covering the detailed functioning of these Objects as this is already well documented [here](https://docs.python.org/3/). From here on, I will only be introducing the basic function and use case of Objects.

[*lists-and-dicts.py*](/krash-kourse/objects/lists-and-dicts.py) - Figure 2.1
```python
a = []
print(dir(a))
print(a.append)
a.append('Krash Kourse Rules')
print(a)
```
```commandline
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
<built-in method append of list object at 0x7f4b3cb490c8>
['Krash Kourse Rules']
```
Here we see an example of a list object. I will leave the functioning of a list's `__add__` method as an exercise for the reader. A list is a type of "collection" in Python which permits us to store an ordered set of Objects. We will not be discussing what a collection is or ideas like inheritance here. What is important to note is a list may contain different types of objects including other lists! Lists are created and accessed using the `[]` operator or iteration (covered in Section 2).

[*lists-and-dicts.py*](/krash-kourse/objects/lists-and-dicts.py) - Figure 2.2
```python
a.append(42)
a.append(['I', 'am', 'a', 'list'])
print(a)
print(a[1])
```
```commandline
['Krash Kourse Rules', 42, ['I', 'am', 'a', 'list']]
42
```

Take note that the index of the list is 0-based. The Object in the list you may have considered "second" is located at an index of `1`. Similarly the first object is located at index `0` and so on.

What happens if the data we want to store isn't ordered? One option is the dictionary Object. A dictionary is a collection indexed by "keys" instead of integers. A dictionary is declared using the `{}` operator and accessed with the `[]` operator. Interestingly a "key" can be any "hash-able" object. To be "hash-able" a Python objects needs only hold an implementation of `__hash__`.

[*lists-and-dicts.py*](/krash-kourse/objects/lists-and-dicts.py) - Figure 2.3
```python
b = {}
b[22] = a
b['number'] = 42
print(b)
print(b['number'])
b[a] = 'string'
```
```commandline
{1: ['Krash Kourse Rules', 42, ['I', 'am', 'a', 'list']], 'number': 42}
42
Traceback (most recent call last):
  File "./lists-and-dicts.py", line 21, in <module>
    b[a] = 'string'
TypeError: unhashable type: 'list'
```

An astute reader may notice that the list Object does seem to have an implementation of `__hash__`, but it can not be used as a "key" in a dictionary. I encourage the reader to observe the output of `print(a.__hash__)` on their own to learn why.

There are several other interesting object types we have left to cover. As with most languages you can even create your own custom Object types. We will instead continue with a discussion which is central to Python, but which is typically left out from introductory courses on the subject. Please observe the following figure;

[*methods.py*](/krash-kourse/objects/methods.py) - Figure 3.1
```python
def does_nothing():
    return 1

print(dir(does_nothing))
print(does_nothing)
print(does_nothing.__call__)
print(does_nothing())
```
```commandline
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
<function does_nothing at 0x7fcfcd481d08>
<method-wrapper '__call__' of function object at 0x7fcfcd481d08>
1
```
This is a method. It represents some form of work we'd like to do. The basic syntax should be fairly clear. We begin with the keyword `def` followed by our method's name. Then we denote arguments of a function as comma-seperated variables in between the parenthesis of the defintion. More importantly the method is actually an object! The invoking of the `__call__` method occurs when we use the `()` operator.

What does this mean for us though? Well, firstly, this means we can pass functions as arguments to other functions for their own use. An exstension of this fact allows us to dynamically modify the context of a function by wrapping it in another function. This is known as decoration. See if you can identify the behavior of the below figure.


[*methods.py*](/krash-kourse/objects/methods.py) - Figure 3.2
```python
def ensure_integers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
               return None
        return func(*args)
    return wrapper

def sum(a, b):
    return a + b

validating_sum = ensure_integers(sum)

print(validating_sum(1, 2))
print(validating_sum('bob', 3))
print(sum)
print(validating_sum)
```
```commandline
3
None
<function sum at 0x7f9e0de13d90>
<function ensure_integers.<locals>.wrapper at 0x7f9e0de13e18>
```
There is a lot of new information to unpack here. Ignore the `for` statement and the `*args` variable for the time being. The key information to glean here is the relationship between `sum` and `ensure_integers`. We are giving `ensure_integers` our `sum` object and it is giving us back a completely new method object.

There is a bit of special syntax for decoration which was left absent in the above figure for clarity. We typically declare decoration like so;

[*methods.py*](/krash-kourse/objects/methods.py) - Figure 3.3
```python
@ensure_integers
def sum(a, b):
    return a + b

print(sum)
```
```commandline
<function ensure_integers.<locals>.wrapper at 0x7f1bc414ef28>
```
Of course, we've now lost the ability to refer to the`sum` directly without the wrapping work performed by `ensure_integers`. In some situations this may be undesirable, but as you grow your understanding of Objects you may discover the remedy to this issue. 

This concludes our discussion on Objects in Python. You should now understand how to declare, analyze, and use integers, strings, lists, dictionaries, and methods. Below you fill find a set of challenge tasks to help you get started with Objects on your own.

1. Try adding two numbers by directly calling the `__add__` method. Remeber the operator for calling a function is `()` with your parametes comma seperated between the parenthesis.
2. Try subtracting numbers and then try subtracting strings. The `-` operator indicates a subtraction. Try the same for multiplication (`*` operator). See if you can identify which ones worked and why.
3. Try writing your own decorator function. See if you can use the decorator to modify the context of printing a string to the standard out.

If this is your first introduction to Python you may wish to read further into the functionality of these Objects. You have the tools at your disposal to self analyze the functioning of Objects, but you may find it easier to read the documentation at <https://docs.python.org/3/>.


