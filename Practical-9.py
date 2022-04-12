# Name = Smit Mataliya
# Id = 20CE053
# Consider an example of declaring the examination result. Design 
three classes: Student, Exam, and Result. The Student class has data 
members such as those representing rollNumber, Name, etc. Create the 
class Exam by inheriting Student class. The Exam class adds fields 
representing the marks scored in six subjects. Derive Result from the 
Exam class, and it has its own fields such as total_marks. Write an 
interactive program to model this relationship.
#Github Link : https://github.com/smitmataliya/Practical-9
class Student:
 def _init_(self,name,id):
 self.name=name
 self.id=id
 def stu_info(self):
 print('Name of student is',self.name)
 print('Id is ',self.id)
class Exam(Student):
 def _init_(self,name,id,a1,a2,a3,a4,a5,a6):#for marks of 6 
subjects
 Student._init_(self,name,id)
 self.a1=a1
 self.a2=a2
 self.a3=a3
 self.a4=a4
 self.a5=a5
 self.a6=a6
 def marks_info(self):
 print('a1= ',self.a1)
print('a2= ',self.a2)
 print('a3= ',self.a3)
 print('a4= ',self.a4)
 print('a5= ',self.a5)
 print('a6= ',self.a6)
class Result(Exam):
 def _init_(self,name,id,a1,a2,a3,a4,a5,a6):
 Exam._init_(self,name,id,a1,a2,a3,a4,a5,a6)
 self.Total_Marks=a1+a2+a3+a4+a5+a6
 def f_result(self):
 return self.Total_Marks
print("How many student's data you want to print:")
n=int(input())
for i in range(1,n+1):
 print('Enter the Name of the student:')
 name=str(input())
 print("Enter id of the student: ")
 id=str(input())
 print("Enter a1")
 a1=int(input())
 print("Enter a2")
 a2=int(input())
 print("Enter a3")
 a3=int(input())
 print("Enter a4")
 a4=int(input())
 print("Enter a5")
 a5=int(input())
 print("Enter a6")
 a6=int(input())
 Result=Result(name,id,a1,a2,a3,a4,a5,a6)
 Result.stu_info()
 Result.marks_info()
 print("Total Marks is:",Result.f_result())