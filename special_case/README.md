# Special Case

The following questions, I prefer to solve by some not commonly used methods. If you interest more about those methods, please find more material about this method.

* [String Processing](##String-Processing)
* [Topological Sort](##Topological-Sort)
* [Binary Indexed Tree](##Binary-Indexed-Tree)
* [Prefix Tree](##Prefix-Tree)

## String-Processing

In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. [Wikipedia](https://en.wikipedia.org/wiki/String_(computer_science))

To solve this kind of problem, you need to familiar with: 1)sorting method/syntax, 2)split and join syntax, 3)encoding and decoding method/syntax, 4)regular expression 5)Unix utilities(optional)

| *#* | *Link* | *Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 937 | https://leetcode.com/problems/reorder-data-in-log-files/ | |


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