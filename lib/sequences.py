#!/usr/bin/env python3

def print_fibonacci(length):
    numbers = []
    a = 0
    b = 1
    for i in range(length):
        numbers.append(a)
        a, b = b, a + b
    print(numbers)