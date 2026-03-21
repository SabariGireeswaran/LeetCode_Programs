arr = []
arr_len = int(input("Enter the total number of elements in your array\n"))

for i in range(arr_len):
    arr.append(int(input(f"Enter the Number {i+1}\n")))

arr.sort()

result = []
for i in range(len(arr)):
    a = i

    for j in range(a+1, len(arr)):
        b = j

        for k in range(b+1, len(arr)):
            c = k

            A, B, C = arr[a], arr[b], arr[c]
            sum = A + B + C

            if sum==0 and sorted([A, B, C]) not in result:
                result.append(sorted([A, B, C]))
print(result)