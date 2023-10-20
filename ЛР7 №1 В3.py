class Student:
    def __init__(self, last_name, first_name, middle_name, birth_date, address, phone, faculty, course):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.address = address
        self.phone = phone
        self.__faculty = faculty
        self.__course = course
    @property
    def faculty(self):
        return self.__faculty
    @faculty.setter
    def faculty(self, new_faculty):
        self.__faculty = new_faculty
    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self, new_course):
        if 1 <= new_course <= 6:  #Предполагается, что курс может быть от 1 до 6
            self.__course = new_course
        else:
            print("Курс должен быть в диапазоне от 1 до 6.")
    def __str__(self):
        return f"Студент: {self.last_name} {self.first_name} {self.middle_name}\n" \
               f"Дата рождения: {self.birth_date}\n" \
               f"Адрес: {self.address}\n" \
               f"Телефон: {self.phone}\n" \
               f"Факультет: {self.faculty}\n" \
               f"Курс: {self.course}"
#использование класса Student:
student = Student("Иванов", "Илья", "Иванович", "02.02.2002", "ул.Западная, д.2", "+375 29 888-33-44", "Программирование", 2)
print(student) #вывод класса
