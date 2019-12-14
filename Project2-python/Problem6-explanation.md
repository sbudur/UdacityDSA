# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print('union - first test ')
print (union(linked_list_1,linked_list_2))
print('intersection - first test')
print (intersection(linked_list_1,linked_list_2))

OUTPUT:
union - first test 
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 -> 
intersection - first test
4 -> 6 -> 6 -> 4 -> 21 -> 


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3,2,4,35,6,65,6,4,3,23]
element_4 = [1,7,8,9,11,21,1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)
print('union - second test')
print (union(linked_list_3,linked_list_4))
print('intersection - second test')
print (intersection(linked_list_3,linked_list_4))

OUTPUT:
union - second test
3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
intersection - second test


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = []
element_6 = [1,7,8,9,11,21,1]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)
print('union - third test')
print (union(linked_list_5,linked_list_6))
print('intersection - third test')
print (intersection(linked_list_5,linked_list_6))

OUTPUT:
union - third test
1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
intersection - third test



Complexity:
intersection(list1, list2) function takes two while loops for checking every element in list1 is present in list 2 which leads to O(n*n)
union(list1, list2) function involves making a copy of the existing linked list where each node is created again and added to the union list accordingly from 2 input linked lists. Complexity is O(n) as it needs to traverse each and every node in both of the lists and copy in to output list.