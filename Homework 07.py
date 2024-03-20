'''
Задача 1: Уникальные элементы

Напишите функцию, которая принимает список и возвращает новый список
только с уникальными элементами из исходного списка.
'''
def delete_similar_elements(a):
    set_list = set(a)
    unique = list(set_list)
    return unique

my_list = [1, 2, 3, 4, 4, 4, 5, 4, 4]
print(delete_similar_elements(my_list))

'''
Задача 2: Переводчик с латиницы на кириллицу

Создайте словарь для перевода символов с латиницы на кириллицу.
Напишите функцию, которая принимает строку на латинице и возвращает её перевод
на кириллицу с использованием вашего словаря.
'''
def latin_cyrillic(text):
    text = text.lower()
    my_dict = {
            'a': 'а',
            'b': 'б',
            'c': 'ц',
            'd': 'д',
            'e': 'е',
            'f': 'ф',
            'g': 'г',
            'h': 'х',
            'i': 'и',
            'j': 'й',
            'k': 'к',
            'l': 'л',
            'm': 'м',
            'n': 'н',
            'o': 'о',
            'p': 'п',
            'q': 'к',
            'r': 'р',
            's': 'с',
            't': 'т',
            'u': 'у',
            'v': 'в',
            'w': 'в',
            'x': 'кс',
            'y': 'й',
            'z': 'з'
        }
    cyrillic = ''
    for element in text:
        cyrillic += my_dict.get(element, element)
    
    return cyrillic

latin_text = "Sozdavat slovar dolgo"

print(latin_cyrillic(latin_text))
'''
Задача 3: Объединение списков в кортежи

Напишите функцию, которая принимает два списка одинаковой длины
и возвращает список кортежей, где каждый кортеж состоит из элементов этих списков,
стоящих на одинаковых позициях.
'''
def zip_two_lists(list_one, list_two):
    if len(list_one) != len(list_two):
        print('Списки должны быть одинаковой длины')

    ziped_list = []
    for element in range(len(list_one)):
        ziped_list.append((list_one[element], list_two[element]))
    
    return ziped_list

list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]

print(zip_two_lists(list1, list2))

'''
Задача 4: Подсчет слов в тексте

Напишите функцию, которая анализирует текст (предоставленный в виде строки)
и возвращает словарь, где ключи — это уникальные слова, а значения —
количество их появлений в тексте.
'''
text = 'Задача 4: Подсчет слов в тексте Напишите функцию, которая анализирует текст'
text_list = text.split()

def list_to_dict_count(text_list):
    my_dict = {}
    for element in text_list:
        if element in my_dict:
            my_dict[element] += 1
        else:
            my_dict[element] = 1
    return my_dict

print(list_to_dict_count(text_list))
'''
Задача 5: Слияние словарей

Напишите функцию, которая объединяет два словаря
и суммирует значения одинаковых ключей.
'''
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3.5, 'c': 4, 'd': 5}
print(dict2['b'].isdigit())

def merge_n_sum_same_keys(dict1, dict2):
    result = dict1
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

print(merge_n_sum_same_keys(dict1, dict2))
'''
Задача 6: Частота элементов в списке

Напишите функцию, которая принимает список и возвращает словарь,
где ключи — это элементы списка, а значения — частота их появления.
'''
def list_to_dict_counter(list):
    dictionary = {}
    for element in list:
        if element in dictionary:
            dictionary[element] += 1
        else:
            dictionary[element] = 1
    return dictionary

text = 'Напишите функцию, которая принимает список и возвращает словарь, где ключи — это элементы списка, а значения — частота их появления.'
text_list = text.split()
result = list_to_dict_counter(text_list)
print(result)
'''
Задача 7: Разница между множествами

Напишите функцию, которая находит разницу
между двумя множествами и возвращает её в виде нового множества.
'''
def find_difference(set1, set2):
    set3 = set()
    for i in set1:
      if i not in set2:
         set3.add(i)
    for i in set2:
       if i not in set1:
          set3.add(i)
    return set3
'''
Задача 8: Сортировка списка кортежей

Напишите функцию, которая принимает список кортежей,
и каждый кортеж содержит два элемента.
Функция должна возвращать список кортежей,
отсортированный по второму элементу каждого кортежа.
'''
def sort_tuples_by_second_element(tuple_list):
    def get_second_element(item):
        return item[1]
    
    return sorted(tuple_list, key=get_second_element)

list = [(1, 5), (2, 3), (3, 8), (4, 1)]
print(sort_tuples_by_second_element(list))
'''
Задача 9: Самое длинное слово в строке

Напишите функцию, которая принимает строку
и возвращает самое длинное слово в этой строке.
'''
def longest_word(text):
    text_list = text.split()
    longest = ''
    for word in text_list:
        if len(word) > len(longest):
            longest = word
    return longest
'''
Задача 10: Удаление дубликатов из списка
Напишите функцию, которая удаляет все дубликаты из списка
и возвращает список, в котором каждый элемент уникален.
'''
def delete_duplicates(list):
    no_duplicates = []
    for element in list:
        if element not in no_duplicates:
            no_duplicates.append(element)
    return no_duplicates

