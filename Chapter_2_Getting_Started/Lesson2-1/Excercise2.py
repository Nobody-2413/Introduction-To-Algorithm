# Create a insertion sort algorithm that sort the list from greatest to least
def insertionSort(nums):
    for i in range(len(nums) - 2, 0, -1):
        key = nums[i]
        j = i + 1
        while j < len(nums) and nums[j] > key:
            nums[j - 1] = nums[j]
            j += 1
        nums[j - 1] = key
    return nums

print(insertionSort([5, 2, 4, 6, 1, 3]))