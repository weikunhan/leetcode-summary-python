# Hash Map&Set

The following questions, I prefer to solve by using Heap Map&Set. It may have the optimal method, please check the discussion in LeetCode.  

* [Hash Map](##Hash-Map)
* [Hash Set](##Hash-Set)

## Hash Map

In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash map uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. In many situations, hash map turn out to be on average more efficient than search trees or any other table lookup structure. For this reason, they are widely used in many kinds of computer software, particularly for associative arrays, database indexing, caches, and sets. [Wikipedia](https://en.wikipedia.org/wiki/Hash_table)

The time complexity of the hash map is O(1) (Search O(1), Insert O(1), Delete O(1)), and the Space complexity of the hash map is O(n). 

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 13 | https://leetcode.com/problems/roman-to-integer/ | [this link](../practice/solution/0013_roman_to_integer.py) |
| 49 | https://leetcode.com/problems/group-anagrams/ | [this link](../practice/solution/0049_group_anagrams.py) |
| 187 | https://leetcode.com/problems/repeated-dna-sequences/ | |
| 219 | https://leetcode.com/problems/contains-duplicate-ii/ | |
| 220 | https://leetcode.com/problems/contains-duplicate-iii/ | |
| 451 | https://leetcode.com/problems/sort-characters-by-frequency/ | |
| 532 | https://leetcode.com/problems/k-diff-pairs-in-an-array/ | |
| 697 | https://leetcode.com/problems/degree-of-an-array/ | |
| 953 | https://leetcode.com/problems/verifying-an-alien-dictionary/ | |
| 963 | https://leetcode.com/problems/minimum-area-rectangle-ii/ | |
| 1138 | https://leetcode.com/problems/alphabet-board-path/ | |
| 1207 | https://leetcode.com/problems/unique-number-of-occurrences/ | |
| 1570 | https://leetcode.com/problems/dot-product-of-two-sparse-vectors/ | [this link](../practice/solution/1570_dot_product_of_two_sparse_vectors.py) |
| | https://leetcode.com/discuss/interview-question/373006 | [this link](../practice/amazon/favorite_genres.py) |
| | https://www.1point3acres.com/bbs/thread-580122-1-1.html | [this link](../practice/amazon/user_based_recommendation_system.py) |
| | https://www.1point3acres.com/bbs/thread-610975-1-1.html | [this link](../practice/tusimple/throttling_gateway.py) |

## Hash Set

A hash map is an implementation of Map. A Map maps keys to values. The key lookup occurs using the hash. On the other hand, a hash set is an implementation of Set. A Set is designed to match the mathematical model of a set. A hash set does use a HashMap to back its implementation. The hash set does not allow duplicate elements that mean you can not store duplicate values in the hash set. Hash set is quite useful when need verify some information is exists or been used, which can help reduce time complexity by checking in the hash set. 

Same as a hash map, the time complexity of the hash set is O(1) (Search O(1), Insert O(1), Delete O(1)), the Space complexity of the hash set is O(n).

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 36 | https://leetcode.com/problems/valid-sudoku/ | [this link](../practice/solution/0036_valid_sudoku.py) |
| 217 | https://leetcode.com/problems/contains-duplicate/ |[this link](../practice/solution/0217_contains_duplicate.py) |
| 564 | https://leetcode.com/problems/find-the-closest-palindrome/ | |
| 723 | https://leetcode.com/problems/candy-crush/ | |
| 734 | https://leetcode.com/problems/sentence-similarity/ | |
| 929 | https://leetcode.com/problems/unique-email-addresses/ | |
| 970 | https://leetcode.com/problems/powerful-integers/ | |
| 1044 | https://leetcode.com/problems/longest-duplicate-substring/ | |
