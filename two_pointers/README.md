# Two Pointers 

The following questions, I prefer to solve by using Two Pointers. It may have the optimal method, please check the discussion in LeetCode.

* [Array](##Array)
* [String](##String)

## Array

Two pointers are really an easy and effective technique to solve many array related problems in place, especially in technical interviews. The array is one of the fundamental blocks in algorithms. This kind of problem usually involves two pointers: 1) one slow-runner and the other fast-runner, and 2) one pointer starts from the beginning while the other pointer starts from the end.

This type of problem includes: find the 3-4 sum in place problem, remove duplicates element in place problem, sort element in place problem， sliding window implementation (see Special Case)

The time complexity of this technique depends on the question.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 11 | https://leetcode.com/problems/container-with-most-water/ | [this link](../practice/solution/0011_container_with_most_water.py) |
| 15 | https://leetcode.com/problems/3sum/ | [this link](../practice/solution/0015_3sum.py) |
| 16 | https://leetcode.com/problems/3sum-closest/ | [this link](../practice/solution/0016_3sum_closest.py) |
| 18 | https://leetcode.com/problems/4sum/ | [this link](../practice/solution/0018_4sum.py) |
| 881 | https://leetcode.com/problems/boats-to-save-people/ | |
| 1099 | https://leetcode.com/problems/two-sum-less-than-k/ | [this link](../practice/solution/1099_two_sum_less_than_k.py) |
| 1099* | https://leetcode.com/discuss/interview-question/373202 | [this link](../practice/a/optimal_utilization.py) |
| 1229 | https://leetcode.com/problems/meeting-scheduler/ | |

## String

Since a string is just formed by an array of characters, they are both similar.

This type of problem includes: find partition in target string problem

The time complexity of this technique depends on the question.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 556 | https://leetcode.com/problems/next-greater-element-iii/ | |
| 696 | https://leetcode.com/problems/count-binary-substrings/ | [this link](../practice/solution/0696_count_binary_substrings.py) |
| 763 | https://leetcode.com/problems/partition-labels/ | [this link](../practice/solution/0763_partition_labels.py) |