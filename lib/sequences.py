#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = list()
    if length >= 1:
        fibonacci_list.append(0)
        if length >= 2:
            fibonacci_list.append(1)
            if length >= 3:
                for i in range(2, length):
                    fibonacci_list.append(
                        fibonacci_list[i - 1] + fibonacci_list[i -2]
                    )
    print(fibonacci_list)


print_fibonacci(15)
