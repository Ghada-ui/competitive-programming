# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        comp = []
        current = head
        while current:
            comp.append(current.val)
            current = current.next
        current = head
        while current:
            if current.val != comp.pop():
                return False
            current = current.next

        return True