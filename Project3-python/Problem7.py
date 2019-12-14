#!/usr/bin/env python
# coding: utf-8

# In[1]:


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root_node = RouteTrieNode('/', handler)
        
    def insert(self, input_path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        curr_node = self.root_node
        for path_name in input_path_list:
            found_child = False
            for child in curr_node.children:
                if child.path_name == path_name:
                    curr_node = child
                    found_child = True
                    break
            if found_child == False:
                new_node = RouteTrieNode(path_name)
                curr_node.children.append(new_node)
                curr_node = new_node
        #curr_node.last = True
        
        curr_node.handler = handler 
        #print('added : ', curr_node.path_name, ' - ', curr_node.handler)

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr_node = self.root_node
        
        if len(path_list) == 1 and path_list[0] == '/':
            return curr_node.handler
        
        for path_name in path_list:
            not_found = True
            for each_child in curr_node.children:
                if each_child.path_name == path_name:
                    curr_node = each_child
                    not_found = False
                    break
        
        if not_found == True:
            return None
        
        """
        if not curr_node.children:
            print('no children in root')
            return None
        """
    
        #print('found:', curr_node.path_name, '-', curr_node.handler)
        return curr_node.handler
        
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, path_part='', handler=None):
        # Initialize the node with children as before, plus a handler
        self.path_name = path_part 
        self.children = []
        self.handler = handler

    def insert(self, path_name, handler):
        # Insert the node as before
        new_child = RouteTrieNode(path_name, handler)
        return new_child


# In[2]:


import os
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_route = RouteTrie(handler)

    def add_handler(self, path_str, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path_str)
        #print(path_list)
        #print('add ', path_list, '-',handler)
        if path_list[0]=='/':
            #print('calling insert ....')
            self.root_route.insert(path_list[1:], handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        #print('lookup - ', path)
        path_list = self.split_path(path)
        
        if path_list[0] != '/':
            return None 
        
        return self.root_route.find(path_list)
    
    
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        allparts = []
        while 1:
            parts = os.path.split(path)
            #print('printing parts ', parts )
            if parts[0] == path:  # sentinel for absolute paths
                #print('parts[0] - ', parts[0], ' === path', path )
                allparts.insert(0, parts[0])
                break
            elif parts[1] == path: # sentinel for relative paths
                #print('parts[1] - ', parts[1], ' === path', path )
                allparts.insert(0, parts[1])
                break
            else:
                path = parts[0]
                #print('assigning', parts[0], ' to path')
                allparts.insert(0, parts[1])
                #print(allparts)
        return allparts


# In[3]:


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
#router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


# In[ ]:





# In[ ]:




