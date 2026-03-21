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


n = int(input("Enter the number of rows:"))
pattern2(n)
pattern3(n)
pattern4(n)