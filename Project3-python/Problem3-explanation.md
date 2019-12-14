test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case1 = [[1,3,5,6], [63,51]]
test_function(test_case)
test_function(test_case1)
test_case2 = [[1,3], [3,1]]
test_function(test_case2)
test_case3 = [[0,3,1], [30,1]]
test_function(test_case3)
test_case4 = [[], []]
test_function(test_case4)

[1, 2, 3, 4, 5]
531 42
Pass
[2, 4, 5, 6, 8, 9]
964 852
Pass
[1, 3, 5, 6]
63 51
Pass
[1, 3]
3 1
Pass
[0, 1, 3]
30 1
Pass
[]
0 0
Pass

Complexity:
Applied quicksort to sort the input list whose average runtime is O(nlog(n)) and picked on alternate numbers in the list to form 2 max numbers.Quicksort is considered fastest sorting algorithm and performance is average on most inputs cases, but not to forget it depends mainly on th input and pivot selection.
