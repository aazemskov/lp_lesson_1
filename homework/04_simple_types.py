# https://learn.python.ru/lessons/04_simple_types.html?full#38

# Практика: Числа
'''
Создайте файл simple.py, и сделайте в нем следующую задачу:
a = 2
b = ???
print(a + b)  # задайте значение переменной b,
              # чтобы результат был 2.5
'''

a = 2
b = 0.5
print(a + b)

# Практика: Строки
'''
name = 'ВСТАВЬТЕ ВАШЕ ИМЯ'
print(???)  # сделайте так, чтобы программа 
# приветствовала вас, используя переменную name 
# и форматирование строк например "Привет, Миша!"
'''

name = 'Анатолий'
print(f'Привет, {name}!')

# Практика: Числа 2
'''
v = input('Введите число от 1 до 10: ')
print(???) 
# поправьте код, чтобы выводилось число
# на 10 больше, чем введённое
# например, пользователь ввел 10 
# программа вывела 20
'''

v = input('Введите число от 1 до 10: ')
print(int(v) + 10)

# Практика: Строки 2
'''
name = input('Введите ваше имя: ')
print(???) # поправьте код, чтобы выводилась строка
            # Привет, ИМЯ! Как дела?
'''

name = input('Введите ваше имя: ')
print(f'Привет, {name.upper()}! Как дела?')


# Практика: Приведение типов
# Выведите на экран при помощи print() результат работы:

# float('1')  # ???
>>> print(float('1'))
1.0
# int('2.5')  # ???
>>> print(int('2.5'))
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '2.5'
# bool(1)  # ???
>>> print(bool(1))
True
# bool('')  # ???
>>> print(bool(''))
False
# bool(0)  # ???
>>> print(bool(0))
False



















