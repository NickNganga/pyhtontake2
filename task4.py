def even_odd1(a):
    if a % 4 == 0:
        return(a, "is a multiple of 4")
    elif a % 2 == 0:
        return(a, "is an EVEN number.")
    else:
        return(a, "is an odd number")

def even_odd2(a,b):
    if a % b == 0:
        return(a, "divides evenly by", b)
    else:
        return(a, "does not divide evenly by", b)


num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

print(even_odd1(num))
print(even_odd2(num,check))