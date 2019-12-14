print(MyTrie.find('trigger'))
print(MyTrie.find('soul'))
print(MyTrie.find('fact'))

<__main__.TrieNode object at 0x7ffb80060ef0>
None
<__main__.TrieNode object at 0x7ffb80060be0>

Recommendations:
prefix - tr
ie
igger
igonometry
ipod

prefix - a
nt
nthology
ntagonist
ntonym

prefix - as
as not found

prefix - astr
astr not found

Complexity:
Both for insertion and search the worst case complexity is O(n). Even we look for suffixes using recursive serch it is O(n). 
