userSize = int(input("Enter the size of the pattern: "))

row = 0

while row < userSize:  
    for col in range(userSize):
        print("*", end="")
    print()  
    row += 1