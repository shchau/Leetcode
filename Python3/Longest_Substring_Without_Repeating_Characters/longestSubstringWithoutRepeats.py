class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """        
        ans, pos, visited = 0, 0, [False for char in range(256)]
        for i, char in enumerate(s):
            
            if visited[ord(char)]:  # If this char has been visited before
                while char != s[pos]:
                    #he number of times this loop iterates is equal to the length of the substring. 
                    
                    visited[ord(s[pos])] = False # reset the chars of our current substring to have not been visited
                    pos += 1 # pos is our current position in the original string.
                pos += 1
            else:
                # This is a new char for our current substring 
                visited[ord(char)] = True
            
            ans = max(ans, i - pos + 1) # i - pos + 1 is equal to the length of the current substring. 
        return ans

# Testing
#sol = Solution()
#s = "abcabcbb"
#print(sol.lengthOfLongestSubstring(s))