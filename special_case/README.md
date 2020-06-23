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
| 1 | https://leetcode.com/problems/two-sum/ | [this link](../practice/solution/0001_two_sum.py) |
| 1* | https://leetcode.com/discuss/interview-question/356960 | [this link](../practice/amazon/find_pair_with_given_sum.py) |
| 1* | https://leetcode.com/discuss/interview-question/372434 | [this link](../practice/amazon/two_sum_unique_pairs.py) |
| 167 | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ | |
| 454 | https://leetcode.com/problems/4sum-ii/ | |

## Sliding Window

Sliding Window problem is a variation of Two Pointers. The main difference between with Two Pointers is that Sliding Window usually requires a hash table to count occurrence times. Therefore, for some situations, the Sliding window is reduced complexity compared with directly using Two Pointers. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 3 | https://leetcode.com/problems/longest-substring-without-repeating-characters/ | [this link](../practice/solution/0003_longest_substring_without_repeating_characters.py) |
| 76 | https://leetcode.com/problems/minimum-window-substring/ | |
| 438 | https://leetcode.com/problems/find-all-anagrams-in-a-string/ | |
| 992 | https://leetcode.com/problems/subarrays-with-k-different-integers/ | |
| 992* | https://leetcode.com/discuss/interview-question/370157 | [this link](../practice/amazon/substrings_with_exactly_k_distinct_chars.py) |
| 995 | https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/ | |
| 1100 | https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/ | |
| 1052 | https://leetcode.com/problems/grumpy-bookstore-owner/ | |

## Math

There are few problems are related to mathematical. You should familiar with common methods to play mathematical in computer science. For example, to identify whether a natural number is a prime number, just look at whether it is from 2 to the root N (forgive me for expressing this) whether it can be divided by N.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 7 | https://leetcode.com/problems/reverse-integer/ | [this link](../practice/solution/0007_reverse_integer.py)|
| 69 | https://leetcode.com/problems/sqrtx/ | |
| 289 | https://leetcode.com/problems/game-of-life/ | |
| 365 | https://leetcode.com/problems/water-and-jug-problem/ | |
| 367 | https://leetcode.com/problems/valid-perfect-square/ | |
| 461 | https://leetcode.com/problems/hamming-distance/ | |
| 477 | https://leetcode.com/problems/total-hamming-distance/ | |
| 492 | https://leetcode.com/problems/construct-the-rectangle/ | |
| 633 | https://leetcode.com/problems/sum-of-square-numbers/ | |
| 650 | https://leetcode.com/problems/2-keys-keyboard/ | |
| 780 | https://leetcode.com/problems/reaching-points/ | [this link](../practice/solution/0780_reaching_points.py) |
| 794 | https://leetcode.com/problems/valid-tic-tac-toe-state/ | |
| 866 | https://leetcode.com/problems/prime-palindrome/ | |
| 991 | https://leetcode.com/problems/broken-calculator/ | |
| 1131 | https://leetcode.com/problems/maximum-of-absolute-value-expression/ | |
| 1175 | https://leetcode.com/problems/prime-arrangements/ | |
| 1185 | https://leetcode.com/problems/day-of-the-week/ | |
| 1275 |https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/ | |
| 1344 | https://leetcode.com/problems/angle-between-hands-of-a-clock/ | |
| 1360 | https://leetcode.com/problems/number-of-days-between-two-dates/ | |

## Prefix Tree

In computer science, a trie, also called digital tree or prefix tree, is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings. [Wikipedia](https://en.wikipedia.org/wiki/Trie)

To solve this kind of problem, you need to build a trie. the core content to build trie: 1) insert function, 2) search function. Please prepare the template for this kind of problem. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 212 | https://leetcode.com/problems/word-search-ii/ | |
| 425 | https://leetcode.com/problems/word-squares/ | |
| 720 | https://leetcode.com/problems/longest-word-in-dictionary/ | |
| 1268 | https://leetcode.com/problems/search-suggestions-system/ | [this link](../practice/solution/1268_search_suggestions_system.py)| 

## Greedy

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the intent of finding a global optimum. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time. [Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 41 | https://leetcode.com/problems/first-missing-positive/ | |
| 45 | https://leetcode.com/problems/jump-game-ii/ | |
| 55 | https://leetcode.com/problems/jump-game/ | |
| 122 | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ | |
| 252 | https://leetcode.com/problems/meeting-rooms/ | |
| 253 | https://leetcode.com/problems/meeting-rooms-ii/ | |
| 321 | https://leetcode.com/problems/create-maximum-number/ | |
| 759 | https://leetcode.com/problems/employee-free-time/ | |
| 860 | https://leetcode.com/problems/lemonade-change/ | |
| 1029 | https://leetcode.com/problems/two-city-scheduling/ | |

## Topological Sort

In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of all vertices of a directed acyclic graph (its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering) [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)

To solve this kind of problem, you need two steps: 1)initial graph, 2)prune graph

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 207 | https://leetcode.com/problems/course-schedule/ | |
| 210 | https://leetcode.com/problems/course-schedule-ii/ | [this link](../practice/solution/0210_course_schedule_ii.py)|
| 269 | https://leetcode.com/problems/alien-dictionary/ | |
| 310 | https://leetcode.com/problems/minimum-height-trees/ | |

## Binary Indexed Tree

A Fenwick tree or binary indexed tree is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers. [Wikipedia](https://en.wikipedia.org/wiki/Fenwick_tree)

For my understanding, the binary indexed tree is another evolution from divided DP. However, when you want to change the preprocessing sum in divided DP, it takes O(n) time, which is not efficient in some cases. Then you may need to choose the binary indexed tree. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 307 | https://leetcode.com/problems/range-sum-query-mutable/ | |