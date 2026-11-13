class Node:
    def __init__(self,key,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root
    def is_empty(self):
        return self.root == None
    def left_sub_tree(self):
        return Tree(self.root.left)
    def right_sub_tree(self):
        return Tree(self.root.right)    
    def in_order_traversal(self):
        if self.is_empty():
            return None
        else:
            self.left_sub_tree().in_order_traversal()
            print(self.root.key,end="--")
            self.right_sub_tree().in_order_traversal()
    def pre_order_traversal(self):
        if self.is_empty():
            return None
        else:
            print(self.root.key,end="--")
            self.left_sub_tree().pre_order_traversal()
            self.right_sub_tree().pre_order_traversal()
    def post_order_traversal(self):
        if self.is_empty():
            return None
        else:
            self.left_sub_tree().post_order_traversal()
            self.right_sub_tree().post_order_traversal()      
            print(self.root.key,end="--") 
    def length(self):
        if self.is_empty():
            return 0
        else:
            return 1 + self.left_sub_tree().length() + self.right_sub_tree().length()
root_node = Node(13, left=Node(6, left=Node(12), right=Node(7, left=Node(9), right=None)), right=Node(4, left=Node(17), right=Node(8)))
test_tree_1 = Tree(root_node)

print("In Order Traversal (🇫🇷parcours infixe🇫🇷) : ")
print(Tree.in_order_traversal(test_tree_1))
print("\n")
print("Pre Order Traversal (🇫🇷parcours prefixe🇫🇷) : ")
print(Tree.pre_order_traversal(test_tree_1))
print("\n")
print("Post Order Traversal (🇫🇷parcours suffixe🇫🇷) : ")
print(Tree.post_order_traversal(test_tree_1))
print("\n")
print(f"Lenght : {Tree.length(test_tree_1)}")
