# 1. Список студентов
groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Анна",
        "surname": "Сидорова",
        "exams": ["Английский", "Социология", "Право"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Петр",
        "surname": "Федоров",
        "exams": ["Физика", "Математика", "Химия"],
        "marks": [3, 4, 3]
    }
]

# 2. Функция фильтрации студентов по средней оценке
def filter_students(students):
    # Запрашиваем у пользователя средний балл
    try:
        avg_mark_to_filter = float(input("Введите средний балл для фильтрации: "))
    except ValueError:
        print("Ошибка: введите числовое значение.")
        return

    # Создаем список для отфильтрованных студентов
    filtered_students = []

    # Проходим по каждому студенту в списке
    for student in students:
        # Считаем средний балл студента
        average_mark = sum(student["marks"]) / len(student["marks"])
        # Если средний балл выше заданного, добавляем студента в новый список
        if average_mark > avg_mark_to_filter:
            filtered_students.append(student)

    # Выводим отфильтрованный список студентов
    print("\nСтуденты со средним баллом выше {:.2f}:".format(avg_mark_to_filter))
    if not filtered_students:
        print("Таких студентов нет.")
        return

    # Вывод "шапки" таблицы
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Оценки".ljust(20))
    # Вывод данных студентов
    for student in filtered_students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["marks"]).ljust(20))


# Вызов функции для фильтрации
filter_students(groupmates)