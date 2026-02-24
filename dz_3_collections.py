'''
Задание №1

Написать программу, которая получает на вход строку и возвращает словарь, где:
ключи — символы из этой строки;
значения — количество раз, сколько каждый символ встречается.
'''

user_input = input('Введите что угодно, программа вернут словарь, где ключи - это уникальные значения, а значение кол-во таких ключей в строке)\n>>> ')

result_dict = {}

for elem in user_input:
    if elem in result_dict:
        result_dict[elem] += 1
    else:
        result_dict[elem] = 1

print(result_dict)

'''
Задание №2

Дана строка текста (или введённая через консоль). Программа должна вернуть новую строку, в которой порядок слов будет обратным.
Пример:
"Python is really cool" → "cool really is Python".

'''
user_input = input('Введите что угодно, программа вернет строку c обратным порядком слов)\n>>> ')
print(' '.join(user_input.split(' ')[::-1]))


'''
Задание №3

Написать программу, которая удаляет из списка все дубликаты, сохранив исходный порядок элементов.

# '''

my_list = [1, 1, 2, 2, 'asd', 'asd']
# print(list(set(my_list)))

new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)


'''
Задание №4

Дана строка текста (или введённая через консоль). Программа должна вернуть словарь с четырьмя ключами:
"гласные",

"согласные",

"цифры",

"пунктуация".

Значения — количество символов каждого типа в строке.

'''

symbol_dict = {
    "гласные": 0,
    "согласные": 0,
    "цифры": 0,
    "пунктуация": 0
    }

user_input = input('Введите строку, программа вернет словарь c количество гласных, согласных, цифр и пунктуационных символов)\n>>> ')

vowels = "аеёиоуыэюяaeiouy"
consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz"
digits = "0123456789"
punctuation = ".,!?:;()-—[]\\{\\}«»\"'…/\\|*#@&%$€£¥+=<>~`^"

for elem in user_input:
    if elem.lower() in vowels:
        symbol_dict['гласные'] += 1
    elif elem.lower() in consonants:
        symbol_dict['согласные'] += 1
    elif elem.lower() in digits:
        symbol_dict['цифры'] += 1
    elif elem.lower() in punctuation:
        symbol_dict['пунктуация'] += 1

print(symbol_dict)
