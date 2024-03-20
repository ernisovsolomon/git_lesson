'''
1) Создайте список чисел, кратных 3, в диапазоне от 3 до 30.
'''

my_list = []

for i in range(3, 30):
    if i % 3 == 0:
        my_list.append(i)

print('Cписок чисел кратных 3: ', my_list)

'''
2) Создайте список четных чисел от 2 до 1 000 включительно.
'''
even_numbers = []

for i in range(2, 1001, 2):
    even_numbers.append(i)

print(even_numbers)

'''
3) Суммируйте все числа внутри списка четных чисел
'''
numbers = []

for i in range(2, 10, 2):
    numbers.append(i)

print('Наш список: ', numbers)

summa = 0
for i in numbers:
    summa += i

print('Сумма чисел внутри списка: ', summa)

'''
4) **Кубы: результат возведения числа в третью степень называется кубом.
Например, куб 2 записывается в языке Python в виде 2**3. Создайте список
первых 10 кубов (то есть кубов всех целых чисел от 1 до 10)
и выведите значения всех кубов в цикле for.
'''
cube_list = []

for i in range(1, 10):
    cube_list.append(i**3)

print(cube_list)

'''
50б.
Задача: Поиск наименьшего числа
'''
big_list = []

while True:
    user = int(input('Введите число: '))
    big_list.append(user)
    if user == 0:
        big_list.remove(0)        
        break

print('Наименьшее число: ', min(big_list))