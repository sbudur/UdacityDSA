#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os

# Let us print the files in the directory in which you are running this script
#print (os.listdir('.'))
#print (os.path.isfile("./ex.py"))
#print ("./ex.py".endswith(".py"))

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = list()
    for each in os.listdir(path):
        filepath = os.path.join(path, each)
        print(filepath)
        if os.path.isdir(filepath):
            files = files + find_files(suffix, filepath)
        else:
            if filepath.endswith(suffix):
                files.append(filepath)
            
    return files

#find_files('.c', '.')
#find_files('.ipynb', '.')
find_files('h', '.')


# In[ ]:





# In[ ]:




