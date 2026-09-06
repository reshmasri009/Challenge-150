#Merge sorted arrays
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
def merge(nums1,m,nums2,n):

    last = m + n - 1

    while m>0 and n>0:
        if nums1[m-1]>nums2[n-1]:
            nums1[last]=nums1[m-1]
            m-=1
        else:
            nums1[last]=nums2[n-1]
            n-=1
        last-=1

    while n>0:
        nums1[last]=nums2[n-1]
        n-=1
        last -= 1
    return nums1


m = int(input("Enter number of valid elements in nums1 (m): "))
n = int(input("Enter number of elements in nums2 (n): "))

print("Enter nums1 elements (with extra 0s at the end):")
nums1 = list(map(int, input().split()))

print("Enter nums2 elements:")
nums2 = list(map(int, input().split()))

print("Before merge:", nums1)
result = merge(nums1, m, nums2, n)
print("After merge:", result)
