
# # Задача 26: Напишите программу, которая на вход принимает
# # два числа A и B, и возводит число А в целую степень B с
# # помощью рекурсии.
# # A = 3; B = 5 -> 243 (3⁵)
# # A = 2; B = 3 -> 8
# def degreeRecurse(A, B):
#     if B == 0:
#         return 1
#     if B < 0:
#         return 1/degreeRecurse(A, -B)
#     return A * degreeRecurse(A, B-1)
    
# A = int(input("A> "))
# B = int(input("B> "))
# print(f"A = {A}; B = {B} -> {degreeRecurse(A,B)}")


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a, b):
    if a == 0:
         return b;
    return sum(a-1, b+1)
    
a = int(input("a> "))
b = int(input("b> "))
print(f"a = {a}; b = {b} -> {sum(a,b)}")