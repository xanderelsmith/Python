# Definition for singly-linked list.
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#   Input: l1 = [2, 4, 3] (represents 342), l2 = [5, 6, 4] (represents 465)
#   Output: [7, 0, 8] (represents 807)
from typing import Optional

from addtwonum.listnode import ListNode
from addtwonum.solution import Solution
 # Constructing the example linked lists:
# l1 represents 342: 2 -> 4 -> 3
l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 represents 465: 5 -> 6 -> 4
l2 = ListNode(5, ListNode(6, ListNode(4)))

    # Adding the two numbers:
new_var = Solution()
result=new_var.addTwoNumbers(l1, l2)
    
    # Print the resulting linked list:
print("Result:", result)
                

