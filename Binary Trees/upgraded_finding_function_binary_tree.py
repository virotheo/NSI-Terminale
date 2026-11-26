def find(tree,value):
    if tree is empty():
        return False
    if tree.root.key == value:
        return True    
    else:
        if value < tree.root.key:
            return find(tree.sub-left-tree,value)
        else:
            return find(tree.sub-right-tree,value)
# Complexity is O(log(n)) where n is the size of the binary tree
