# Special Case

The following questions, I prefer to solve by some not commonly used methods. If you interest more about those methods, please find more material about this method.

* [Two Sum](##Two-Sum)
* [Sliding Window](##Sliding-Window)
* [Math](##Math)
* [Prefix Tree](##Prefix-Tree)
* [Greedy](##Greedy)
* [Topological Sort](##Topological-Sort)
* [Binary Indexed Tree](##Binary-Indexed-Tree)

## Two Sum

Two Sum related problems can simply solve using Two Pointers. I would like to make Two Sum problems as a special case because there is a faster algorithm that will find pairs that sum to target value in linear time. The algorithm is using a hash map to mapping target value with index which have a constant lookup time.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 1 | https://leetcode.com/problems/two-sum/ | |
| 167 | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ | |
| 1* | https://leetcode.com/discuss/interview-question/356960 | [this link](../python_practice/amazon/find_pair_with_given_sum.py) |
| 1* | https://leetcode.com/discuss/interview-question/372434 | [this link](../python_practice/amazon/two_sum_unique_pairs.py) |

## Sliding Window

Sliding Window problem is a variation of Two Pointers. The main difference between with Two Pointers is that Sliding Window usually requires a hash table to count occurrence times. Therefore, for some situations, the Sliding window is reduced complexity compared with directly using Two Pointers. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 992 | https://leetcode.com/problems/subarrays-with-k-different-integers/ | |
| 76 | https://leetcode.com/problems/minimum-window-substring/ | |
| 992* | https://leetcode.com/discuss/interview-question/370157 | [this link](../python_practice/amazon/substrings_with_exactly_k_distinct_chars.py) |

## Math

There are few problems are related to mathematical. You should familiar with common methods to play mathematical in computer science. For example, to identify whether a natural number is a prime number, just look at whether it is from 2 to the root N (forgive me for expressing this) whether it can be divided by N.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 866 | https://leetcode.com/problems/prime-palindrome/ | |
| 461 | https://leetcode.com/problems/hamming-distance/ | |
| 477 | https://leetcode.com/problems/total-hamming-distance/ | |
| 367 | https://leetcode.com/problems/valid-perfect-square/ | |
| 69 | https://leetcode.com/problems/sqrtx/ | |
| 633 | https://leetcode.com/problems/sum-of-square-numbers/ | |
| 991 | https://leetcode.com/problems/broken-calculator/ | |

## Prefix Tree

In computer science, a trie, also called digital tree or prefix tree, is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings. [Wikipedia](https://en.wikipedia.org/wiki/Trie)

To solve this kind of problem, you need to build a trie. the core content to build trie: 1) insert function, 2) search function. Please prepare the template for this kind of problem. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 1268 | https://leetcode.com/problems/search-suggestions-system/ | | 
| 720 | https://leetcode.com/problems/longest-word-in-dictionary/ | |
| 425 | https://leetcode.com/problems/word-squares/ | |
| 212 | https://leetcode.com/problems/word-search-ii/ | |

## Greedy

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the intent of finding a global optimum. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time. [Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 253 | https://leetcode.com/problems/meeting-rooms-ii/ | |

## Topological Sort

In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of all vertices of a directed acyclic graph (its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering) [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)

To solve this kind of problem, you need two steps: 1)initial graph, 2)prune graph

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 207 | https://leetcode.com/problems/course-schedule/ | |
| 210 | https://leetcode.com/problems/course-schedule-ii/ | |
| 310 | https://leetcode.com/problems/minimum-height-trees/ | |

## Binary Indexed Tree

A Fenwick tree or binary indexed tree is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers. [Wikipedia](https://en.wikipedia.org/wiki/Fenwick_tree)

For my understanding, the binary indexed tree is another evolution from divided DP. However, when you want to change the preprocessing sum in divided DP, it takes O(n) time, which is not efficient in some cases. Then you may need to choose the binary indexed tree. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 307 | https://leetcode.com/problems/range-sum-query-mutable/ | |