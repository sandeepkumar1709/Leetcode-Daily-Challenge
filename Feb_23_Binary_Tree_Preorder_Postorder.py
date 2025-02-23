"""
Approach:
    We can solve this by using divide and conquer approach. We will first build the root of the tree using the first element of the preorder traversal.
    We then find the index of the left child of the root in the postorder traversal. We then recursively build the left and right child of the root.
    We will keep track of the indexes of the postorder traversal in a dictionary to get the index of the left child of the root.
Time complexity:
    O(n) where n is the length of the traversal string.
space complexity:
    O(n) for the recursive stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructTree(r1,r2,o1,o2):
    if r1 > r2 or o1 > o2:
        return None


    root = TreeNode(preorder[r1])
    if r1 != r2:
        left_value = preorder[r1+1]
        left_idx = post_order_indexes[left_value]
        left_size = left_idx - o1+1
        root.left = constructTree(r1+1,r1+left_size,o1,left_idx)
        root.right = constructTree(r1+left_size+1,r2,left_idx+1,o2-1)
    return root


preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
post_order_indexes = {}
for idx,val in enumerate(postorder):
    post_order_indexes[val] = idx
print(constructTree(0,len(postorder)-1,0,len(postorder)-1)) # [1,2,3,4,5,6,7]