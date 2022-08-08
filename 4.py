"""
my_list = ["Выпить кофе", "Выучить Python", "Захватить мир", "Пойти спать"]

nastroy = int(
    input("Введите свое настроение цифрами(1-Плохое, 2-Так себе, 3-Злое, 4-Усталое): ")
)
if nastroy == 1:
    print(my_list[0])
elif nastroy == 2:
    print(my_list[1])
elif nastroy == 3:
    print(my_list[2])
elif nastroy == 4:
    print(my_list[3])
"""
my_list = []
if my_list == [] or my_list[0]:
    print(f"Ваш список дел - пуст")

bisnes = input("Давайте добавим дело: ")
my_list.append(bisnes)
print(f"Ваш список дел - {my_list}")
qwest = input("Это все дела? Да или нет? ")

if qwest == "Нет" or qwest == "нет":
    bisnes = input("Введите новое дело: ")
    my_list.append(bisnes)
    print(f"Ваш список дел - {my_list}")
elif qwest == "Да" or qwest == "да":
    print("Ох, и бездельник вы")
