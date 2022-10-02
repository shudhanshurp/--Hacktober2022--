
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

input0 = [[3, 2, 5],
          [1, 7, 6],
          [8, 0, 4]]


def up(input0):

    for i in range(3):
        for j in range(3):
            if (input0[i][j] == 0):
                if (i == 0):
                    print("INVALID MOVES")
                else:
                    temp = input0[i-1][j]
                    input0[i-1][j] = 0
                    input0[i][j] = temp
                break
    for i in range(3):
        for j in range(3):
            print(input0[i][j], end=" ")
        print()
    return input0


def down(input0):

    for i in range(3):
        for j in range(3):

            if (input0[i][j] == 0):
                temp = input0[i-1][j]
                input0[i-1][j] = 0
                input0[i][j] = temp

    for i in range(3):
        for j in range(3):
            print(input0[i][j], end=" ")
        print()
    return input0


def left(input0):

    for i in range(3):
        for j in range(3):

            if (input0[i][j] == 0):
                if (j == 0):
                    print("INVALID MOVES")
                else:
                    temp = input0[i][j-1]
                    input0[i][j-1] = 0
                    input0[i][j] = temp
                break

    for i in range(3):
        for j in range(3):
            print(input0[i][j], end=" ")
        print()
    return input0


def right(input0):

    for i in range(3):
        for j in range(3):

            if (input0[i][j] == 0):
                if (j == 2):
                    print("INVALID MOVES")

                else:
                    temp = input0[i][j+1]
                    input0[i][j+1] = 0
                    input0[i][j] = temp
                break

    for i in range(3):
        for j in range(3):
            print(input0[i][j], end=" ")
        print()
    return input0


for i in range(3):
    for j in range(3):
        print(input0[i][j], end=" ")
    print()

while (input0 != goal):
    userinput = int(input("Enter production:"))

    if (userinput == 1):
        up(input0)

    elif (userinput == 2):
        down(input0)

    elif (userinput == 3):
        left(input0)

    elif (userinput == 4):
        right(input0)
