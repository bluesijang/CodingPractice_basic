from itertools import combinations, permutations


n = 5
arr = [3, 2, 1, 1, 9]
min = 1

result = [False] * 10000


# arr.sort()

for i in range(1, len(arr)+1):
    for row in combinations(arr, i):
        result[sum(row)] = True

for i in range(1, len(result)):
    if result[i] is False:
        print(i)
        break
