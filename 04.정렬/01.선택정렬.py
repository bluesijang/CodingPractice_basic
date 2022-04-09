# 선택정렬
# 제일 앞 값과, 뒤쪽(for loop) 값들을 비교하며 변경

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print(array)
