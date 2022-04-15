# n = int(input())

arr = [1, 2, 3, 5, 10, 11, 15, 18, 22, 23,
       26, 31, 33, 34, 35, 36, 39, 40, 45, 49]

# value for looking
n = 11

print(f"Value for looking : {n}")


def bin_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return bin_search(arr, target, mid + 1, end)
    else:
        return bin_search(arr, target, start, mid - 1)


result = bin_search(arr, n, 0, len(arr)-1)

if result == None:
    print("해당 값이 없습니다.")
else:
    print(f"index [{result}]에 값 {n}이 있습니다.")
