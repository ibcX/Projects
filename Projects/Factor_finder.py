

# Factor finder
#  A number's factors are two numbers that, when multiplied with each other, produce the number.

print("Factor finder")

user_input = ""
while user_input != "exit":
    user_input = input("Enter a number to factor: ")
    if user_input == "exit":
        break
    else:
        user_input = int(user_input)
        factors = []
        for i in range (2, user_input - 1):
            if user_input % i == 0:
                factors.append(i)
        if bool(factors) == False:
            print("It's a prime number.")
        else:
            print(str(factors))
