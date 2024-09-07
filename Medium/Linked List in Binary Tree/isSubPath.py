# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            if head.val != root.val:
                return False
            return check_vals(head.next, root.left) or check_vals(head.next, root.right)
        
        if not root:
            return False
        if dfs(head, root):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


        

        
