#!/usr/bin/env python
# coding: utf-8

# In[2]:


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low = 0
    curr = 0
    high = len(input_list)-1
    
    while(curr<=high):
        if input_list[curr] == 0:
            input_list[low],input_list[curr]=input_list[curr],input_list[low]
            low+=1
            curr+=1
        elif input_list[curr]==2:
            input_list[curr], input_list[high]= input_list[high], input_list[curr]
            high-=1
        else:
            curr+=1
    print(input_list)
    return input_list
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0])
test_function([])
test_function([2, 2, 2, 0])


# In[ ]:





# In[ ]:




