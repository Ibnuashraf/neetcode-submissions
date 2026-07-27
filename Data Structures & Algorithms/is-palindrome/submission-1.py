class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=""
         
        for ch in s:
            if ch.isalnum():
                clean+=ch.lower()
        if clean == clean[::-1]:
            return True 
        else :
            return False




        