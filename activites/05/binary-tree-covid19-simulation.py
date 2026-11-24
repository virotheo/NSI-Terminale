
"""
1) According to the decision tree in Figure 1 
a patient who has a cough and a fever but neither 
nausea nor anosmia is positive for COVID-19.
2) The meaning of the 'assert' in the symptom function is that
we don't want a leaf from the  binary tree so if we make a 'assert not a leaf()'
we'll remove all the leaves of the binary tree. 
3) An attribute might be for example value or even left and right and
the class method might be for example is_leaf or symptom or diagnosis.
4) (cf applique function)
5) The lenght of the binary tree is 16
6) We were able to reduce the lenght of the binary tree to 10
7) (cf reduce function)
"""
class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left == None and self.right == None    

    def symptom(self):
        assert not self.is_leaf()
        return self.value

    def diagnosis(self):
        assert self.is_leaf()
        return self.value
    
    def reduce(self):
        if self.is_leaf():
            return 
        self.left.reduce()
        self.right.reduce()
        if self.left.is_leaf() and self.right.is_leaf() \
            and self.left.value == self.right.value :
            self.value = self.right.value
            self.left = None
            self.right = None

n15,n17,n18,n21,n22,n25 = Node('-'),Node('-'),Node('-'),Node('-'),Node('-'),Node('-')

n16,n19,n20,n23,n24,n26,n27,n28,n29,n30 = Node('+'),Node('+'),Node('+'),\
Node('+'),Node('+'),Node('+'),Node('+'),Node('+'),Node('+'),Node('+')

n7,n8,n9,n10,n11,n12,n13,n14 = Node('anosmia',n15,n16),Node('anosmia',n17,n18),\
Node('anosmia',n19,n20),Node('anosmia',n21,n22),Node('anosmia',n23,n24),Node('anosmia',n25,n26),Node('anosmia',n27,n28),Node('anosmia',n29,n30)

n3,n4,n5,n6 = Node('nausea',n7,n8),Node('nausea',n9,n10),Node('nausea',n11,n12),Node('nausea',n13,n14)

n1=Node('fever',n3,n4)
n2=Node('fever',n5,n6)
n0=Node('cough',n1,n2)

def applique(tree, patient):
    if tree.is_leaf():
        return tree.diagnosis()
    else:
        if patient[tree.symptom()]:
            return applique(tree.right,patient)
        else:
            return applique(tree.left,patient)

patient1={'cough':True,'fever':False,'nausea':True,'anosmia':False}

patient2={'cough':False,'fever':True,'nausea':False,'anosmia':True}

print(applique(n0,patient1))
print(applique(n0,patient2))

n0.reduce()
