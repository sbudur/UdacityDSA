test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

0
Pass
5
Pass
2
Pass
3
Pass
-1
Pass


Complexity:
The solution goes by finding the pivot point - the element next to this point is smaller and then we divide the list at this pivot point in to two parts and pass it to binary search. Finding the pivot point is also done using binary search which takes O(log(n)) time. So overall complexity is O(log(n)), and space complexity is for storing N elements, binary serach and finding pivot does not change the order of the elements it just access the elements by indexes.
