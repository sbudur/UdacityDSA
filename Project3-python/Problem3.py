#!/usr/bin/env python
# coding: utf-8

# In[12]:


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    # quicksort on input_list
    
    quicksort(input_list,0,len(input_list)-1)
    print(input_list)
    
    # picking on alternate digits 
    num1 = 0
    for i in range(len(input_list)-1, -1, -2):
        
        num1 = num1*10 + input_list[i]
    
    num2 = 0
    for i in range(len(input_list)-2, -1, -2):
       
        num2 = num2*10 + input_list[i]
    
    print(num1, num2)
    return [num1, num2]
    pass


def quicksort(arr,low,high): 
    if low < high: 
        p_index = partition(arr,low,high) 
  
        quicksort(arr, low, p_index-1) 
        quicksort(arr, p_index+1, high) 
        
def partition(arr,low,high): 
    i = low-1         
    pivot = arr[high]  
  
    for j in range(low , high): 
        if arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return(i+1) 

        


# In[13]:


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

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


# In[ ]:





# In[ ]:




