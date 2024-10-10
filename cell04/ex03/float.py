#!/usr/bin/env python3
x = input('Give me a number: ')
y = float(x)

if y.is_integer():
    print('This number is an integer.')
else:
    print('This number is a decimal.')
