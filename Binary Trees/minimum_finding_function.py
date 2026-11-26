def find_minimum(tree):
    #tree is not empty
    x = tree.root
    while x.left != None:
        x = x.left
    return x.key
