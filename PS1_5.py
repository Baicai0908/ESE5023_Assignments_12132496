from functools import reduce

operators = {
    1: '+',
    2: '-',
    0: ''
}

bases = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def find_expression(num):
    arr = []
    for i in range(8):
        i = 7-i
        arr.append(num//(3**i))
        num -= (num//(3**i))*(3**i)

    arr = map(lambda x: operators[x], arr)

    formula = reduce(lambda x, y: x+y, zip(bases, arr))
    formula = list(formula)
    formula.append('9')
    formula = ''.join(formula)

    result = eval(formula)
    return result, formula


if __name__ == '__main__':
    total = 3**8
    n = 0
    Total_solutions = []
    for j in range(total):
        result, formula = find_expression(j)
        if result == 50:
            print(formula+" = 50")

    for k in range(1, 100):
        for l in range(total):
            result, formula = find_expression(l)
            if result == k:
                n += 1
        Total_solutions.append(n)
        n = 0

print(Total_solutions)
print(Total_solutions.index(max(Total_solutions))+1)
print(Total_solutions.index(min(Total_solutions))+1)
