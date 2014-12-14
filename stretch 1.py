# Write a program that asks for a number and displays the squares
# of all the integers between 1 and this number inclusive.
# It should print 5 values on each line in neat columns.



def function1():
    
    




    string = "" 
    count = 0
    number = int(input("please enter a number"))
    while count < number:
        count = count + 1
        if count % 5:
            string = string + str((count) ** 2)+ ","
        else:
            string = string + str((count) ** 2)+ ","
            print(string)
            string = ""
    print(string)    


square = [] 
columns = 3
number = int(input("please enter a number"))
for x in range(1,number+1):
    square.append("{0:>5}".format(x**2))
for i in range(0, len(square),columns):
    print(",".join(square[i:i+columns]))

