arr = [3, 4, 5, 1, 2, 2, 2]
target = 2


def search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (right + left) // 2
        print(mid)
        if target == arr[mid]:
            return mid

        # left sorted portion
        if arr[left] <= arr[mid]:
            if target > arr[mid] or target < arr[left]:
                left = mid + 1
            else:
                right = mid - 1
        # right sorted portion
        else:
            if target < arr[mid] or target > arr[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


print(search(arr, target))
