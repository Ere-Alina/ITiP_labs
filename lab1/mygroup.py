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
        "name": "Анастасия",
        "surname": "Волкова",
        "exams": ["АиГ", "ИС", "Web"],
        "marks": [4, 5, 3]
    },
    {
        "name": "Константин",
        "surname": "Лавочкин",
        "exams": ["Web", "Информатика", "ЭЭиС"],
        "marks": [4, 4, 3]
    },
    {
        "name": "Виктория",
        "surname": "Боярова",
        "exams": ["Философия", "Web", "АиГ"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Павел",
        "surname": "Тапочкин",
        "exams": ["Web", "КТП", "Философия"],
        "marks": [3, 3, 5]
    }
]

# функция фильтрации студентов по средней оценке
def filter_students(students, average):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20), u"Средний балл".ljust(15))
    for student in students:
        sum = 0
        for mark in student["marks"]:
            sum += mark
        avg = sum / len(student["marks"])
        if (round(avg, 2) > average):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20), str(round(avg, 2)).ljust(15))
    

middle = float(input("Введите средний балл: ")) 
filter_students(groupmates, middle) 