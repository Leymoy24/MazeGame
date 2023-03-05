import random

surname = {
    "part1": ["Прохор", "Лап", "Зав", "Нем", "Кам", "Красн", "Фом", "Ракит"],
    "part2": ["евич", "ов", "ский", "ович", "ий", "ук", "ев", "ян", "ич"]
}

initial = ["А.", "Г.", "Б.", "Ф.", "Р.", "Н.", "М", "З."]

f = open("Male_names.txt", "r", encoding="utf-8")
names = f.readlines()
names = [name.rstrip("\n") for name in names]
f.close()

# Вывод 10-ти случайный ФИО
for i in range(0, 10):
    first_part = surname["part1"][random.randint(0, len(surname["part1"]) - 1)]
    second_part = surname["part2"][random.randint(0, len(surname["part2"]) - 1)]
    name = names[random.randint(0, len(names) - 1)]
    ds = initial[random.randint(0, len(initial) - 1)]
    print(name + " " + ds + " " + first_part + second_part)
