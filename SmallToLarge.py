n = int(input())
array = []

for i in range(n) :
    array.append(float(input()))

for j in range(n-1) :

    if array[j] > array[j+1] :
        print("Array values ​​are not sorted from small to large")
        break

    if j == n-2 :
        print("Array values ​​are sorted from small to large")