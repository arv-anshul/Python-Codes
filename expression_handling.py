# expression_handler function
# It is not a full fledged version of the function this is just a child function
# This function does not follow the BODMAS method.

def expression_handler(expression):
    OPERATORS = ['+', '-', '*', '/']
    digit = ''
    expression_list = []

    for i in expression.replace(' ', '') + '#':
        if i.isnumeric():
            digit += i

        elif i in OPERATORS:
            expression_list.append(digit)

            # Performing the operations > clear the list > appending the number
            if len(expression_list) == 3:
                number = perform_operation(expression_list)
                expression_list.clear()
                expression_list.append(number)

            expression_list.append(i)
            digit = ''

        elif i == '#':
            expression_list.append(digit)
            digit = ''

            # In the end of the expression
            # Performing the operations > clear the list > appending the number
            number = perform_operation(expression_list)
            expression_list.clear()
            expression_list.append(number)

    return expression_list[0]


def perform_operation(expression_list):
    if expression_list[1] == '+':
        return int(expression_list[0]) + int(expression_list[2])
    elif expression_list[1] == '-':
        return int(expression_list[0]) - int(expression_list[2])
    elif expression_list[1] == '*':
        return int(expression_list[0]) * int(expression_list[2])
    elif expression_list[1] == '/':
        return int(expression_list[0]) / int(expression_list[2])


if __name__ == '__main__':
    expression = '12/52*3-10'

    print(expression_handler(expression))
