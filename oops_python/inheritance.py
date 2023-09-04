#DRY 
#DONOT REPEAT YOURSELF
#CODE REUSABILITY
class User:
    def login(self):
        print("Login")
    def register(self):
        print("Register")
class Student(User):
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")   
stu1 =Student()
stu1.enroll()
stu1.review()
stu1.login()
stu1.register()         
#child class is inheriting evry attribute of parent class         
#How to acess the constructor from a parent class.
#Return the factorial of the number N
# def factorial(N):
#     # Your code goes here

#   return 1 if (N==1 or N==0) else N * factorial(N - 1);
# num = int(input())
# print("Factorial of",num,"is",)
# factorial(num)