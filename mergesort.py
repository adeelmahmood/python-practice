def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge(left_list, right_list)


def merge(left, right):
    li = 0
    ri = 0
    sorted = []

    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            sorted.append(left[li])
            li += 1
        else:
            sorted.append(right[ri])
            ri += 1

    sorted.extend(left[li:])
    sorted.extend(right[ri:])

    return sorted


unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)  # Output should be [3, 9, 10, 27, 38, 43, 82]
