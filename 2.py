99# Задача ввести двухзначное число, на выходе сумму этих двух чисел

# input digits
numbers = input("input two numbers ")
# Вынимаем цифры из ввода
numbers_1 = numbers[0]
numbers_2 = numbers[1]
# Переобразование и сложение
sum = int(numbers_1) + int(numbers_2)
# Вывод
print (numbers_1, '+', numbers_2, '=', sum)

# Работа с условиями
sun = input("Введите 1 если солнечно, и 2 если посмурно ")
if sun == '1':
    d = "Можно загарать"
else:
    d = "Смотрим телевизор"
print(d)

myname = input("Введите логин: ")
mypass = input("Введите пароль: ")
if myname == 'Ivan' and mypass == '12345678':
    print("Добро пожаловать админ!")
else:
    print("Доступ закрыт")
    