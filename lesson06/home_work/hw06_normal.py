# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


class Person:
    last_name: str
    first_name: str
    middle_name: str

    def __init__(self, last_name='Smith', first_name='John', middle_name='Ll'):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

    def __str__(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.middle_name)

    def __add__(self, other):
        return '{} {} {} и {} {} {}'.format(self.last_name, self.first_name, self.middle_name, other.last_name, other.first_name, other.middle_name)


class Teacher(Person):
    subject: str

    #    school_classes: list

    def __init__(self, last_name, first_name, middle_name, subject):  # , school_classes: list):
        super(Teacher, self).__init__(last_name, first_name, middle_name)
        self.subject = subject


#        self.school_classes = school_classes


class SchoolClass:
    number_class: str
    teachers: list = []

    #    students = []

    def __init__(self, number_class: str = '7z', teachers=[]):  # students: list = []):
        self.number_class = number_class
        self.teachers = teachers


#        self.students = students

#    def add_student(self, student):
#         self.students.append(student)


class Student(Person):
    mother: Person()
    father: Person()
    school_class: SchoolClass()

    def __init__(self, last_name, first_name, middle_name, mother, father, school_class):
        super(Student, self).__init__(last_name, first_name, middle_name)
        self.mother = mother
        self.father = father
        self.school_class = school_class


class School:
    # -----Parents--
    par1 = Person('Мишин', 'Валерий', 'Игнатьевич')
    par2 = Person('Нуриева', 'Нурия', 'Рашидовна')
    par3 = Person('Абдулкадеров', 'Айрат', 'Иванович')
    par4 = Person('Абдулкадерова', 'Альфия', 'Рахимовна')
    par5 = Person('Семёнов', 'Василий', 'Абрамович')
    par6 = Person('Барабан', 'Людмила', 'Андреевна')
    par7 = Person('Яровой', 'Пётр', 'Юрьевич')
    par8 = Person('Бронштейн', 'Анастасия', 'Израильевна')
    # --------------
    # -----Teachers-
    teac1 = Teacher('Мишин', 'Валерий', 'Игнатьевич', 'English')
    teac2 = Teacher('Потапов', 'Константин', 'Игнатьевич', 'Russian')
    teac3 = Teacher('Валерьев', 'Михаил', 'Вадимович', 'Math')
    teac4 = Teacher('Антонова', 'Лариса', 'Сергеевна', 'Chinese')
    teac5 = Teacher('Хаханова', 'Антонина', 'Михайловна', 'Geography')
    teac6 = Teacher('Соломонова', 'Юлия', 'Петровна', 'Other')
    list_teachers = [teac1, teac2, teac3, teac4, teac5, teac6]
    # --------------
    # --Classes-----
    cl1 = SchoolClass('8ф', list_teachers)
    cl2 = SchoolClass('5я', [teac6, teac5, teac3, teac2, teac1])
    cl3 = SchoolClass('3а', [teac2, teac3, teac5])
    cls = [cl1, cl2, cl3]
    # --------------
    # ------Students
    st1 = Student('Файзрахманов', 'Рафаиль', 'Гайтульфардович', par2, par1, cl3)
    st2 = Student('Гузеева', 'Марина', 'Александровна', par4, par3, cl2)
    st3 = Student('Лимонов', 'Максим', 'Ильич', par6, par5, cl3)
    st4 = Student('Лимонов', 'Фёдор', 'Ильич', par6, par5, cl1)
    st5 = Student('Иванов', 'Кирилл', 'Олегович', par8, par7, cl1)
    st5.school_class
    students = [st1, st2, st3, st4, st5]
    # --------------
    # -------------1

    @property
    def all_classes_of_school(self):
        set_students = set()
        for st in self.students:
            set_students.add(st.school_class.number_class)
        return set_students
    # -------------2

    def all_students_from_class(self, number_class: str):
        return [st.last_name + ' ' + st.first_name[:1] + '. ' + st.middle_name[:1] + '.'
                for st in self.students if st.school_class.number_class == number_class]
    # -------------3

    def all_subject_from_student(self, name):
        result = []
        for student in self.students:
            if student.last_name + ' ' + student.first_name + ' ' + student.middle_name == name:
                for teacher in student.school_class.teachers:
                    result.append(teacher.subject)
        return result
    # -------------4

    def ancestors_of_students(self, name):
        result = []
        for student in self.students:
            if student.last_name + ' ' + student.first_name + ' ' + student.middle_name == name:
                return student.father + student.mother
    # -------------5

    def list_of_teachers_from_class(self, number_class):
        result = []
        for cl in self.cls:
            if cl.number_class == number_class:
                for teac in cl.teachers:
                    result.append(teac.last_name + ' ' + teac.first_name + ' ' + teac.middle_name)
        return result
#
#        par2for sall_students_from_class(self):
# ,tudent in


sc = School()
# -------------1
print(sc.all_classes_of_school)
# -------------2
number_class = '3а'
print(sc.all_students_from_class(number_class))
# -------------3
print(sc.all_subject_from_student('Гузеева Марина Александровна'))
# -------------4
print(sc.ancestors_of_students('Иванов Кирилл Олегович'))
# -------------5
print(sc.list_of_teachers_from_class('8ф'))
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
