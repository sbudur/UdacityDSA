#!/usr/bin/env python
# coding: utf-8

# In[6]:


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # finding pivot element using binary search
    if input_list[0]<input_list[len(input_list)-1]:
        # array is sorted but not rotated
        pivot_idx = (len(input_list)-1)/2
    else:
        pivot_val, pivot_idx = get_pivot(input_list, 0, len(input_list)-1)
        #print(pivot_val, pivot_idx)
        
    # finding the element
    num_idx = search_element(input_list, 0, pivot_idx, len(input_list)-1, number)
    print(num_idx)
    return num_idx
    pass

def search_element(input_list, low, mid, high, number):
    if low>high:
        return -1
    
    if number == input_list[mid]:
        return mid 
    elif number>=input_list[low] and number<=input_list[mid]:
        #print('low to mid', low,' - ', mid)
        return search_element(input_list, low, int((low+mid)/2), mid, number)
    else:
        #print('mid+1 to high')
        return search_element(input_list, mid+1, int((high+mid+1)/2), high, number)

def get_pivot(input_list, low, high):
    if low>high:
        return -1
    if low==high:
        return low
    #print('process ', low, ' to ', high)
    mid = int((low+high)/2)
    if input_list[mid]>input_list[mid+1]:
        return input_list[mid], mid 
    elif input_list[mid]>input_list[high]:
        return get_pivot(input_list, mid, high)
    else:
        return get_pivot(input_list, low, mid)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            #print('linear search index - ', index)
            return index
    #print('linear search index - ', index)
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# In[ ]:





# In[ ]:




