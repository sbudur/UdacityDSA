#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[199]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self, char=''):
        ## Initialize this node in the Trie
        #print('intialised...')
        self.char = char 
        self.children = []
        self.last = False
        
    def insert_child(self, char):
        ## Add a child node in this Trie
        new_child = TrieNode(char)
        return new_child
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        if self.last:
            #print('reached end ...', suffix)
            yield suffix
        
        #print(self.char)
        for each_node in self.children:
            yield from each_node.suffixes(suffix+each_node.char)
        pass
    
   
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root_node = TrieNode()
        
    def insert(self, word):
        ## Add a word to the Trie
        curr_node = self.root_node
        for each_char in word:
            found_child = False
            for child in curr_node.children:
                if child.char == each_char:
                    curr_node = child
                    found_child = True
                    break
            if found_child == False:
                new_node = TrieNode(each_char)
                curr_node.children.append(new_node)
                curr_node = new_node
        curr_node.last = True   
            
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        curr_node = self.root_node
        if not curr_node.children:
            print('no children in root')
            return None
        
        for each_char in prefix:
            not_found = True
            #print('searching ', each_char)
            for each_child in curr_node.children:
                if each_child.char == each_char:
                    curr_node = each_child
                    not_found = False
                    break
        if not_found == True:
            return None
        return curr_node
        pass


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[4]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
print(MyTrie.find('trigger'))
print(MyTrie.find('soul'))
print(MyTrie.find('fact'))


# In[5]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:





# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[56]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        pass
    
    def insert(self, char):
        ## Add a child node in this Trie
        pass
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        pass


# In[ ]:




