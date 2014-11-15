number = 0
while number > 20 or number < 1:

    number = int(input("please enter a number between 10 and 20: "))
    if number > 20:
        print("that number is too high")
    elif number < 10:
        print("that number is too low")
    else:
        print("thank you")
