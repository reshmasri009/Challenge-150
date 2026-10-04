#Remove duplicates from sorted array II

def removeDuplicates(nums):
    if not nums:
        return 0
    i = 1
    count = 1
    for j in range(1,len(nums)):
        if nums[j] == nums[j-1]:
            count += 1
        else:
            count = 1
        if count <= 2:
            nums[i] = nums[j]
            i += 1
        return i


nums = [23,45,23,23,45,67,56]
print(removeDuplicates(nums))




    