# Hash Map&Set

The following questions, I prefer to solve by using Heap Map&Set. It may have the optimal method, please check the discussion in LeetCode.  

* [Hash Map](##Hash-Map)
* [Hash Set](##Hash-Set)

## Hash Map

This structure that can map keys to values. A hash map uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. In many situations, hash map turn out to be on average more efficient than search trees or any other table lookup structure. For this reason, they are widely used in many kinds of computer software, particularly for associative arrays, database indexing, caches, and sets.

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 49 | https://leetcode.com/problems/group-anagrams/ | |
| 451 | https://leetcode.com/problems/sort-characters-by-frequency/ | |
| 953 | https://leetcode.com/problems/verifying-an-alien-dictionary/ | |
| 1138 | https://leetcode.com/problems/alphabet-board-path/ | |
| 1152 | https://leetcode.com/problems/analyze-user-website-visit-pattern/ | |
| 1207 | https://leetcode.com/problems/unique-number-of-occurrences/ | |
| | https://leetcode.com/discuss/interview-question/373006| [this link](../python_practice/amazon/favorite_genres.py) |

## Hash Set

Hash Set is little bit difference than Hash Map, but the underlying Hash storage mechanism is exactly the same, even Hash Set itself is implemented using Hash Map. There are many similarities between Hash Set and Hash Map. For Hash Set, the system uses the hash algorithm to determine the storage location of the collection elements, which can ensure that the collection elements can be quickly stored and retrieved; for Hash Map, the system key-value is regarded as a whole for processing, the system always calculates the key-value storage location according to the hash algorithm, which can ensure that the key-value pairs of the map can be quickly stored and retrieved.

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 929 | https://leetcode.com/problems/unique-email-addresses/ | |