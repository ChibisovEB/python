from functools import reduce
def sum(a, b):
    return (a + b)

myList = [1,2,3,4,5, "weecg",7,8,90,23,5,4,6, "were",78,66,67,22,23,45,43,44]
# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number: '))
# ll = (lambda a, b: a + b)
# print(type(a))

# print(f'Sum of {a} and {b} is {sum(a, b)} with tradition function')
# print(f'Sum of {a} and {b} is {ll} with lambda function')
print(f'MyList  {myList}')
myList = list(filter(lambda x: type(x) is int , myList))
print(f'Четные {list(filter(lambda x: (x%2 == 0) , myList))}')
print(f'Нечетные {list(filter(lambda x: (x%2 != 0) , myList))}')
print(f'Конвертируем в строки {list(map(lambda x: (str(x)) , myList))}')
print(f'reduce {reduce((lambda x, y: x + y), myList)}')
