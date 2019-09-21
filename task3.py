def list_ends(a_list):
    return (a_list[0], a_list[len(a_list)-1])

# number of elements
num = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
put = list(map(int,input("\nEnter the numbers : ").strip().split()))[:num]

# Below Line calls the function created above.
put1 = list_ends(put)

#Outputs the values under indices '0' & '-1' (the last one in the list).
print("\nList is - ", put)

#Outputs the values under indices '0' & '-1' (the last one in the list).
print("\nNew List is - ", put1)