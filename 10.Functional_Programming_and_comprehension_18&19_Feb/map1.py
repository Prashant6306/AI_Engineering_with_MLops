


# def cube(n):
#     list1=[]
#     for i in n:
#         list1.append(i**3)
#     return list1

# values=[2,3,4,5,6]
# result=cube(values)
# print(result)


## Syntax: map(function, iterable)
def cube(n):
    return n**3

values=[2,3,4,5,6]

map_obj=map(cube, values)
result=list(map_obj)
print(result)