#!/usr/bin/env python3

def print_fibonacci(length):
  fib_sequence = []
  if length >= 1:
    fib_sequence.append(0)
  if length >=2:
    fib_sequence.append(1)

  for x in range(2, length):
    next_fibonacci_number = fib_sequence[x-1] + fib_sequence[x-2]
    fib_sequence.append(next_fibonacci_number)
  print(fib_sequence)

print_fibonacci(9)
