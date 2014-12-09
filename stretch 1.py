# Write a program that asks for a number and displays the squares
# of all the integers between 1 and this number inclusive.
# It should print 5 values on each line in neat columns.


#number = int(input("please enter a number"))
#for count in range(1, number+1):
 #   print(number**2)
    
    
count = 0
number = int(input("please enter a number"))
while count <= number:
    count = count + 1
    if count <= number:
         print((number - count )** 2)
    else:
        print("programe end")
