INPUT:
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
child.add_user('child_user')

Tests:
is_user_in_group("sub_child_user", sub_child) - True
is_user_in_group(" ", sub_child) - False
is_user_in_group("child", sub_child) - False
is_user_in_group("sub_child_user", parent) -True

is_user_in_group("child_user", parent) - True
is_user_in_group("child_user", sub_child) - False 

Complexity:
Worst case is going through each and every group and sub group to check for a user so O(n). Where n is the total number of groups and subgroups and users.