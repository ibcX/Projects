import random
from datetime import datetime, timedelta


def birthday_generator(number):
    date_1 = datetime(year=1900, month=12, day=31)
    dates = []
    for i in range(0, number):
        days_gen = random.randint(1, 365)
        date_ = date_1 + timedelta(days=days_gen)
        dates.append(date_)
    return dates


def check_duplicates(birthdays, birthday_num):
    duplicate_dates = []
    for i in range(0, birthday_num):
        if birthdays[i] in birthdays[i + 1:-1]:
            duplicate_dates.append(birthdays[i])
    return duplicate_dates


def simulations(number):
    print(f"\n\nGenerating {number} random birthdays 100,000 times...")
    i = 1
    j = 0
    while i < 100000:
        birthdays = birthday_generator(number)
        duplicate_dates = check_duplicates(birthdays, number)
        if duplicate_dates:
            j += 1
        i += 1

    print(f"Out of 100,000 simulations of {number} people, there was a matching birthday in that group {j} times. "
          f"This means that {number} people have a {j / 1000} % chance of having a matching birthday in their group. "
          f"\nThat's probably more than you would think!")


def main():
    print("""
_________________________________________________    
           Birthday paradox
_________________________________________________    
    How many birthdays shall I generate? (Max 100)
    """)
    birthday_num = 0
    while birthday_num not in range(1, 101):
        birthday_num = int(input("Please insert a number: "))

    birthdays = birthday_generator(birthday_num)
    for i in birthdays:
        d = datetime.strftime(i, "%b %d")
        print(d, end=" ")
    duplicate_dates = check_duplicates(birthdays, birthday_num)
    if not duplicate_dates:
        print("\nIn this simulation, there are no duplicate birthdays")
    else:
        print("\nIn this simulation, multiple people have a birthday on", end=" ")
        for j in duplicate_dates:
            d = datetime.strftime(j, "%b %d")
            if j == duplicate_dates[-1] and len(duplicate_dates) > 1:
                print(f"and {d}")
            else:
                print(f"{d}", end=" ")
    simulations(birthday_num)


main()
