#!/usr/bin/env python3
for x in range(0, 11):
    print(f"Table de {x}:", end=" ")
    for y in range(0, 11):
        print(x * y, end=" ")
    print()
