# Basic Data Structures

The data structures you should know before starting coding in LeetCode:

* Array
* Linked List
* Stack
* Queue
* Binary Tree
* Binary Search Tree
* Red-Black Tree
* Heap
* Hash Table
* Graph
* Advanced Data Structure

For more information, you need to check related courses and books. Here, most basic data structures are:

* [Array](##Array)
* [Linked List](##Linked-List)
* [String (Not a data structure)](##String)

## Array

In computer science, an array data structure, or simply an array, is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. An array is stored such that the position of each element can be computed from its index tuple by a mathematical formula. The simplest type of data structure is a linear array, also called one-dimensional array. For example, an array of 10 32-bit (4-byte) integer variables, with indices 0 through 9, may be stored as 10 words at memory addresses 2000, 2004, 2008, ..., 2036, so that the element with index i has the address 2000 + (i × 4). The memory address of the first element of an array is called first address, foundation address, or base address. Because the mathematical concept of a matrix can be represented as a two-dimensional grid, two-dimensional arrays are also sometimes called matrices. In some cases the term "vector" is used in computing to refer to an array, although tuples rather than vectors are the more mathematically correct equivalent. Tables are often implemented in the form of arrays, especially lookup tables; the word table is sometimes used as a synonym of array. Arrays are among the oldest and most important data structures, and are used by almost every program. They are also used to implement many other data structures, such as lists and strings. They effectively exploit the addressing logic of computers. In most modern computers and many external storage devices, the memory is a one-dimensional array of words, whose indices are their addresses. Processors, especially vector processors, are often optimized for array operations. Arrays are useful mostly because the element indices can be computed at run time. Among other things, this feature allows a single iterative statement to process arbitrarily many elements of an array. For that reason, the elements of an array data structure are required to have the same size and should use the same data representation. The set of valid index tuples and the addresses of the elements (and hence the element addressing formula) are usually, but not always,fixed while the array is in use. [Wikipedia](https://en.wikipedia.org/wiki/Array_data_structure)

For programming practice, you need to know how to: 1)iterate through 1D array, 2)iterate through 2D array, 3)play tricks using different programming languages, 4)understand bit manipulation

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 14 | https://leetcode.com/problems/longest-common-prefix/ | [this link](../practice/solution/0014_longest_common_prefix.py) |
| 54 | https://leetcode.com/problems/spiral-matrix/ | [this link](../practice/solution/0054_spiral_matrix.py) |
| 56 | https://leetcode.com/problems/merge-intervals/ | [this link](../practice/solution/0056_merge_intervals.py) |
| 57 | https://leetcode.com/problems/insert-interval/ | [this link](../practice/solution/0057_insert_interval.py) |
| 59 | https://leetcode.com/problems/spiral-matrix-ii/ | [this link](../practice/solution/0059_spiral_matrix_ii.py) |
| 238 | https://leetcode.com/problems/product-of-array-except-self/ | [this link](../practice/solution/0238_product_of_array_except_self.py) |
| 252 | https://leetcode.com/problems/meeting-rooms/ | [this link](../practice/solution/0252_meeting_rooms.py) |
| 253 | https://leetcode.com/problems/meeting-rooms-ii/ | [this link](../practice/solution/0253_meeting_rooms_ii.py) |
| 277 | https://leetcode.com/problems/find-the-celebrity/ | [this link](../practice/solution/0277_find_the_celebrity.py) |
| 605 | https://leetcode.com/problems/can-place-flowers/ | [this link](../practice/solution/0605_can_place_flowers.py) |
| 628 | https://leetcode.com/problems/maximum-product-of-three-numbers/ | [this link](../practice/solution/0628_maximum_product_of_three_numbers.py) |
| 759 | https://leetcode.com/problems/employee-free-time/ | [this link](../practice/solution/0759_employee_free_time.py) |
| 766 | https://leetcode.com/problems/toeplitz-matrix/ | [this link](../practice/solution/0766_toeplitz_matrix.py) |
| 836 | https://leetcode.com/problems/rectangle-overlap/ | [this link](../practice/solution/0836_rectangle_overlap.py) | 
| 945 | https://leetcode.com/problems/minimum-increment-to-make-array-unique/ | [this link](../practice/solution/0945_minimum_increment_to_make_array_unique.py) |
| 957 | https://leetcode.com/problems/prison-cells-after-n-days/ | [this link](../practice/solution/0957_prison_cells_after_n_days.py) |
| 1013 | https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/ | [this link](../practice/solution/1013_partition_array_into_three_parts_with_equal_sum.py) |
| 1031 | https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/ | [this link](../practice/solution/1031_maximum_sum_of_two_non_overlapping_subarrays.py) |
| 1243 | https://leetcode.com/problems/array-transformation/ | [this link](../practice/solution/1243_array_transformation.py) |
| 1356 | https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/ | [this link](../practice/solution/1356_sort_integers_by_the_number_of_1_bits.py) |
| | https://www.1point3acres.com/bbs/thread-642190-1-1.html | [this link](../practice/tusimple/min_cost_to_racing_track_end.py) |
| | https://www.1point3acres.com/bbs/thread-592043-1-1.html | [this link](../practice/tusimple/subsequence_removal.py) |
| | https://www.1point3acres.com/bbs/thread-592043-1-1.html | [this link](../practice/tusimple/subsequence_removal_ii.py) | 
| | https://www.1point3acres.com/bbs/thread-592043-1-1.html | [this link](../practice/tusimple/subsequence_removal_iii.py) |

