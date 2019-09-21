# from functions import add_two_numbers
# from functions import name_merger
from functions import marks_sum
from functions import mark_avrg
from functions import sum_digits
from task4 import even_odd1
# While-Loops are used when we lack a defined end to a loop

# A For-Loop is a loop the repeats until maximum is reached; we have a defined end.

# for a in range (10,101):
#     print(a)

# fruits = ["Apples" , "Mango" , "Avocado" , "Guava" , "Strawberry" , "Banana" , "Lemon"]
#
# for each in fruits:
#     each = each + "a"
#     print(each)

# sum = 0
# for each in range (10):
#     sum = each + sum
#     print(sum)


# name = "Ng'ang'a"
# sum = 0
# count = 0
# for each in range(100):
#     each = sum + each
#     count = count + 1
#     print(count,"."," ",name)

# for each in range(8,101,3):
#     print(each)
#
# first_name  = input("Enter First Name ")
# second_name  = input("Enter Second Name ")
# fullname = name_merger(first_name,second_name)
# print("The fullname is",fullname)

# math = eval(input("Enter Marks for Maths "))
# eng = eval(input("Enter Marks for English "))
# swa = eval(input("Enter Marks for Swahili "))
# sci = eval(input("Enter Marks for Science "))
# hist = eval(input("Enter Marks for History "))
#
# total_marks = marks_sum(math,eng,swa,sci,hist)
# average_marks = mark_avrg(total_marks)
#
# print("The Total Marks are",total_marks)
# print("The Average Mark is",average_marks)

num1 = input("Enter intergers: ")
num1 = int(num1)


kk1 = even_odd1(num1)

print(kk1)

