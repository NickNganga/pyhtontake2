# number of elements
num = int(input("Enter number of elements: "))

# Below line read inputs from user using map() function
put = tuple(map(int,input("\nEnter the numbers: ").strip().split()))[:num]


tupp1 = int(len(put)/2)

#Outputs all the tuple values.
print("\nTuple is: ", put)

#Outputs the values of the first & last halves of the tuple.
print("\nFirst Tuple half is: ", put[:tupp1], "\nSecond Tuple half is: ", put[tupp1:])
# print("\nNew List is - ", put1)
