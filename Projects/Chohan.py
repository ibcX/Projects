
# Cho-Han
#
# In this traditional Japanese dice game, two dice are rolled in a bamboo
# cup by the dealer sitting on the floor. The player must guess if the
# dice total to an even (cho) or odd (han) number.

import random

def score_calculator(dice_1, dice_2, money, bet, bet_amount):
    sum_dices = dice_1 + dice_2
    fee = 0.1*bet_amount
    if sum_dices % 2 == 0:
        if bet == "cho" or bet == "even":
            money = money + bet_amount - fee
            print(f"You won! You take {bet_amount}. The house collects a {fee} fee.")
        elif bet == "han"  or bet == "odd":
            money = money - bet_amount - fee
            print(f"You lose! You have lost {bet_amount}. The house collects a {fee} fee.")
    else:
        if bet == "han" or bet == "odd":
            money = money + bet_amount - fee
            print(f"You won! You take {bet_amount}. The house collects a {fee} fee.")
        elif bet == "cho" or bet == "even":
            money = money - bet_amount - fee
            print(f"You lose! You have lost {bet_amount}. The house collects a {fee} fee.")
    return money


def main():
    money = 5000
    print(f"You have {money}. How much do you want to bet? (for exit insert command 'exit')\n")
    bet_amount=0
    while bet_amount != "exit":
        bet_amount = input("")
        if bet_amount == "exit":
            break
        elif not bet_amount.isdecimal():
            print("Not a valid amount!")
        else:
            bet_amount = int(bet_amount)
            if (money - bet_amount) < 0:
                print("You don't have that amount!")
            else:
                print("""
    The dealer swirls the cup and you hear the rattle of dice.
    The dealer slams the cup on the floor, still covering the dice and asks for your bet.""")
                bet = input("CHO (even) or HAN (odd)?\n")
                dice_1 = random.randint(1,6)
                dice_2 = random.randint(1,6)
                print(f"""
            The result is:
              {dice_1} - {dice_2}     
                    """)
                money = score_calculator(dice_1, dice_2, money, bet, bet_amount)
                if money <= 0:
                    print('You have run out of money!')
                    print('Thanks for playing!')
                    break
                print(f"You now have {money}. How much do you want to bet? (for exit insert command 'exit')\n")


main()