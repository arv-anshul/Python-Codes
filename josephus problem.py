# The Josephus Problem - Numberphile
# When number of soilders is even
give = int(input('Enter a Number: '))
# give = 178
number = list(range(1, give+1))
print('Main list:', number)


def round_n(num_list, meta):    # num=10
    if meta == 'even':
        round_ = list(range(1, (len(num_list)//2)+1))
        return round_
    elif meta == 'odd':
        round_ = list(range(1, (len(num_list)//2)+1))
        round_.append(0)
        return round_


def loop_runner():
    if len(number) % 2 == 0:
        round_1 = round_n(number, 'even')
    else:
        round_1 = round_n(number, 'odd')

    for i in round_1:
        number.pop(i)


# loop start
for i in range(len(number)//2):
    if len(number) != 1:
        loop_runner()
    else:
        break

print('\nWinner is', number[0])