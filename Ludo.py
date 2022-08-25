import random

throw_list = []


def dice_get():
    # pop the element from the cache list if list is more than 6 element
    if len(throw_list) == 3:
        # throw_list.pop(0)
        del throw_list[0]
    if 6 in throw_list:
        return random.randrange(1, 6)
    else:
        return random.randrange(1, 7)


def play_ludo():
    """\n This is a ludo game in which if a player got 6 then\n no one got 6 before 3 round. I made it for fun and this type of condition \n"""

    # get random number from dice
    dice_number = dice_get()

    throw_list.append(dice_number)
    print(dice_number, "\t", throw_list)

    user_input = input("Press ENTER for next throw | 1 for end: ")
    play_ludo() if user_input == '' else print(throw_list)


print(play_ludo.__doc__)
user_input = input("Press ENTER for run | 1 for end: ")
play_ludo() if user_input == '' else exit()
