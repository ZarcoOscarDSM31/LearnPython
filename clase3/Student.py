
class Student :

    count = 0

    def __init__(self, name, age, languages, address, is_active):
        self.name = name
        self.age = age
        self.languages = languages
        self.address = address
        self.is_active = is_active
        Student.count += 1

    def __str__(self):
        return f'Estudiante: {self.name}, Edad: {self.age}, Lenguajes: {self.languages}, Direccion: {self.address}, Activo: {self.is_active}'

    @staticmethod
    def get_total_students():
        return Student.count

    @classmethod
    def get_total_students_class(cls):
        return cls.count

if __name__ == '__main__':
    student = Student('Oscar Daniel', 20, ['Python', 'C#', 'Java'], {'street': 'Calle 1', 'city': 'CDMX', 'country': 'Mexico'}, True)
    print(Student.get_total_students())
    print(Student.get_total_students_class())


    student2 = Student('Juan Perez', 30, ['javascript', 'PHP', 'c++'], {'street': 'Calle 2', 'city': 'CDMX', 'country': 'Mexico'}, True)
    print(Student.get_total_students())
    print(Student.get_total_students_class())


