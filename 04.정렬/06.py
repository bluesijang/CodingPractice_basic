n, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1_sorted = sorted(arr1, reverse=True)
arr2_sorted = sorted(arr2, reverse=True)

max_sum = sum(arr1_sorted[:n-k]) + sum(arr2_sorted[:k])

print(max_sum)
