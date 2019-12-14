INPUT 1:
a_great_sentence = "In the sky there are always answers and explanations for everything: every pain, every suffering, joy and confusion,/We long for things that harm us and run from the things that grow and heal us. We think good is bad and bad is good"
OUTPUT 1:
The content of the data is: In the sky there are always answers and explanations for everything: every pain, every suffering, joy and confusion,/We long for things that harm us and run from the things that grow and heal us. We think good is bad and bad is good

The content of the encoded data is: 101100001101000101111111010000110101100101001000101111111010011110100011000111101000110010110111110101100010010110001100110101101111010101001110110001100110110111001010101100011111000101101110011011100010111101100011010110000100010000111001010111101110100111010010101111111110111011001111110010001010111101110100111010010011110001100111011101100100001010111101110100111010010001101110010100001000101001111110111011001110010000100101111000010010011001101101110011100000100011010100011100101101110110001101100100111000011111001110100010110110001101100110001000100001110001011111111101110110011011000010111111110001010011111110001111110001001110010110001100110110111000111111001110100010000111100011100010001011111110100001011111111101110110011011000010111111110001010010011011110001111010001100110110111001111110101100101101001110010110100101100011110011101000010111111111011101101100100100111000100010111001110101100010010101100101110011001101101110010010101100101110011101011000100111000100010111

The content of the decoded data is: In the sky there are always answers and explanations for everything: every pain, every suffering, joy and confusion,/We long for things that harm us and run from the things that grow and heal us. We think good is bad and bad is good



INPUT 2:
a_great_sentence = " "
OUTPUT 2:
The content of the data is:  

The content of the encoded data is: 

The content of the decoded data is: 



INPUT 3:
a_great_sentence = "The bird is the word"
OUTPUT 3:
The content of the data is: The bird is the word

The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001

The content of the decoded data is: The bird is the word


Complexity:
It involves building frequency dictionary (character_count function takes constant time storing frequencies of all the characters O(n)) and then selecting 2 minimum frequency symbols and merging them repeatedly for which I have used Min Heap (complexity to build the heap make_heap() using heappush operations is O(n log n), then merge_nodes() by popping the 2 min frequency nodes happens in constant time O(1) but push takes O(nlog(n)) ). Next is recursively traversed all the nodes in the tree and assigned the codes to each character (O(n) as we traverse recursively to each and every node)). Next is Encoding the given input based on the codes assigned and decode the text for the output which takes O(n) time for lookup the dictionary of codes and form the desired output. Overall we can say O(nlog(n)) and space complexity is O(n) for storing the characters as nodes in Heap.