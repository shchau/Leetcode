class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lenStr = len(s)
        
        if lenStr <= 1:
            return True
        
        # Front and back pointer
        front, back = 0, lenStr-1
        
        while front < back:
            
            # Move past non alphanumeric characters
            while not s[front].isalnum() and front < back:
                front += 1
            while not s[back].isalnum() and front < back:
                back -= 1
            
            # Check if chars are the same
            if s[front].lower() == s[back].lower():
                front += 1
                back -= 1
            else:
                return False
            
        return True