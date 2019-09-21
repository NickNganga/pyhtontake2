# A while-loop repeats until a specified condition is false

# a=1
#
# #the condition we are referencing is "a<10"
#
# while a < 101:
#     print(a)
#     a = a+2

savedPin = "0000"
trials = 3
enteredPin = input("Enter User PIN:"" ")
trials = trials-1
while savedPin != enteredPin and trials>0:
    enteredPin = input("Enter User PIN:"" ")
    trials = trials-1
else:
    if trials<1 and enteredPin != savedPin:
        print("Card Blocked." " " "Kindly Apply for Replacement")
    else:
        print("Log In Successful!")