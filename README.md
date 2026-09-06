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

# Complexity

Time Complexity-O(m+n)
Space Complexity-O(1)
