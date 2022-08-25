no_of_words = int(input('How many words you have? '))


def take_input():
    w1 = set(input(f'Enter {count}{sup_num(count) } word: ').upper())
    w2 = set(input(f'Enter {count}{sup_num(count) } word: ').upper())
    main_set = w1.difference(w2)
    print('Required letter:', main_set)
    return main_set


def sup_num(num):
    if num == 1:
        return 'st'
    elif num == 2:
        return 'nd'
    elif num == 3:
        return 'rd'
    else:
        return 'th'


# extra variables
count = 1
word_dict = dict()

while count <= no_of_words:
    word = take_input()

    word_dict[count] = word

    print()
    count += 1

print()
for k, v in word_dict.items():
    print(f'{k}{sup_num(count) } letter:\t[ {" , ".join(v)} ]')
