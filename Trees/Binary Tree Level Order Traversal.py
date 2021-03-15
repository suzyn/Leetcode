Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 36 ms, 14.6 MB
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return
        
        queue = [root]      
        result = []     
    
        # 레벨 단위로 순회
        while queue:
            length = len(queue)
            temp = []                   
            for i in range(0, length):
                root = queue.pop(0)
                temp.append(root.val)
                if root.left : queue.append(root.left)
                if root.right: queue.append(root.right)
            result.append(temp)
        
        return result
 