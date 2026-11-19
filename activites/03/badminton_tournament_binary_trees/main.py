'''
Question 1a) - This tree's root is Lea and the leaves are : "Marc" "Lea" "Claire" "Théo" "Marie" "Louis" "Anne" "Kevin".
Question 1b) -
def winner(tree):
   return root(tree)
Question 1c) - 
def final(tree):
    return [root(left(tree)),root(right(tree))]
 Question 2a) - 
def occurences(tree,player_name):
    if is_empty(tree)
    counter = 0
    elif root(tree) == player_name:
        return 1 + occurences(left(tree),player_name)+occurences(right(tree),player_name)
    else:
        return occurences(left(tree),player_name)+occurences(right(tree),player_name)

Question 2b) - 
def has_won(tree,player_name):
    return occurences(tree,player_name) > 1

Question 3) - This is not working because of the case of the winner which is 1 time higher      
def number_of_matches(tree,player_name):
    if player_name == root(tree):
        return occurences(tree,player_name) - 1
    else:
        return occurences(tree,player_name)    

Question 4) -       
def player_list(tree):
    if is_empty(tree):
        return []
    elif is_empty(left(tree)) and is_empty(right(tree)) :
        return [root(tree)]
    else:
        return player_list(left(tree))+player_list(right(tree))        
'''
