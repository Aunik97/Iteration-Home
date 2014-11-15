total = 0
counter = 0
finished = False

while not finished:
    number = float(input("Please enter number 'x'. Enter -1 when you have finished."))
    if number == -1:
        finished = True
    else:
        print("the programme is going to carry on")
        total = total + number
        counter = counter + 1
average = total / counter
print(average)
