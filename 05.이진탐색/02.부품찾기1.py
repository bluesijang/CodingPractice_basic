from cv2 import RETR_CCOMP


n = 5
arr1 = [8, 3, 7, 9, 2]

m = 3
arr2 = [5, 7, 9]


def bin_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return bin_search(arr, target, mid+1, end)
    else:
        return bin_search(arr, target, start, mid-1)


arr1.sort()
print(f"arr1 {arr1}")
print(f"arr2 {arr2}")

for i in arr2:
    if bin_search(arr1, i, 0, len(arr1)-1) != None:
        print("Yes", end=' ')
    else:
        print("No", end=' ')
