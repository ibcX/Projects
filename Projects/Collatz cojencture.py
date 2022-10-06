
# Collatz conjecture or, the 3n + 1 Problem
# The Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:
# If n is even, the next number n is n / 2.
# If n is odd, the next number n is n * 3 + 1.
# If n is 1, stop. Otherwise, repeat.

print("""Collatz conjecture
If n is even, the next number n is n / 2.
If n is odd, the next number n is n * 3 + 1.
If n is 1, stop. Otherwise, repeat.

""")

starting_number = int(input("Enter a starting number (greater than 0): \n"))
while starting_number != 1:
    if starting_number % 2 == 0:
        starting_number = starting_number/2
    elif starting_number % 2 == 1:
        starting_number = starting_number * 3 + 1
    print(int(starting_number), end=", ")

