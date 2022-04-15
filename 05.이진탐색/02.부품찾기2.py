n = 5
source = [8, 3, 7, 9, 2]

m = 3
wanted = [5, 7, 9]

array = [0] * 100000

for i in source:
    array[i] = 1


for x in wanted:
    if array[x] == 1:
        print("Yes", end=' ')
    else:
        print("No", end=" ")
