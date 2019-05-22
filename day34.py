"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    
    while root != None:
        if root.left == None:
            root = root.right 
        else:
            temp = root.right
            root.right = root.left
            root.left = None
            root = root.right
            right = root
            while right.right != None:
                right = right.right
            right.right = temp




            