# Генерация двух файлов со случайными значениями для Сыпко Сергея
from random import randint

if __name__ == '__main__':
    result_40 = []
    result_5 = []

    list_40 = [i + 1 for i in range(40)]
    list_5 = [i + 1 for i in range(5)]

    for i in range(10):
        for j in range(len(list_40)):
            new_j = randint(0, len(list_40) - 1)
            list_40[j], list_40[new_j] = list_40[new_j], list_40[j]
        result_40.append([l for l in list_40])

        for j in range(len(list_5)):
            new_j = randint(0, len(list_5) - 1)
            list_5[j], list_5[new_j] = list_5[new_j], list_5[j]
        result_5.append([l for l in list_5])

    print(result_40)
    print(result_5)

    with open("40.csv", "w", encoding="utf-8") as file:
        for i in range(40):
            for j in range(10):
                file.write(f"{result_40[j][i]};")
            file.write("\n")
    print(f"Завершилась запись в файл 40.csv")

    with open("5.csv", "w", encoding="utf-8") as file:
        for i in range(5):
            for j in range(10):
                file.write(f"{result_5[j][i]};")
            file.write("\n")
    print(f"Завершилась запись в файл 5.csv")
