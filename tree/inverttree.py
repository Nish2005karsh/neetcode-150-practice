def invertTree(self,root):
    if not root:
        return None
    temp=root.left
    root.left=root.right
    root.right=temp
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
root = [4,2,7,1,3,6,9]
root=TreeNode(root)
print(invertTree(root))