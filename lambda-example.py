from functools import reduce
def sum(a, b):
    return (a + b)

myList = [1,2,3,4,5, "weecg",7,8,90,23,5,4,6, "were",78,66,67,22,23,45,43,44]
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
# ll = (lambda a, b: a + b)
# print(type(a))

# print(f'Sum of {a} and {b} is {sum(a, b)} with tradition function')
# print(f'Sum of {a} and {b} is {ll} with lambda function')
print(f'MyList  {myList}')
myList = list(filter(lambda x: type(x) is int , myList)) # исключаем из списка все нечисла
print(f'Четные {list(filter(lambda x: (x%2 == 0) , myList))}') # показываем только четные числа
print(f'Нечетные {list(filter(lambda x: (x%2 != 0) , myList))}') # показываем только четные нечисла
print(f'Конвертируем в строки {list(map(lambda x: (str(x)) , myList))}') # конвертация в строки всего спсика
print(f'reduce {reduce((lambda x, y: x + y), myList)}') # сумма всех элементов

tables = [lambda x = x: x*10 for x in range(1, 11)]
for table in tables:
    print(table())

max_number = lambda a, b : a if a > b else b
print(f"выводим максмальное число {max_number(30, 102)}")
print(a if a > b else b) # вывод условный

# Лямбда и множественные операторы
# Вложенная лямбда функция
current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
result = second_largest(current_list, sorted_list)
print(current_list)
print(result)
