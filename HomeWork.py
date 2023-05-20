# task 2
# Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
number = ""
summ = 0
while len(number) != 3:
    number = input("Введите трехзначное число: ")
for i in number:
    summ += int(i)
print(number, summ)
print(f'Сумма цифр числа {number} равна {summ}!')