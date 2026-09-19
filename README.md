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






