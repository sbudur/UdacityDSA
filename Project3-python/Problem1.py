#!/usr/bin/env python
# coding: utf-8

# In[3]:


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start = 0
    end = number
    
    if number ==0 or number==1:
        return number
    
    while(end - start >=0):
        #print('range ', start, ' - ', end)
        mid = (end + start) / 2
        #print('encountered ', mid)
        sq = mid * mid 
        #print('sq - ', sq)
        if (abs(sq-number) <= 1 or number==sq):
            return int(mid)
        elif number < sq:
            # number 9 , mid - 4 , sq- 16 
            # sqrt is between 0 to 4.5
            end = mid
        else:
            start = mid         
        
    
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


# In[ ]:





# In[ ]:




