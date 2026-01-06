# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def traverse(root,level,level_val):
    if level not in level_val:
        level_val[level]=0
    val = root.val
    level_val[level]=level_val[level]+val
    left_root = root.left
    right_root = root.right
    if left_root is not None:
        level_val = traverse(left_root,level+1,level_val)
    if right_root is not None:
        level_val = traverse(right_root,level+1,level_val)
    return level_val

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_val={}
        level_val = traverse(root,1,level_val)
        print(level_val)
        max_val =level_val[1]
        max_level=1
        for level in level_val:
            val = level_val[level]
            if val>max_val:
                max_val = val
                max_level=level
        return max_level
