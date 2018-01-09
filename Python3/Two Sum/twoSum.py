class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a dictionary to store viewed numbers with their indexs
        viewed = {}
        for index, num in enumerate(nums):
            # If the other number to add up to the target has been seen already, we have our answer
                if target - num in viewed:
                    return[viewed[target - num], index]
            # Else add it to the numbers we've viewed
                viewed[num] = index

# Testing 
#sol = Solution()
#nums = [3,2,4]
#target = 6
#print(sol.twoSum(nums, target))