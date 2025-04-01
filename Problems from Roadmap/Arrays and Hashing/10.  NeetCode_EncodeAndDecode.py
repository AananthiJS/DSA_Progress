class Solution:
    def encode(self, strs):
        #get the length of each string and add it before each string itself 
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string

    def decode(self, s: str):
        decoded_list = []
        i = 0
        while i < len(s):
            j = i 
            while j < len(s) and s[j].isdigit():#s[j] != "#":
                j += 1  

            length = int(s[i:j]) 
            j += 1 
            word = s[j: j + length]
            decoded_list.append(word)  
            i = j + length 
        return decoded_list

            
