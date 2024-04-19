# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1=""
        str2=""
        curr = l1
        curr2 = l2
        
        while curr:
            str1 += str(curr.val)
            curr = curr.next
        while curr2:
            str2 += str(curr2.val)
            curr2 = curr2.next   
        result = int(str1) + int(str2)   
        char_tuple = tuple(str(result))
        result = ListNode(int(char_tuple[0]))
        curr = result
        for char in char_tuple[1:]: 
            curr.next = ListNode(int(char))
            curr = curr.next
        return result         
        