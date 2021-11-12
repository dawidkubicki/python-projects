def add(*args):
    numbers = []
    for i in args:
        numbers.append(i)
    print(sum(numbers))

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)