

# Fibonacci Sequence

print("Fibonacci Sequence")
fib_numbers = int(input("Enter how many Fibonacci numbers would you like to be calculated: "))

fib_1 = 0
fib_2 = 1

if fib_numbers == 1:
    print("The first Fibonacci number is 0")
elif fib_numbers == 2:
    print("The first two Fibonacci numbers are: 0 and 1")
else:
    print('0, 1', end=", ")
    for i in range(2, fib_numbers):
        fib_3 = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_3
        if i < (fib_numbers - 1):
            print(fib_3, end=", ")
        elif i == (fib_numbers - 1):
            print(fib_3)
        i += 1
