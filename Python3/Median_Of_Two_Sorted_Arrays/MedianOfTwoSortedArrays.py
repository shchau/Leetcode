class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2 
        m, n = len(A), len(B)
        if m > n:
             A, B, m, n = B, A, n, m
        
        imin, imax, halflen = 0, m, (m + n + 1) / 2
        
        # Initiate Binary Search
        while imin <= imax:
            # i is middle of A, j is middle of B
            i = int((imin + imax) / 2)
            j = int(halflen - i)
        
            if i < m and B[j-1] > A[i]:
                # i is too small 
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big 
                imax = i - 1
            else:
                # i is perfect 
                
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])
                
                
                if (m+n) % 2 == 1:
                    # There's an odd amount of numbers, so max_of_left is the median
                    return max_of_left
                
                # Else there's an even amount of numbers, so median is between two numbers in the middle
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                
                return (float(max_of_left + min_of_right) / 2.0)