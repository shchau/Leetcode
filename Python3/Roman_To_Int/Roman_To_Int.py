class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Roman to Decimal conversions
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ans = 0
        i = 0
        
        while i < len(s):
            c1 = romanDict[s[i]]
        
            if i + 1 < len(s):
                # There's another character to be checked, we'll see if it follows the special case. 
                c2 = romanDict[s[i+1]]
            
                if c1 >= c2:
                # Value we're currently iterating on is fine to translate directly 
                    ans += c1
                    i += 1
                else:
                # Value follows special case, i.e "IV", meaning we'd add 5-1 == 4 
                    ans += c2 - c1
                    i += 2
            else:
            # Value we're currently iterating on is fine to translate directly
                ans += c1
                i += 1
            
        return ans