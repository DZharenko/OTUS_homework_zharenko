'''
Написать функцию, которая принимает неограниченное количество чисел в виде позиционных аргументов и ключевой аргумент — операцию над этими числами (сложение или умножение).
Функция должна возвращать результат выполнения указанной операции.

'''

def add_or_multiply_func(*args,operation='add'):

    if operation == 'add':
        result = sum(args)
        print(f'Результат сложения равен {result}')
        return result
    elif operation == 'multiply':
        result = 1
        for elem in args:
            result *= elem
        print(f'Результат умножения равен {result}')
        return result
    else:
        print('Вы не ввели аргументы или операцию')

'''
Написать функцию для ввода из консоли целого числа.
Если введено не число, функция должна вывести соответствующее сообщение и предложить ввести значение заново — до тех пор, пока пользователь не введёт корректное число.
'''

def check_integer():

    while True:
        number = input('Введите целое число\n>>>')
        if number.isdigit():
            print(f'Вы ввели целое число - {number}')
            break
        else:
            print('Введенное значение не является целым числом, повторите попытку')

'''
Написать функцию, которая создаёт абсолютный путь к файлу.

Позиционные аргументы:

название диска,

неограниченное количество папок,

имя файла (без расширения).


Ключевые аргументы:
ext — расширение файла,

sep — разделитель (по умолчанию '/').

'''
# Решение через конкатенацию
def create_full_path_to_file(*args, ext='xlsx', sep='/'):
    full_path = ''
    for elem in args:
        full_path += f'{elem}{sep}'

    full_path_w_ext = f'{full_path[:-1]}.{ext}'
    print (f' Полный путь - {full_path_w_ext}')
    return full_path_w_ext

create_full_path_to_file('c','work', 'funx')

# Решение через join
def create_full_path_to_file(*args, ext='xlsx', sep='/'):
    full_path = sep.join(args)
    result = f' Полный путь - {full_path}.{ext}'
    print(result)
    return result

'''
Написать функцию, которая принимает список, состоящий из объектов разных типов, и возвращает словарь, где:
ключи — типы данных объектов;
значения — списки объектов соответствующего типа.
'''

def list_to_dict(data):
    dict_from_list = {}
    for elem in data:
        key = type(elem)
        dict_from_list.setdefault(key, [])
        dict_from_list[key].append(elem)
    return dict_from_list


