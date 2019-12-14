#!/usr/bin/env python
# coding: utf-8

# In[5]:


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return -1
    ctr = 1
    max_int = ints[0]
    min_int = ints[0]
    while(ctr<len(ints)):
        if ints[ctr]>max_int:
            max_int = ints[ctr]
        if ints[ctr]<min_int:
            min_int = ints[ctr]
        ctr+=1
    print(min_int, max_int)
    return (min_int,max_int)
    pass

## Example Test Case of Ten Integers
import random

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


# In[ ]:




