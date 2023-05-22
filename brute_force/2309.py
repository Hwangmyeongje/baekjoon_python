array = []
for i in range(9):
    array.append(int(input()))
sum_a = sum(array)
array.sort()
rm1=0
rm2=0
for i in range(8):
    for j in range(i+1,9):
        if sum_a - (array[i] + array[j]) == 100:
            rm1=array[i]
            rm2=array[j]
            break
array.remove(rm1)
array.remove(rm2)
for i in array:
    print(i)
