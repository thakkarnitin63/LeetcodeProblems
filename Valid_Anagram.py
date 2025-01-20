"""Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False

        s_dict=defaultdict(int)
        t_dict=defaultdict(int)
        for itr in range(0,len(s)):
            s_dict[s[itr]]+=1
            t_dict[t[itr]]+=1
        
        for itr2 in s_dict:
            if s_dict[itr2]!=t_dict[itr2]:
                return False
        return True
    

#### not my solution, but i like this one as well#####
"""
def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        char_count = defaultdict(int)

        for char in s:
            char_count[char] += 1

        for char in t:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        return True
"""