import re
from expression_handling import perform_operation


def expression_handler_1(expression):
    expression = expression.replace(' ', '')

    if expression.replace('.', '').isnumeric() or expression[0] == '-':
        return expression

    if '/' in expression:
        expression_parts = re.findall(r'\w*[.]*\w*\/\w*[.]*\w*', expression)
        expression_list = expression_parts[0].split('/')
        expression_list.insert(1, '/')

    elif '*' in expression:
        expression_parts = re.findall(r'\w*[.]*\w*\*\w*[.]*\w*', expression)
        expression_list = expression_parts[0].split('*')
        expression_list.insert(1, '*')

    elif '+' in expression:
        expression_parts = re.findall(r'\w*[.]*\w*\+\w*[.]*\w*', expression)
        expression_list = expression_parts[0].split('+')
        expression_list.insert(1, '+')

    elif '-' in expression:
        expression_parts = re.findall(r'\w*[.]*\w*\-\w*[.]*\w*', expression)
        expression_list = expression_parts[0].split('-')
        expression_list.insert(1, '-')

    # print(expression_list, '>>>\t', expression)
    result = str(perform_operation(expression_list))
    expression = expression.replace(expression_parts[0], result)

    return expression_handler_1(expression)


if __name__ == '__main__':
    expression = '12+34/2*3'
    print(expression_handler_1(expression))
