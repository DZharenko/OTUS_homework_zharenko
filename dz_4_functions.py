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
        print(f'Вы не ввели аргументы или операцию')





    