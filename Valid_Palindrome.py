"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for i in range(len(s)):
            if s[i].isalnum():
                new_s+=s[i].lower()

        left,right=0,len(new_s)-1
        while left<right:
            if new_s[left]!=new_s[right]:
                return False
            left+=1
            right-=1
            
        return True



## This is one of acceptable solution we can do better 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while (
                left < right and not s[left].isalnum()
            ):  # Checks condition to move pointer
                left += 1  # Moves from all the white spaces and non alpha num elements
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower(): # Actual condition to check to move forward

                return False
            left += 1
            right -= 1

        return True
