numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
number_to_find = 15


def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number > number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def find_all_occurances(number_list, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = list([index])

    # find all left side indices
    x = index - 1
    while x >= 0:
        if number_list[x] == number_to_find:
            indices.append(x)
        else:
            break
        x -= 1

    # find all right side indices
    x = index + 1
    while x <= len(number_list):
        if number_list[x] == number_to_find:
            indices.append(x)
        else:
            break
        x -= 1

        return sorted(indices)


indices = find_all_occurances(numbers, number_to_find)
print(f"Indices of occurances of {number_to_find} are {indices}")
