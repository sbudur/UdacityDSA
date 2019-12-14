l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(20, 100)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((20, 99) == get_min_max(l)) else "Fail")

l =[]
print ("Pass" if (-1 == get_min_max(l)) else "Fail")

l = [i for i in range(-20, 100)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-20, 99) == get_min_max(l)) else "Fail")

0 9
Pass
20 99
Pass
Pass
-20 99
Pass

Complexity:
O(n) - need to iterate once through the entire list.

