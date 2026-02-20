

#prices = [10, 25, 40, 55]
#ouput:[20, 50, 80, 110]

# def double(n):
#     return n*2

# prices = [10, 25, 40, 55]

# result=list(map(double,prices))
# print(result)


# double1=lambda n:n*2
# print(double1(10))

## Syntax: map(function, iterable)
# prices = [10, 25, 40, 55]
# result=list(map(lambda n:n*2, prices))
# print(result)


celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c*9/5)+32, celsius))
print(fahrenheit)


fruits = ['apple','kiwi','banana','fig']
lengths = set(map(lambda f: len(f), fruits))
print(lengths)


costs = [100, 200, 350]
with_tax = list(map(lambda x: x * 1.18, costs))
print(with_tax)