class StudentGrade:
    def __init__(self, student):
        self.student = student
        self.average = 0

    def averageGrade(self, grade1, grade2):
        self.average = (grade1 + grade2) / 2
        if self.average >= 7.00:
            print('O Aluno está aprovado!')
        return self.average

    def averageGradefinal(self, finalGrade):
        self.average = (self.average + finalGrade) / 2
        if self.average >= 5:
            print('O aluno está aprovado')
        return self.average

    def studentApproval(self):
        if self.average >= 5.00:
            print(f"Aluno {self.student} está aprovado!")
        else:
            print(f"Aluno {self.student} está reprovado, tente novamente ano que vem")

student_name = input("Digite o nome do aluno: ")

studentPerformance = StudentGrade(student_name)

grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))

studentPerformance.averageGrade(grade1, grade2)
final_grade = float(input("Digite a nota final: "))

studentPerformance.averageGradefinal(final_grade)
studentPerformance.studentApproval()

