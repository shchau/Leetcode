class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            # if number is negative, make it positive
            x = -x
            # convert to str, reverse that string, and change back to negative int
            ans = -int(str(x)[::-1])
            
        else:
            # convert to str, reverse str, convert back to int
            ans = int(str(x)[::-1])
        
        # check for overflow
        if ans > 2147483647 or ans < -2147483648:
            return 0
        
        return ans