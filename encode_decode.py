'''
Encode and Decode Strings
Solved 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''


from collections import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            encoded_string+=str(len(s))+'#'+s
        return encoded_string

            

    def decode(self, s: str) -> List[str]:
        i,j=0,0
        decoded_list=[]
        while j<len(s):
            i=j
            while s[i] != "#":
                i+=1
            length=int(s[j:i])
            j=i+1
            i=j+length
            decoded_list.append(s[j:i])
            j=i

        return decoded_list

        
        
        
            
                
        

    
        
        