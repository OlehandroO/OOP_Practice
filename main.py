class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    @property
    def average(self, sum=0, count=0):
        for grades in self.grades.values():
            for grade in grades:
                sum += grade
                count += 1
        return sum / count

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average}\n'
                f'Курсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}\n')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average < other.average

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average == other.average

    def __gt__ (self, other):
        if isinstance(other, Student):
            return self.average > other.average

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    @property
    def average(self, sum=0, count=0):
        for grades in self.grades.values():
            for grade in grades:
                sum += grade
                count += 1
        return sum / count

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average}\n')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average < other.average

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average == other.average

    def __gt__ (self, other):
        if isinstance(other, Lecturer):
            return self.average > other.average

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n')


best_student1 = Student('Ruoy', 'Eman', 'M')
best_student2 = Student('Bob', 'Bobsky', 'M')
best_student1.courses_in_progress += ['Python','C++']
best_student1.finished_courses += ['Java']
best_student2.courses_in_progress += ['Python','C++']
best_student2.finished_courses += ['Java']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python','C++']

lector1 = Lecturer('Tom', 'Tomas')
lector1.courses_attached += ['Python','C++']

lector2 = Lecturer('Sonya', 'Gordienko')
lector2.courses_attached += ['Python','C++']

best_student1.rate_lecture(lector1, 'Python', 10)
best_student1.rate_lecture(lector1, 'C++', 4)
best_student1.rate_lecture(lector1, 'Python', 5)

best_student1.rate_lecture(lector2, 'Python', 10)
best_student1.rate_lecture(lector2, 'C++', 10)
best_student1.rate_lecture(lector2, 'Python', 10)


cool_mentor.rate_hw(best_student1, 'Python', 10)
cool_mentor.rate_hw(best_student1, 'C++', 7)
cool_mentor.rate_hw(best_student1, 'Python', 4)

cool_mentor.rate_hw(best_student2, 'Python', 3)
cool_mentor.rate_hw(best_student2, 'C++', 5)
cool_mentor.rate_hw(best_student2, 'Python', 10)



print(lector2)

print(best_student1 > best_student2) #True
print(lector1 > lector2) #False