

rows = int(input("enter amount of rows"))
columns = int(input("enter amount of columns"))

for row in range(rows):
    line = str()
    for column in range(columns):
        line = line + "*"
    print(line)
        
