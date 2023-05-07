#!/usr/bin/env python
# coding: utf-8

def quicksort(array, start, end):
    # 如果 start >= end，表示已經完成排序
    if start >= end:
        return

    # 選擇第一個元素為 pivot
    pivot = array[start]
    left = start + 1
    right = end

    while left <= right:
        # 向右尋找第一個比 pivot 大的元素
        while left <= end and array[left] < pivot:
            left += 1

        # 向左尋找第一個比 pivot 小的元素
        while right > start and array[right] >= pivot:
            right -= 1

        # 如果 left 和 right 沒有相遇，則交換它們對應的元素
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    # 將 pivot 放到分割線的位置上
    array[start], array[right] = array[right], array[start]

    # 遞迴排序分割線左側的子陣列和右側的子陣列
    quicksort(array, start, right - 1)
    quicksort(array, right + 1, end)

    # 印出排序過程
    print("排序中的序列：", array[start:end+1])

# 原始陣列
array = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

print("原始陣列：", array)

# 呼叫快速排序函數並列印排序結果
quicksort(array, 0, len(array) - 1)
print("排序後的陣列：", array)


# In[ ]:




