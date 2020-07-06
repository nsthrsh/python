class Student:
    def set_marks(self,mark,k):
        for i in range(k):
            self.mark[i] = mark[i]
    def set_name(self, name):
        self.name = name
    def get_average_mark(self,k):
        for i in range(k):
            self.s+= self.mark[i]
        print(self.name, ' - ', (self.s/len(self.mark)))
        
n=int(input("Введіть кількість студентів: "))
for i in range(n):
    student=Student()
    student.name=input("Введіть імя студента: ")
    k=int(input("Введіть кількість оцінок: "))
    student.s=0
    student.mark = [0]*k
    for j in range(k):
        student.mark[j]=int(input("Введіть оцінку студента: "))
    student.set_marks(student.mark,k)
    student.get_average_mark(k)
    print('\n')
