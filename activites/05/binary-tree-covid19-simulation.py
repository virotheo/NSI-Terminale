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
    
    def applique(tree, patient):
        if tree.is_leaf():
            return tree.diagnosis()
        else:
            if patient[tree.symptom()]:
                return applique(tree.right,patient)
            else:
                return applique(tree.left,patient)    

    def reduce(self):
        if self.is_leaf():
            return 
        self.left.reduce()
        self.right.reduce()
        if self.left.is_leaf() and self.right.is_leaf() \
            and self.value == True :
            self.value = self.right.value
            self.left = None
            self.right = None
