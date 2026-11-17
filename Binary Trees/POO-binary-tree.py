def Creefile():
    return []

def file_est_vide(F):
    return len(F)==0

def file_emfiler(F,element):
    return F.append(element)#nouveau sommet de la file

def file_taille(F):
    return len(F)


def file_defiler(F:list):
    if not file_est_vide(F):
        return F.pop(0)
    else:
        return

def file_tete(F):
    if not file_est_vide(F):
        return F[-1]

def file_insert_elements(l_element,F):
    for x in l_element:
        file_emfiler(F,x)

def file_vider(F):
    while not file_est_vide(F):
        print(file_defiler(F))


def inverser(F):
    l=Creefile()
    while not file_est_vide(F):
        file_emfiler(l,file_defiler(F))
    F=l



def Ordonner(F):
    l_imF=Creefile()
    l_F=Creefile()
    while not file_est_vide(F):
        new=file_defiler(F)
        if new%2==0:
            file_emfiler(l_F,new)
        else:
            file_emfiler(l_imF,new)
    while not file_est_vide(l_F):
        file_emfiler(F,file_defiler(l_F))
    while not file_est_vide(l_imF):
        file_emfiler(F,file_defiler(l_imF))



mafile=Creefile()
file_emfiler(mafile,"a")
file_emfiler(mafile,"b")
file_emfiler(mafile,"c")
file_emfiler(mafile,"d")
inverser(mafile)
print(mafile)


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
    def height(self):
        if self.is_empty():
            return -1
        else:     
            left_height = self.left_sub_tree().height()
            right_height = self.right_sub_tree().height()
            return 1 + max(left_height, right_height)   
    def find(self, valeur):
        if self.is_empty():
            return False
        if self.root.key == valeur:
            return True
        return self.left_sub_tree().find(valeur) or self.right_sub_tree().find(valeur)    
    def breadth_first_traversal(self):
        f = Creefile()
        file_emfiler(f,self.root)
        while not file_est_vide(f):
            node = file_defiler(f)
            print(node.key, end="--")
            if node.left!=None:
                file_emfiler(f,node.left)
            if node.right != None:
                file_emfiler(f,node.right)


n8 = Node(8)
n11 = Node(11)
n5 = Node(5)
n10 = Node(10,n11)
n7 = Node(7,n8,n5)
n9 = Node(9,n10)
n13 = Node(13,n7,n9)
my_tree = Tree(n13)

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
print("\n")
print(f"Height : {Tree.height(test_tree_1)}")
print(test_tree_1.find(5))
print('\n')
print(f"Breadth Traversal (🇫🇷parcours en largeur🇫🇷) : ")
print(my_tree.breadth_first_traversal())
