#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[10]:


import sys
import heapq

class HeapNode:
    def __init__(self, char, freq):
        """Create node for given symbol and probability."""
        self.left = None
        self.right = None
        self.char = char
        self.freq = freq
        
    def __cmp__(self, other):
        if(other == None):
            return -1
        if(not isinstance(other, HeapNode)):
            return -1
        return self.freq > other.freq
    
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq

    
class Huffman_Encoding:
    def __init__(self):
        self.codes = {}
        self.heap = []
        self.reverse_mapping = {}
        
    def huffman_encoding(self, data):
        # step1
        freq_data = self.character_count(data)
        #step2 
        self.make_heap(freq_data)  
        #step3
        self.merge_nodes()
        #step4 - making codes
        self.make_codes()
        #step5
        
        encoded_text= self.get_encoded_text(data)
        #padded_encoded_text = self.pad_encoded_text(encoded_text)
        #print(encoded_text)
        return encoded_text
        
    def huffman_decoding(self, encoded_data):
        current_code = ""
        decoded_text = ""
        for bit in encoded_data:
            current_code += bit
            if(current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""
        return decoded_text
        pass

    def character_count(self, data):
        char_freq = dict()
        for each_char in data:
            if each_char in char_freq:
                char_freq[each_char]+=1
            else:
                char_freq[each_char]=1
        return char_freq

    def make_heap(self, freq_char_data):
        for each_char in freq_char_data:
            node = HeapNode(each_char, freq_char_data[each_char])
            heapq.heappush(self.heap, node)
    
    def merge_nodes(self):
        while(len(self.heap)>1):
            n1 = heapq.heappop(self.heap)
            n2 = heapq.heappop(self.heap)
            n3 = HeapNode(None, n1.freq + n2.freq)
            n3.left = n1
            n3.right = n2
            heapq.heappush(self.heap, n3)
    
    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)
    
    def make_codes_helper(self, root, current_code):
        if(root == None):
            return
        
        if(root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        
        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")
            
            
    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        
        return encoded_text
    

p1 = Huffman_Encoding()
a_great_sentence = "The bird is the word"

#a_great_sentence = "abcd"
#a_great_sentence = " "
#a_great_sentence = "In the sky there are always answers and explanations for everything: every pain, every suffering, joy and confusion,/We long for things that harm us and run from the things that grow and heal us. We think good is bad and bad is good"

#print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data = p1.huffman_encoding(a_great_sentence)

#print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = p1.huffman_decoding(encoded_data)

#print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))
    
    
    


# In[ ]:





# In[ ]:




