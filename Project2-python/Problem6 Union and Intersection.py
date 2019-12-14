#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def copy_linked_list(self):
        new_list = LinkedList()
        current = self.head
        while current:
            node = Node(current.value)
            new_list.append(node)
            current = current.next
        return new_list
    
def union(list1, list2):
    # Your Solution Here
    if list1.head is None:
        union = list2.copy_linked_list()
        return union
    if list2.head is None:
        union = list1.copy_linked_list()
        return union
        
    union = list1.copy_linked_list()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next
    list2_copy = list2.copy_linked_list()
    last_node.next = list2_copy.head
    
    return union      
    pass
    
def intersection(list1, list2):
    # Your Solution Here
    if (list1.head is None or list2.head is None):
        return LinkedList()
    intersection = LinkedList()
    current1 = list1.head
    while current1:
        current2 = list2.head
        data = current1.value
        while current2:
            if current2.value == data:
                node = Node(data)
                intersection.append(node)
                break
            current2 = current2.next
        current1 = current1.next
    return intersection
    pass


# In[5]:



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


# In[ ]:





# In[ ]:




