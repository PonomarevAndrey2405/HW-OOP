class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_rating = float()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.courses_attached:
                lecturer.grades.setdefault(course, [])
                lecturer.grades[course] += [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.avg_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.avg_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def __lt__(self, other):       
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.avg_rating < other.avg_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_rating = float()

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.avg_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.avg_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.avg_rating < other.avg_rating


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Students example
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

stud1 = Student('John', 'Doe', 'm')
stud1.courses_in_progress += ['Python']

stud2 = Student('Jane', 'Doe', 'f')
stud2.courses_in_progress += ['Java']

# Reviewer example
rev1 = Reviewer('Some', 'Buddy')
rev1.courses_attached += ['Python', 'Java']

rev2 = Reviewer('Aleksey', 'Krasko')
rev2.courses_attached += ['Python', 'Java']

rev1.rate_hw(stud1, 'Python', 10)
rev1.rate_hw(stud1, 'Python', 8)
rev1.rate_hw(stud1, 'Python', 9)

rev2.rate_hw(stud2, 'Java', 10)
rev2.rate_hw(stud2, 'Java', 9)
rev2.rate_hw(stud2, 'Java', 8)

rev1.rate_hw(best_student, 'Python', 10)
rev1.rate_hw(best_student, 'Python', 8)
rev1.rate_hw(best_student, 'Python', 9)


# Lecturer example
lect1 = Lecturer('Some', 'Lecturer')
lect1.courses_attached += ['Python']

lect2 = Lecturer('Ivan', 'Sidorov')
lect2.courses_attached += ['Java']

stud1.rate_lecturer(lect1, 'Python', 5)
stud2.rate_lecturer(lect1, 'Python', 7)
best_student.rate_lecturer(lect1, 'Python', 10)

stud1.rate_lecturer(lect2, 'Java', 8)
stud2.rate_lecturer(lect2, 'Java', 9)
best_student.rate_lecturer(lect2, 'Java', 10)

# output
print(f'Перечень студентов:\n{stud1}\n{stud2}\n{best_student}')

print(f'\nПеречень лекторов:\n{lect1}\n{lect2}')

student_list = [stud1, stud2, best_student]

lecturer_list = [lect1, lect2]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.avg_rating
            count_all += 1
    avg_for_all = sum_all / count_all
    return avg_for_all

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.avg_rating
            count_all += 1
    avg_for_all = sum_all / count_all
    return avg_for_all

print(f"\n\nСредняя оценка для всех студентов по курсу Python: {student_rating(student_list, 'Python')}")

print(f"\n\nСредняя оценка для всех лекторов по курсу Python: {lecturer_rating(lecturer_list, 'Python')}")