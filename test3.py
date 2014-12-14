

number = 0

data = int(input("Please enter an number"))
except ValueError:
    print("That is not a valid number")

while number <= data:
    number += 1
    square =((number) ** 2)
    print(square, end=" " )
