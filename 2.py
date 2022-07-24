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