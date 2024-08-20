# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        l = []

        def linked_list_to_list(head):
            return [node.val for node in iterate_list(head)]

# Helper generator to iterate through the linked list
        def iterate_list(head):
            current = head
            while current is not None:
                yield current
                current = current.next
        
        l = linked_list_to_list(head)
        return l == l[::-1]

            
        
