# A function is a named, reuseable block of code used to perform a related task.

# a=0
# b=0
# a = a + 2
# b = b + 3
# c = a + b
# print(c)

# def add_two_numbers(a,b):
# # "add_two_numbers" is the name of the function while "def" is the key word python uses to create a new function.
#     c = a + b
# # "a" & "b" are function parameters while "c" is the return value.
#     return c
#
# def name_merger(d,e):
#     f = d + e
#     return f

def marks_sum(math,eng,swa,sci,hist):
    tot_marks = math + eng + swa + sci + hist
    return (tot_marks)

def mark_avrg(tot):

    return tot/5

def sum_digits(num):
    # hint: use for loops
    # hint: convert num to string
    sum_of_digits = 0
    num = str(num)
    for x in num:
        sum_of_digits = sum_of_digits + int(x)
    return sum_of_digits

