"""
Enter the results of pre-order traversal and middle-order traversal of a binary tree, build the binary tree and return its root node.
It is assumed that the result of both the preceding and the middle traversal of the input does not contain duplicate numbers.
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def mytree(l1, h1, l2, h2):
            root = TreeNode(preorder[l1])
            for i, val in enumerate(inorder):
                if val == root.val:
                    break
            llen = i - l2
            rlen = h2 - i
            if llen != 0:
                root.left = mytree(l1+1, l1+llen, l2, l2+llen-1)
            else:
                root.left = None
            if rlen != 0:
                root.right = mytree(h1-rlen+1,h1, h2-rlen+1, h2)
            else:
                root.right = None
            return root
        n = len(preorder)
        return mytree(0, n-1, 0, n-1) if n != 0 else None
