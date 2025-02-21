"""
Approach:
    Brute force approach is to replace the elements of the tree with the values of the nodes for that position.
    Then we can search for the target value in the tree.

Time Complexity:
    O(n) for filling the elements in the tree and O(n) for searching the target value in the tree.

Space Complexity:
    O(n) for the recursive stack.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.fill_elements(self.root,0)

    def fill_elements(self,node, value):
        if node == None:
            return

        node.val = value
        self.fill_elements(node.left, (value * 2)+1)
        self.fill_elements(node.right, (value * 2)+2)


    def find_element(self, node, target):
        if node == None:
            return False

        if node.val == target:
            return True
        return self.find_element(node.left, target) or self.find_element(node.right, target)
        


    def find(self, target: int) -> bool:
        return self.find_element(self.root, target)


        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)