# Special Case

The following questions, I prefer to solve by some not commonly used methods. If you interest more about those methods, please find more material about this method.

* [Two Sum](##Two-Sum)
* [String Processing](##String-Processing)
* [Prefix Tree](##Prefix-Tree)
* [Topological Sort](##Topological-Sort)
* [Binary Indexed Tree](##Binary-Indexed-Tree)

## Two-Sum

Two sum problem is a variation of the subset sum problem which is interval-DP. Or, even simply it can solve using two pointers in some situations. I would like to make two sum problems as a special case because there is a faster algorithm that will find pairs that sum to S in linear time. The algorithm below makes use of hash tables which have a constant lookup time.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 1 | https://leetcode.com/problems/two-sum/ | |
| 167 | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ | |
| 1* | https://leetcode.com/discuss/interview-question/356960 | [this link](../python_practice/amazon/find_pair_with_given_sum.py) |
| 1* | https://leetcode.com/discuss/interview-question/372434 | [this link](../python_practice/amazon/two_sum_unique_pairs.py) |

## String-Processing

In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. [Wikipedia](https://en.wikipedia.org/wiki/String_(computer_science))

To solve this kind of problem, you need to familiar with: 1)sorting method/syntax, 2)split and join syntax, 3)encoding and decoding method/syntax, 4)regular expression, 5)hash mapping, 6)Unix utilities(optional)

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 937 | https://leetcode.com/problems/reorder-data-in-log-files/ | |
| | https://leetcode.com/discuss/interview-question/373006| [this link](../python_practice/amazon/favorite_genres.py) |


## Prefix-Tree

In computer science, a trie, also called digital tree or prefix tree, is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings. [Wikipedia](https://en.wikipedia.org/wiki/Trie)

To solve this kind of problem, you need two steps: 1)initial trie, 2)query trie.

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 208 | https://leetcode.com/problems/implement-trie-prefix-tree/ | |
| 1268 | https://leetcode.com/problems/search-suggestions-system/ | | 
| 425 | https://leetcode.com/problems/word-squares/ | |
| 642 | https://leetcode.com/problems/design-search-autocomplete-system/ | |

## Topological-Sort

In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)

To solve this kind of problem, you need two steps: 1)initial graph, 2)prune graph

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 207 | https://leetcode.com/problems/course-schedule/ | |
| 210 | https://leetcode.com/problems/course-schedule-ii/ | |
| 310 | https://leetcode.com/problems/minimum-height-trees/ | |

## Binary-Indexed-Tree

A Fenwick tree or binary indexed tree is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers. [Wikipedia](https://en.wikipedia.org/wiki/Fenwick_tree)

For my understanding, the binary indexed tree is another evolution from divided DP. However, when you want to change the preprocessing sum in divided DP, it takes O(n) time, which is not efficient in some cases. Then you may need to choose the binary indexed tree. 

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 307 | https://leetcode.com/problems/range-sum-query-mutable/ | |