#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
def is_user_in_group(user, group):
    #print('---------')
    if user in group.get_users():
        #print(group.get_users())
        return True
    else:
        #print('recurrence ...')
        for sub_group in group.get_groups():
            return is_user_in_group(user, sub_group)
    return False


# In[21]:


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
child.add_user('child_user')

is_user_in_group("sub_child_user", sub_child)
is_user_in_group(" ", sub_child)
is_user_in_group("child", sub_child)
is_user_in_group("sub_child_user", parent)


is_user_in_group("child_user", parent)
is_user_in_group("child_user", sub_child)


# In[ ]:





# In[ ]:




