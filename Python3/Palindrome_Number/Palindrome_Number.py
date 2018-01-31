class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # More special cases improve overall runtime in the reverse str solution.  
        
        # Negatives aren't palindromes
        if x < 0:
            return False
        
        # single digit numbers are palindromes
        if x < 10:
            return True

        # two digit numbers that aren't divsible by 11 aren't palindromes
        if x < 100 and x % 11 != 0:
            return False
        # two digit numbers that are divisible by 11 are palindromes
        elif x < 100 and x % 11 == 0:
            return True
        
        # Reverse it as a string and conmpare with itself to see if it's a palindrome
        if str(x)[::-1] == str(x):
            return True 
        else:
            return False
