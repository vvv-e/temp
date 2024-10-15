# Кортеж списков
tuple_of_lists = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

# Перебор элементов кортежа списков
for lst in tuple_of_lists:
    for item in lst:
        print(item, end=" ")
    print()  # Переход на новую строку после каждого списка
