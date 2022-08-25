# ----
def trimming_process(word_1, word_2):
    rough_result = [i for i in word_1 if i not in word_2]
    main_result = list(dict.fromkeys(rough_result))
    # str_result = " | ".join(main_result)
    # return f'Your {count}{sur_number} letter: {str_result}'
    return main_result

def sur_num(num):
    if num == 1:
        return 'st'
    elif num == 2:
        return 'nd'
    elif num == 3:
        return 'rd'
    else:
        return 'th'


no_of_words = int(input('Number of letter in that word: '))
count = 1
all_word_list = {}

print('\n<><><><><><><><> Start <><><><><><><><>')
while no_of_words >= count:
    sur_number = sur_num(count)
    print(f'\n~~~~~~~~~~~~ {count}{sur_number} word ~~~~~~~~~~~~~')

    org_word = list(input(f'Enter {count}{sur_number} org_word: ').upper())
    rej_word = list(input(f'Enter {count}{sur_number} rej_word: ').upper())

    final_word = trimming_process(org_word, rej_word)

    all_word_list[count] = final_word

    print(f'>> Your {count}{sur_number} letter:', " | ".join(final_word))

    count += 1

print()
for key, value in all_word_list.items():
    print(f'{key}{sur_num(key)} letter:\t[ {" | ".join(value)} ]')