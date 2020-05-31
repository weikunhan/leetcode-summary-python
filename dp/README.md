# Dynamic Programming

The following questions, I prefer to solve by using DP. It may have the optimal method, please check the discussion in LeetCode. When you try to come up a DP solution, you need to know 4 things: 1)state, 2)function, 3)initialization, 4)answer

* [Coordinate DP](##Coordinate-DP) 
* [Sequential DP](##Sequential-DP)
* [Bidirectional Sequence DP](##Bidirectional-Sequence-DP)
* [Interval DP](##Interval-DP)
* [Divided DP](##Divided-DP)
* [Knapsack DP](##Knapsack-DP)
* [Comprehensive DP](##Comprehensive-DP)
* [Game type DP](##Game-type-DP)

## Coordinate DP

This type of problem includes: find status in the checkerboard problem

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 64 | https://leetcode.com/problems/minimum-path-sum/ | |
| 688 | https://leetcode.com/problems/knight-probability-in-chessboard/| |

## Sequential DP

This type of problem includes: find the longest/shortest common sequence problem, find the longest/shortest increase/decreasing sequence problem, find egg drop problem

For this kind of question, you need to use 1D DP array to transfer state when dealing with comparison

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 53 | https://leetcode.com/problems/maximum-subarray/ | |
| 91 | https://leetcode.com/problems/decode-ways/ | |
| 121 | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ | |
| 123 | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/ | |
| 135 | https://leetcode.com/problems/candy/ | |
| 152 | https://leetcode.com/problems/maximum-product-subarray/ | |
| 309 | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/ | |
| 821 | https://leetcode.com/problems/shortest-distance-to-a-character/ | |
| 978 | https://leetcode.com/problems/longest-turbulent-subarray/ | |

## Bidirectional Sequence DP

This type of problem includes: find longest/shortest palindromic sequence problem

For this kind of question, you need to use 2D DP array to transfer state when dealing with comparison

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 5 | https://leetcode.com/problems/longest-palindromic-substring/ | [this link](../practice/solution/0005_longest_palindromic_substring.py) |
| 72 | https://leetcode.com/problems/edit-distance/ | |
| 97 | https://leetcode.com/problems/interleaving-string/ | |
| 887 | https://leetcode.com/problems/super-egg-drop/ | |
| 1035 | https://leetcode.com/problems/uncrossed-lines/ | |
| 1143 | https://leetcode.com/problems/longest-common-subsequence/ | |

## Interval DP

This type of problem includes: find the subset problem，find word break problem

For this kind of question, you need to enumerate the left and right subranges and record the state into into 1D or 2D DP array.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 139 | https://leetcode.com/problems/word-break/ | |
| 140 | https://leetcode.com/problems/word-break-ii/ | |
| 368 | https://leetcode.com/problems/largest-divisible-subset/ | |

## Divided DP

This type of problem includes: find the area sum problem

For this kind of question, you need to preprocess calculate the sum into 1D or 2D DP array.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 221 | https://leetcode.com/problems/maximal-square/ |
| 304 | https://leetcode.com/problems/range-sum-query-2d-immutable/ |

## Knapsack DP

This type of problem includes: find 0-1 knapsack problem, find unbound knapsack problem, find bounded knapsack problem, find multi-objective knapsack problem, find multi-dimensional knapsack problem, find multiple knapsack problem, find quadratic knapsack problem

For this kind of quesiton, you need to know what is knapsack problem: a problem in combinatorial optimization: given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 120 | https://leetcode.com/problems/triangle/ | |
| 322 | https://leetcode.com/problems/coin-change/ | |
| 474 | https://leetcode.com/problems/ones-and-zeroes/ | |
| 1155 | https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/ | |

## Comprehensive DP

This type of problem includes: find the matrix multiplication problem, find the fibonacci sequence problem, find the catalan number problem

For this kind of question, you need to famillar with basic math knowlegae.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 70 | https://leetcode.com/problems/climbing-stairs/ | |
| 96 | https://leetcode.com/problems/unique-binary-search-trees/ | |
| 311 | https://leetcode.com/problems/sparse-matrix-multiplication/ | |
| 509 | https://leetcode.com/problems/fibonacci-number/ | |

## Game-type DP

This type of problem includes: life game-type problem, math game-type problem, policy game-type problem, others game-type problem

For this kind of question, there is a common point that the problem is talking about the comparison or execution sequence.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 486 | https://leetcode.com/problems/predict-the-winner/ | |
| 1048 | https://leetcode.com/problems/longest-string-chain/ | |
| 1153 | https://leetcode.com/problems/string-transforms-into-another-string/ | |
