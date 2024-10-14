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

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average = [round(sum(num) / len(num), 1) for num in grades]
print(average)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)

group_1 = {sorted_students[num]:average[num] for num in range(len(average))}
group_2 = {student:average[num] for num, student in enumerate(sorted_students)}
group_3 = {student:grade for student, grade in zip(sorted_students, average)}
group_4 = dict(zip(sorted_students, average))

print(f"{group_1}\n{group_2}\n{group_3}\n{group_4}")

group = {}
for num in range(len(grades)):
    group[sorted_students[num]] = grades[num]

for num, student in enumerate(sorted_students):
    group[student] = grades[num]

for student, grade in zip(sorted(students), grades):
    group[student] = grade
print(group)

group_5 = {sorted(students)[num]:round(sum(grades[num]) / len(grades[num]), 1) for num in range(len(average))}
print(f"{group_5}")