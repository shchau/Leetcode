# Definition for singly-linked list.
class ListNode:
         def __init__(self, x):
                  self.val = x
                  self.next = None

class Solution:
         def addTwoNumbers(self, l1, l2):
                  """
                  :type l1: ListNode
                  :type l2: ListNode
                  :rtype: ListNode
                  """
                  # carry represents the "extra" amount we have when the two numbers added are >= 10
                  carry = 0 
        
                  # res will be our linked list answer, holding the sums as we go through, start is a reference to the head of the linked list
                  res = ListNode(0)  
                  start = res
        
                  # So we're going to do a case-by-case scenario of the solution to make it faster.  
                  while l1:
                           if l2 is None:
                                    break
                           val = carry
                           val += l1.val + l2.val
                           l1 = l1.next
                           l2 = l2.next
            
                           # carry is calculated through dividing by 10, while the actual value in our linked list output is the remainder 
                           carry, val = int(val / 10), int(val % 10)
                           res.next = ListNode(val)
                           res = res.next
            
                           # If our value was 10, then we have to set the next node manually as the remainder of 10 % 10 is 0, and we want a 1.  
                           if carry == 1:
                                    res.next = ListNode(1)
                
                
                  #This loop is intended to be used if l1 is longer than l2. Saves us the run time of accounting for l2
                  while l1:
                           val = carry
                           val += l1.val
                           l1 = l1.next
                           carry, val = int(val / 10), int(val % 10)
                           res.next = ListNode(val)
                           res = res.next
            
                           if carry == 1:
                                    res.next = ListNode(1)
        
        
                  # This loop is for the case that l2 is longer than l1
                  while l2:
                           val = carry
                           val += l2.val
                           l2 = l2.next
                           carry, val = int(val / 10), int(val % 10)
                           res.next = ListNode(val)
                           res = res.next
            
                           if carry == 1:
                                    res.next = ListNode(1)
        
         # Now we return the second node in our answer as it's the head of the resulting linked list we wanted. 
         # (We initialized it with ListNode(0), hence why we use start.next) 
         return start.next
    
# Testing
sol = Solution()
l1, l1.next, l1.next.next = ListNode(2), ListNode(4), ListNode(3)
l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)
print(sol.addTwoNumbers(l1,l2))