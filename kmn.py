from random import randint

# 1 - Stone
# 2 - Paper
# 3 - Shear


def game(kmn, choise):
    if choise >3:
        print("You make input Error")
        return None
    if kmn == 3 and choise == 1:
        return True
    if kmn == choise:
        return None
    return choise > kmn


player_win = 0
computer_win = 0
while True:
    print(f"""
    You win is {player_win},
    you lose is {computer_win}""")
    try:
        game_controler = int(input("""
        Lets go play?
        1 - Yes
        2 - No \n"""))
        if game_controler == 2:
            print("Good bye!!!")
            break

        kmn = randint(1, 3)
    
        choise = int(input("""
        1 - Stone
        2 - Paper
        3 - Shear
        """))

        result = game(kmn, choise)
        if result:
            print("You win")
            player_win += 1
        elif result == None:
            player_win += 1
            computer_win +=1
        else:
            print("You lose")
            computer_win +=1
    except ValueError:
        print("You make input Error")


