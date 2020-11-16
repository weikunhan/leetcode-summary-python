# Binary Search

The following questions, I prefer to solve by using Binary Search. It may have the optimal method, please check the discussion in LeetCode.

* [2D Array](##2D-Array)
* [Array](##Array)

## Array

In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.[Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

This type of problem includes: search target value in sorted array problem, search target value in sorted rotated array problem, find longest increasing subsequence problem (patience sorting)

The time complexity of the binary seasrch in sorted array is O(log(n)

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 4 | https://leetcode.com/problems/median-of-two-sorted-arrays/ | [this link](../practice/solution/0004_median_of_two_sorted_arrays.py)|
| 33 | https://leetcode.com/problems/search-in-rotated-sorted-array/ | [this link](../practice/solution/0033_search_in_rotated_sorted_array.py) |
| 81 | https://leetcode.com/problems/search-in-rotated-sorted-array-ii/ | [this link](../practice/solution/0081_search_in_rotated_sorted_array_ii.py) |
| 153 | https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ | [this link](../practice/solution/0153_find_minimum_in_rotated_sorted_array.py) |
| 300 | https://leetcode.com/problems/longest-increasing-subsequence/ | [this link](../practice/solution/0300_longest_increasing_subsequence.py) |
| 410 | https://leetcode.com/problems/split-array-largest-sum/ | |
| 540 | https://leetcode.com/problems/single-element-in-a-sorted-array/ | [this link](../practice/solution/0540_single_element_in_a_sorted_array.py) |
| 704 | https://leetcode.com/problems/binary-search/ | [this link](../practice/solution/0704_binary_search.py) |
| 1060 | https://leetcode.com/problems/missing-element-in-sorted-array/ | |
| 1011 | https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/ | |
| 1044 | https://leetcode.com/problems/longest-duplicate-substring/ | [this link](../practice/solution/1044_longest_duplicate_substring.py) |

## 2D Array

This type of problem includes: search target value in sorted 2D-array problem, search target value in special sorted 2D-array problem

The time complexity of the binary seasrch in sorted 2D array is O(log(n)

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 74 | https://leetcode.com/problems/search-a-2d-matrix/ | [this link](../practice/solution/0074_search_a_2d_matrix.py) |
| 240 | https://leetcode.com/problems/search-a-2d-matrix-ii/ | [this link](../practice/solution/0240_search_a_2d_matrix_ii.py) |