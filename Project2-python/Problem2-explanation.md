
Output:

find_files('.c', '.')
['./testdir/subdir3/subsubdir1/b.c',
 './testdir/t1.c',
 './testdir/subdir5/a.c',
 './testdir/subdir1/a.c']
 
 find_files(' ', '.')
 []
 
 find_files('.ipynb', '.')
 ['./Problem5 Blockchain.ipynb',
 './Problem2 File Recursion.ipynb',
 './Problem1 LRU Cache.ipynb',
 './Problem4 ActiveDirectory.ipynb',
 './Problem3 Huffman Coding.ipynb',
 './.ipynb_checkpoints/Problem3 Huffman Coding-checkpoint.ipynb',
 './.ipynb_checkpoints/Problem1 LRU Cache-checkpoint.ipynb',
 './.ipynb_checkpoints/Problem5 Blockchain-checkpoint.ipynb',
 './.ipynb_checkpoints/Problem6 Union and Intersection-checkpoint.ipynb',
 './.ipynb_checkpoints/Problem4 ActiveDirectory-checkpoint.ipynb',
 './.ipynb_checkpoints/Problem2 File Recursion-checkpoint.ipynb',
 './Problem6 Union and Intersection.ipynb']
 
 find_files('h', '.')
 ['./testdir/subdir3/subsubdir1/b.h',
 './testdir/subdir5/a.h',
 './testdir/t1.h',
 './testdir/subdir1/a.h']
 
 
 Complexity:
 Space complexity all the files are stored in list.
 Time complexity - it is a recursive function call to check for directories and subdirectories and further for a file with an extension. The code checks each file only once, so if there are total n files - complexity is O(n).
 