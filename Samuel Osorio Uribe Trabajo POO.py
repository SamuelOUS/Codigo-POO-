class Students():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courses = []

    def Matriculate(self, Subject):
        if Subject == Subject in self.courses:
            print(f"La materia  {Subject.name} ya fue matriculada antes para el estudiante {self.name}")
        else:
            self.courses.append(Subject)
            Subject.StudentsIn.append(self)
            print(f"La materia {Subject.name} Fue matriculada con exito para el estudiante {self.name}")

    def Cancel(self, Subject):
        if Subject == Subject in self.courses:
            self.courses.remove(Subject)
            print(f"La materia  {Subject.name} fue cancelada para el estudiante  {self.name}")
        else:
            print(f"La materia {Subject.name} no fue matriculada o fue cancelada para el estudiante {self.name}")

class Teacher:
    def __init__(self,id, name):
        self.id = id
        self.name = name
        self.courses = []
    def Subjects(self, Subject):
        if Subject == Subject in self.courses:
            print(f"El profesor {self.name} ya dicta la clase {Subject}")
        else:
            self.courses.append(Subject)
            Subject.teacher.append(self)

class CreateExam:
    def __init__(self, ExamName, ExamPercent,ExamCourse):
            self.ExamnName = ExamName
            self.ExamPercent = ExamPercent
            self.Course = ExamCourse
            self.ExamQuestions = []

class Course:
    def __init__(self,id, name):
        self.id = id
        self.name= name
        self.StudentsIn = []
        self.teacher = []
    def get_student_list(self, Subject):

        if len(self.StudentsIn) == 0:
            print(f"La lista de estudiantes en el curso {Subject.name} esta vacia")
        else:
            print("La lista de estudiantes en el curso es:")
            for i in range(len(self.StudentsIn)):
                print(f"*{self.StudentsIn[i].name}")
    def remove_student(self, student):
        if student == student in self.StudentsIn:
            self.StudentsIn.remove(student)
            print(f"El estudiante {student.name} fue removido de el curso exitosamente")
        else: print(f"El estudiante {student.name} no esta en el curso")

class Exams:
    def __init__(self, name, percent):
        self.name = name
        self.percet = percent
        self.questions = []

Teacher_1 = Teacher(10, "Adrian")
Teacher_2 = Teacher(11, "German")
Teacher_3 = Teacher(12, "Rosa")
Teacher_4 = Teacher(13, "Juan")
Teacher_5 = Teacher(14, "Sebastian")

Course_1 = Course(1, "Matematicas")
Course_2 = Course(2,"Ciencias")
Course_3 = Course(3,"Electronica")
Course_4 = Course(4,"Fisica")
Course_5 = Course(5,"Geometria")

Student_1 = Students(12345,"Samuel")
Student_2= Students(23455,"Felipe")
Student_3 = Students(65432,"Emanuel")



Student_1.Matriculate(Course_1)
Student_1.Matriculate(Course_1)
Student_1.Cancel(Course_1)
Student_1.Cancel(Course_1)
Student_2.Matriculate(Course_3)
Student_2.Matriculate(Course_3)
Student_2.Matriculate(Course_4)


Teacher_1.Subjects(Course_1)
Teacher_2.Subjects(Course_2)
Teacher_3.Subjects(Course_3)
Teacher_4.Subjects(Course_4)
Teacher_5.Subjects(Course_5)
#Verification elements of Object

print(Course_1.id,Course_1.name,Course_1.StudentsIn[0].name,Course_1.teacher[0].name)

#Verification Elements of Student
print(Student_1.id,Student_1.name,Student_1.courses)
print(Student_2.id,Student_2.name,Student_2.courses[0].name,Student_2.courses[1].name)

#Verification Elements Teacher
print(Teacher_1.id,Teacher_1.name,Teacher_1.courses[0].name)

Course_1.get_student_list(Course_1)
Course_1.remove_student(Student_1)






















