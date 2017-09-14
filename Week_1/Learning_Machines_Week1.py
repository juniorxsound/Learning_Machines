
# coding: utf-8

# # Learning Machines - Week 1
# 
# ### RLE Class

# In[31]:

class Learning_Machines_RLE:
    @staticmethod
    def encode(inputString):
        count = 1
        prev = ''
        encoded = []
        for character in inputString:
            if character != prev:
                if prev:
                    entry = (count, prev)
                    encoded.append(entry)
                count = 1
                prev = character
            else:
                count += 1
        else:
            entry = (count,character)
            encoded.append(entry)
        return encoded
    @staticmethod
    def decode(encoded):
        stringOutput = ""
        for character, count in encoded:
            stringOutput += count * character
        return stringOutput


# ### Example Usage
# 
# #### Encoding - Returns an array of tuples (number of characters, character)

# In[32]:

print(Learning_Machines_RLE.encode("11ndv8885555jjjj4k3ld989995nnnkflelll"))


# #### Decoding - Returns a string

# In[34]:

print(Learning_Machines_RLE.decode([(2, '1'), (7, 'b')]))

