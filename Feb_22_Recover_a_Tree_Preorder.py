
"""
Approach:
    The idea is to use a dfs approach to build the tree from the traversal string. We will keep track of the depth of the tree and the index of the traversal string.
    We count the number of dashes to get the depth of the current node. if the depth is equal to the current depth, we create a new node and increment the index.
    We then recursively call the left and right child of the current node with the updated index and depth.
    We return the root of the tree.
Time complexity:
    O(n) where n is the length of the traversal string.
Space complexity:
    O(n) for the recursive stack.
"""





class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(index, traversal, depth):
    dashes = 0
    curr_index = index[0]

    while curr_index < len(traversal) and traversal[curr_index] == '-':
        dashes+=1
        curr_index+=1
    if depth != dashes:
        return None
    index[0] = curr_index
    num = ""
    while curr_index < len(traversal) and traversal[curr_index] >= '0' and traversal[curr_index] <= '9':
        num += traversal[curr_index]
        curr_index+=1

    
    index[0] = curr_index
    root = TreeNode(int(num))
    root.left = dfs(index, traversal, depth+1)
    root.right = dfs(index, traversal, depth+1)

    return root



def recoverFromPreorder(traversal: str):
    pos = [0]
    return dfs(pos, traversal, 0)



print(recoverFromPreorder("1-2--3--4-5--6--7")) # [1,2,5,3,4,6,7]
print(recoverFromPreorder("1-2--3---4-5--6---7")) # [1,2,5,3,null,6,null,4,null,7]