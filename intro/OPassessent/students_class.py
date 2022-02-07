'''
an example of property and how to add up related objects, see all_students var
'''
class Student:
    # Write your code here.
    all_students = []
    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)


    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if  new_grade < 0 or new_grade > 101:
            raise ValueError ("New grade not in accepted range of [0-100]")         
        else:
            self._grade = new_grade
            #return print(f'current grage is {self._grade}')

    @staticmethod
    def calculate_average_grade(students):
        return -1 if len(students)==0 else (sum(n.grade for n in students))/len(students)

    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)

    

    @classmethod
    def get_best_student(cls):
        best_student = None
        for student in cls.all_students:
            if best_student == None or best_student.grade < student.grade:
                best_student = student
        return best_student


st1 = Student('Vicky',10)
st1.grade = 50
st2 = Student('Paul',20)
st2 == Student.get_best_student()
print(st2 == Student.get_best_student())
r = Student.calculate_average_grade([st1,st2])
print(r)

