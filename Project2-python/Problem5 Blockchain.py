#!/usr/bin/env python
# coding: utf-8

# In[19]:


import hashlib
from datetime import datetime

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None    

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    

    def calc_hash(self):
      sha = hashlib.sha256()

      encoded_hash_str = str(self.timestamp).encode('utf-8') +                  str(self.data).encode('utf-8') +                  str(self.previous_hash).encode('utf-8')

      sha.update(encoded_hash_str)

      return sha.hexdigest()

class MyBlockChain:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_block(self, data):
        if self.head is None:
            #genesis block
            data_block = Block(datetime.now(), data, "0")
            new_node = Node(data_block)
            self.head = self.tail = new_node
        else:
            # hash of the previous block
            prev_hash = self.tail.value.hash
            # create a new block
            data_block = Block(datetime.now(), data, prev_hash)
            new_node = Node(data_block)
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        pass
    
    def get_size(self):
        current_node = self.head
        chain_len = 0
        while current_node is not None:
            print(current_node.value.data)
            print(current_node.value.timestamp)
            print(current_node.value.hash)
            print(current_node.value.previous_hash)
            
            current_node = current_node.next
            chain_len+=1
        return chain_len
        pass 


# In[23]:



test = MyBlockChain()
test.add_block('Sample Info 1')
test.add_block('Sample Info 2')
test.get_size()


"""
test1 = MyBlockChain()
test1.add_block('')
test1.add_block('')
test1.get_size()


test2 = MyBlockChain()
test2.add_block('genesis block')
test2.add_block('block 1')
test2.add_block('block 2')
test2.add_block('block 3')
test2.get_size()

"""


# In[ ]:





# In[ ]:




