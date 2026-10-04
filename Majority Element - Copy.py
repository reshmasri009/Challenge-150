#Majority element

def majorityElement(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num] = 1
    for key in count:
        if count[key] >= len(nums) // 2:
            return key
    

nums = [34,56,78,34,34,56,78,34]
print(majorityElement(nums))