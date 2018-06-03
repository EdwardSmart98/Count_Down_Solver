import itertools
import operator
import random
import re

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
op_order = ['-', '+', '*', '/']

def main():

    [target, values] = user_input();
    print("virtual_target = " + str(target))
    print("values to use:")
    print(values)
    operations = ['+', '-', '*', '/']
    permutations = get_possible_permutations(values, operations)
    answer = 0
    for i in permutations:
        if evaluate_rpn(i, target) != 0:
            answer = rpn_to_arabic(i, evaluate_rpn(i, target))

            break
    if answer == 0:
        print('no solution found')
    else:
        print('solution found!')
        print('-------------')
        print(answer)
        print('-------------')
    return answer


def user_input():
    if input("use random values y/n") == 'y':
        target = random.randint(100, 999)
        values = random.sample(range(1, 10), 6)
    else:
        target = input("enter virtual_target value")
        values = input("enter values to use: e.g. 1,2,3,4,5")
        values = [int(x) for x in re.split(',| ', values)]
    return[target, values]


def evaluate_rpn(rpn, result):

    operations = [x for x in rpn if type(x) is str]
    values = [x for x in rpn if type(x) is int]
    numbers_used = 0
    while len(operations) != 0:
        op = ops[operations.pop()]
        a = values.pop()
        b = values.pop()
        if op == operator.truediv and a == 0:
            return 0
        values.append(op(a,b))
        numbers_used = numbers_used + 1
        if values[len(values)-1] == result:
            return numbers_used
    return 0


def rpn_to_arabic(rpn, numbers_used):
    expression = ''
    operations = [x for x in rpn if type(x) is str]
    values = [x for x in rpn if type(x) is int]
    for i in range(numbers_used):
        expression = expression + '('
    for i in range(numbers_used):
        expression = expression + str(values.pop()) + ")" + operations.pop()
    expression = expression + str(values.pop())

    return expression


def get_possible_permutations(values, operations):
    val_permutations = list(itertools.permutations(values, len(values)))
    op_combinations = list(itertools.product(operations, repeat=len(values)-1))
    choices = []
    for i in val_permutations:
        for j in op_combinations:
            choices.append(i+j)
    print('testing ' + str(len(choices)) + ' permutations...')
    return choices


while True:
    main()
    if input("do you want to go again (y/n)?") != 'y':
        print('\nstopping...........')
        break
