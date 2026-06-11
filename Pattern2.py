def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end = " ")
        print()

def pattern3(n):
    for i in range(1, n + 1):
        for j in range(1,i+1):
            print(j, end = " ")
        print()

def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print(i + 1, end = " ")
        print()

def pattern5(n):
    for i in range(1, n+1):
        left = ((2*n) // 2) - i
        center = 2*i - 1
        right = ((2*n) // 2) - i
        # print(left, center, right)

        for k in range(left):
            print(" ", end="")
        for l in range(center):
            print("*", end="")
        for m in range(right):
            print(" ", end="")
        print()
    return 

def pattern6(n):
    for i in range(n):
        for j in range(i+1):
            print(j, end=" ")
        print()

n = int(input("Enter the number of rows:"))
pattern6(n)