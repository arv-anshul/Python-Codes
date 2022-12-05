import re
from expression_handling import perform_operation


def expression_handler_2(expression):
    '''It handles BODMAS method operation very well.'''
    expression = expression.replace(' ', '')

    if expression.replace('.', '').isnumeric() or expression[0] == '-':
        return expression

    if '(' in expression and ')' in expression:
        expression_parts = re.findall(r'\((.*?)\)', expression)
        sub_expression = expression_parts[0]
        result = expression_handler_2(sub_expression)

        expression = expression.replace('(' + sub_expression + ')', result)
        return expression_handler_2(expression)

    elif '{' in expression and '}' in expression:
        expression_parts = re.findall(r'\{(.*?)\}', expression)
        sub_expression = expression_parts[0]
        result = expression_handler_2(sub_expression)

        expression = expression.replace('{' + sub_expression + '}', result)
        return expression_handler_2(expression)

    elif '[' in expression and ']' in expression:
        expression_parts = re.findall(r'\[(.*?)\]', expression)
        sub_expression = expression_parts[0]
        result = expression_handler_2(sub_expression)

        expression = expression.replace('[' + sub_expression + ']', result)
        return expression_handler_2(expression)

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

    return expression_handler_2(expression)


if __name__ == '__main__':
    expression = '12+36/{[2*3] + [6/1]}'
    print(expression_handler_2(expression))
