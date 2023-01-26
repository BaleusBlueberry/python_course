def add(*args):
    result = 0
    for n in args:
        result += n
    print(result)

add(1, 4, 7, 3, 120)


def calculate(**kwargs):

calculate(add=3, multiply=5 )