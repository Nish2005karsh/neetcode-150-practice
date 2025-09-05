def maxDepth(root):
    if not root:
        return 0
    leftheight=maxDepth(root.left)
    rightHeight=maxDepth(root.right)
    return max(leftheight,rightHeight)+1

