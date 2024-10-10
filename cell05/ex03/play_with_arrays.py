#!/usr/bin/env python3
x = [2, 8, 9, 48, 8, 22, -12, 2]
y = [num + 2 for num in x]
z = [num for num in y if num > 5]
a = list(dict.fromkeys(z))
print(x)
print(a)
