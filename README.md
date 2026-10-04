# Challenge-150
 This repository is dedicated to solving the **Top 150 LeetCode Questions**.   The goal is to build strong problem-solving skills in DSA.  Objectives - Solve the most frequently asked 150 LeetCode problems. - Practice writing efficient, beginner-friendly, and well-explained solutions.  - Strengthen coding foundations in Python


*****************************************************************************************************************************************
Challenge 1
# Merge Sorted Array

Approach
- Start filling `nums1` from the end (`last = m + n - 1`).
- Compare the last valid elements of `nums1` and `nums2`.
- Place the larger element at the `last` index.
- Decrement pointers (`m`, `n`, `last`) accordingly.
- If any elements remain in `nums2`, copy them into `nums1`.

This ensures in-place merging without extra space

 Complexity

Time Complexity-O(m+n)
Space Complexity-O(1)

******************************************************************************************************************************************
Challenge 2

# Remove elements

Approach
-Traverse the array once.
-Compare each element with the target value
-If it is not equal,keep it in the result.
-Return the new array.

Compplexity

Time Complexity-O(n)
Space Complexity-O(n)

******************************************************************************************************************************************

Challenge 3

# Remove duplicates from sorted array

Approach
-Sort the array first (so duplicates are adjacent).
-Use two pointers:
-i = position of last unique element.
-j = scanning pointer.
-If arr[j] != arr[i], move i forward and overwrite arr[i] with arr[j].
-Return the array up to index i.

Complexity

Time: O(n log n) 
Space: O(1)

*******************************************************************************************************************************************

Challenge 4

# Remove duplicates from sorted array-II

Approach
-Use two pointers:
i → tracks the position of the last unique element.
j → scans through the array.
-Start with i = 0.
For each j from 1 to end:
-If arr[j] != arr[i], move i forward and set arr[i] = arr[j].
-At the end, the array up to index i contains all unique elements.

Complexity

Time : O(n)
Space : O(1)

*************************************************************************************************************************************************

Challenge 5

# Merge elements

Approach
-Use three pointers:
p1 = m - 1 → last valid element in nums1.
p2 = n - 1 → last element in nums2.
p = m + n - 1 → last index of nums1.
-Compare nums1[p1] and nums2[p2]:
Place the larger one at nums1[p].
-Move the pointer backward.
-Continue until one array is exhausted.
-If nums2 still has elements, copy them into nums1.

Complexity
Time :O(m+n)
Space : O(1)

****************************************************************************************************************************************************

Challenge 6

# Rotate Array

Approach
array[n-k:] → last k elements (these move to the front).
array[:n-k] → first n-k elements (these shift to the back).
-Concatenate them → rotated array.

Complexity
Time:O(n)
Space:O(n)

*****************************************************************************************************************************************************

Challenge 7

# Best time to buy and sell products

Aprroach
-Track the minimum price seen so far.
-At each step, calculate the profit if you sold today (current_price - min_price).
-Update the maximum profit if this profit is larger.

Complexity
Time:O(n)
Space:O(1)







