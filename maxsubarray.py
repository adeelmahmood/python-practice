# Question: Find the Maximum Subarray Sum
# Problem Statement:
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum = 6.


def max_subarray(arr):
    current_sum, max_sum = arr[0], arr[0]
    subarray = [arr[0]]

    for num in arr[1:]:
        # current_sum = max(num, current_sum + num)
        if current_sum + num > num:
            subarray.append(num)
            current_sum += num
        else:
            # subarray = [num]
            current_sum = num
        # max_sum = max(max_sum, current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
            subarray = [num]

    print(subarray)
    return max_sum


print(max_subarray(nums))
