#!/usr/bin/env python3

# Figure 2.1
a = []
print(dir(a))
print(a.append)
a.append('Krash Kourse Rules')
print(a)

# Figure 2.2
a.append(42)
a.append(['I', 'am', 'a', 'list'])
print(a)
print(a[1])

# Figure 2.3
b = {}
b[22] = a
b['number'] = 42
print(b)
print(b['number'])
b[a] = 'string'