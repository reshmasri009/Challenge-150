# remove element

def remove_element(nums,val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


nums=[22,57,68,57,49]
val=49
i = remove_element(nums,val)
print(i, nums[:i])