## Linked List

In computer science, a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists. Linked lists are among the simplest and most common data structures. They can be used to implement several other common abstract data types, including lists, stacks, queues, associative arrays, and S-expressions, though it is not uncommon to implement those data structures directly without using a linked list as the basis. [Wikipedia](https://en.wikipedia.org/wiki/Linked_list)

This type of problem includes: 1)delete elements in the linked list, 2)insert elements in the linked list. 3)merge elements from two linked lists 4)rotate elements in a linked list, 5)copy special linked list

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 2 | https://leetcode.com/problems/add-two-numbers/ | [this link](../practice/solution/0002_add_two_numbers.py) |
| 19 | https://leetcode.com/problems/remove-nth-node-from-end-of-list/ | [this link](../practice/solution/0019_remove_nth_node_from_end_of_list.py) |
| 21 | https://leetcode.com/problems/merge-two-sorted-lists/ | [this link](../practice/solution/0021_merge_two_sorted_lists.py) |
| 23 | https://leetcode.com/problems/merge-k-sorted-lists/ | [this link](../practice/solution/0023_merge_k_sorted_lists.py) |
| 24 | https://leetcode.com/problems/swap-nodes-in-pairs/ | [this link](../practice/solution/0024_swap_nodes_in_pairs.py) |
| 25 | https://leetcode.com/problems/reverse-nodes-in-k-group/ | |
| 82 | https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/ | |
| 83 | https://leetcode.com/problems/remove-duplicates-from-sorted-list/ | [this link](../practice/solution/0083_remove_duplicates_from_sorted_list.py) |
| 86 | https://leetcode.com/problems/partition-list/ | |
| 92 | https://leetcode.com/problems/reverse-linked-list-ii/ | [this link](../practice/solution/0092_reverse_linked_list_ii.py) |
| 138 | https://leetcode.com/problems/copy-list-with-random-pointer/ | [this link](../practice/solution/0138_copy_list_with_random_pointer.py) |
| 143 | https://leetcode.com/problems/reorder-list/ | |
| 203 | https://leetcode.com/problems/remove-linked-list-elements/ | |
| 206 | https://leetcode.com/problems/reverse-linked-list/ | [this link](../practice/solution/206_reverse_linked_list.py) |
| 237 | https://leetcode.com/problems/delete-node-in-a-linked-list/ | |
| 328 | https://leetcode.com/problems/odd-even-linked-list/ | [this link](../practice/solution/0328_odd_even_linked_list.py) |
| 369 | https://leetcode.com/problems/plus-one-linked-list/ | |
| 445 | https://leetcode.com/problems/add-two-numbers-ii/ | |
| 708 | https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/ | |

## String

In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation). A string is generally considered as a data type and is often implemented as an array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding. String may also denote more general arrays or other sequence (or list) data types and structures. Depending on the programming language and precise data type used, a variable declared to be a string may either cause storage in memory to be statically allocated for a predetermined maximum length or employ dynamic allocation to allow it to hold a variable number of elements. [Wikipedia](https://en.wikipedia.org/wiki/String_(computer_science))

String is not a data structure but many coding problems play with it. Python strings are "immutable" which means they cannot be changed after they are created (Java strings also use this immutable style). Since strings can't be changed, we construct *new* strings as we go to represent computed values. 

This type of problem includes: 1)sort string syntax, 2)split and join string syntax, 3)encoding and decoding string syntax, 4)regular expression, 5)common string methods, 6)Unix utilities(optional)

| *#* | *Link* |*Solution* |
| ---- | --------------------------------- | --------------------------------- |
| 6 | https://leetcode.com/problems/zigzag-conversion/ | [this link](../practice/solution/0006_zigzag_conversion.py) | 
| 8 | https://leetcode.com/problems/string-to-integer-atoi/ | [this link](../practice/solution/0008_string_to_integer_atoi.py) | 
| 12 | https://leetcode.com/problems/integer-to-roman/ | [this link](../practice/solution/0012_integer_to_roman.py)|
| 65 | https://leetcode.com/problems/valid-number/ | [this link](../practice/solution/0065_valid_number.py) |
| 93 | https://leetcode.com/problems/restore-ip-addresses/ | [this link](../practice/solution/0093_restore_ip_addresses.py) |
| 125 | https://leetcode.com/problems/valid-palindrome/ | [this link](../practice/solution/0125_valid_palindrome.py) |
| 151 | https://leetcode.com/problems/reverse-words-in-a-string/ | [this link](../practice/solution/0151_reverse_words_in_a_string.py) |
| 165 | https://leetcode.com/problems/compare-version-numbers/ | |
| 242 | https://leetcode.com/problems/valid-anagram/ | |
| 387 | https://leetcode.com/problems/first-unique-character-in-a-string/ | |
| 405 | https://leetcode.com/problems/convert-a-number-to-hexadecimal/ | |
| 419 | https://leetcode.com/problems/battleships-in-a-board/ | |
| 468 | https://leetcode.com/problems/validate-ip-address/ | |
| 640 | https://leetcode.com/problems/solve-the-equation/ | |
| 678 | https://leetcode.com/problems/valid-parenthesis-string/ | |
| 796 | https://leetcode.com/problems/rotate-string/ | |
| 806 | https://leetcode.com/problems/number-of-lines-to-write-string/ | |
| 937 | https://leetcode.com/problems/reorder-data-in-log-files/ | [this link](../practice/solution/0937_reorder_data_in_log_files.py) |