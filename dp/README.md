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
| 688 | https://leetcode.com/problems/knight-probability-in-chessboard/

## Sequential DP

This type of problem includes: find the longest/shortest common sequence problem, find the longest/shortest increase/decreasing sequence problem, 

For this kind of question, you need to use 1D DP array to transfer state when dealing with comparison

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 821 | https://leetcode.com/problems/shortest-distance-to-a-character/ | |

## Bidirectional Sequence DP

This type of problem includes: find longest/shortest palindromic sequence problem

For this kind of question, you need to use 2D DP array to transfer state when dealing with comparison

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 5 | https://leetcode.com/problems/longest-palindromic-substring/ | |

## Interval DP

This type of problem includes: find the subset problem， find word break problem

For this kind of question, you need to enumerate the left and right subranges and record the sata into into 1D or 2D DP array.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 368 | https://leetcode.com/problems/largest-divisible-subset/ | |
| 139 | https://leetcode.com/problems/word-break/ | |
| 140 | https://leetcode.com/problems/word-break-ii/ | |

## Divided DP

This type of problem includes: find the area sum problem

For this kind of question, you need to preprocess calculate the sum into 1D or 2D DP array.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 304 | https://leetcode.com/problems/range-sum-query-2d-immutable/ |
| 221 | https://leetcode.com/problems/maximal-square/ |

## Knapsack DP

This type of problem includes: find 0-1 knapsack problem, find unbound knapsack problem, find bounded knapsack problem, find multi-objective knapsack problem, find multi-dimensional knapsack problem, find multiple knapsack problem, find quadratic knapsack problem

For this kind of quesiton, you need to know what is knapsack problem: a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 474 | https://leetcode.com/problems/ones-and-zeroes/ | |

## Comprehensive DP

This type of problem includes: find the matrix multiplication problem, find the fibonacci sequence problem, find the catalan number problem

For this kind of question, you need to famillar with basic math knowlegae.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 70 | https://leetcode.com/problems/climbing-stairs/ | |
| 96 | https://leetcode.com/problems/unique-binary-search-trees/ | |
| 311 | https://leetcode.com/problems/sparse-matrix-multiplication/ | |