from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.courses_attached:
                lecturer.grades.setdefault(course, [])
                lecturer.grades[course] += [grade]
        else:
            return 'Ошибка'

    def avg_grades(self):
        avglist = []
        for k, v in self.grades.items():
            avglist.append(mean(v))
        return mean(avglist)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grades():.1f}\nКурсы в процессе изучения: {str(self.courses_in_progress)}\nЗавершенные курсы: {str(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        avglist = []
        for k, v in self.grades.items():
            avglist.append(mean(v))
        return mean(avglist)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades():.1f}'

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
stud2.courses_in_progress += ['Python']

# Reviewer example
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 8)

# Lecturer example
lect1 = Lecturer('Some', 'Lecturer')
lect1.courses_attached += ['Python']

stud1.rate_lecturer(lect1, 'Python', 5)
stud2.rate_lecturer(lect1, 'Python', 7)
best_student.rate_lecturer(lect1, 'Python', 10)

# output
print(cool_mentor)
print(lect1)
print(best_student)