Tests:

test = MyBlockChain()
test.add_block('Sample Info 1')
test.add_block('Sample Info 2')
test.get_size()

Sample Info 1
2019-12-12 15:11:46.566926
4b9aae88219034ba45fced06f8e7a4a7e8e8c39f3a30562ed1902c176afd80b0
0
Sample Info 2
2019-12-12 15:11:46.567090
d5231e70eae852827030e31c252742ecb73260692810eb3f4798a81fc74cdb5b
4b9aae88219034ba45fced06f8e7a4a7e8e8c39f3a30562ed1902c176afd80b0


test1 = MyBlockChain()
test1.add_block('')
test1.add_block('')
test1.get_size()

2019-12-12 15:10:37.825835
b03a728e21e96441706a738281005b12b52bbca2f0541826859475f02ca70967
0

2019-12-12 15:10:37.825919
e967cc31239ac09a5ec68658904f85861105104d4ded91513b2459a6f248fd13
b03a728e21e96441706a738281005b12b52bbca2f0541826859475f02ca70967
2

test2 = MyBlockChain()
test2.add_block('genesis block')
test2.add_block('block 1')
test2.add_block('block 2')
test2.add_block('block 3')
test2.get_size()

genesis block
2019-12-12 15:13:20.888718
d181f295871a26731bf91724f83a64332f967a36bb0a34bbd07f284589c160e6
0
block 1
2019-12-12 15:13:20.888875
d1b6f2924badc3abe4446029ad84dc3fab35b3c2ebee9bc0b7145e3430f689d6
d181f295871a26731bf91724f83a64332f967a36bb0a34bbd07f284589c160e6
block 2
2019-12-12 15:13:20.889006
e05fcedf32a90c4f4ae1e916f7a6d6b6be760a6264762cd4ccbc655dcdb55810
d1b6f2924badc3abe4446029ad84dc3fab35b3c2ebee9bc0b7145e3430f689d6
block 3
2019-12-12 15:13:20.889144
48f9de83adf0feea17a269125b68845d22e32efac99cc67f446fd5ae820a2ba4
e05fcedf32a90c4f4ae1e916f7a6d6b6be760a6264762cd4ccbc655dcdb55810s

Complexity:
The insertion of a node in doubly linked list add_block() is O(1) beacuse of a tail pointer which keeps the track of the last node in the list. Traversing the linked list from start node to end node for get_size() function of blockchain takes O(n) time. Because it is using doubly linked list - there is an extra space needed for every block that we store, wherein the pointer to the previous node is stored. 