# 기준 data 설정[0] (pivot 값), 기준 보다 큰 data(오른쪽부터)와 작은 data(왼쪽부터)의 위치를 바꿈
# 큰 값과 작은 값이 cross 되는 부분에서 [0] 값과 cross 된 값[j]의 위치를 바꿔줌
#  => 왼쪽은 pivot 값보다 작은값이 되고, 오른쪽은 pivot값보다 큰 값들이 모이게 됨 (=> 분할이라 함)
#  => 왼쪽 data 묶음으로 다시 정렬 수행 (오른쪽도..) : recursive


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quicksort(array):

    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x < pivot]
    right_side = [x for x in tail if x >= pivot]

    return quicksort(left_side) + [pivot] + quicksort(right_side)


print(quicksort(array))
