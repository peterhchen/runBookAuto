#!/usr/bin/python3

'''
 Print a tree
 How tall of the tree: 5
    #
   ###
  #####
 #######
#########
    #
 Use 1 while loop and 3 for loop
 4 spaces and 1 hash
 3 spaces and 3 hashes
 2 spaces and 5 hashes
 1 spaces and 7 hashes
 0 spaces and 9 hashes
trunk: 4 spaces and 1 hash
'''

#1. Decrease the spaces each time in loop
#2. Increase the bash each time
#3. Save sapce
#4. Decrease tree hieght
#5. print spaces hashes for each row.
#6. print spaces hashes for each row.
tree_height = input ('How tall of the three: ')
tree_height = int (tree_height) - 1
n_space = tree_height
n_hash = 1
trunk_space = tree_height -1

while tree_height != 0:
    for i in range (n_space):
        print (' ', end="")
    for i in range (n_hash):
        print ('#', end="")
    print()
    n_space -= 1
    n_hash += 2
    tree_height -= 1
    
for i in range (trunk_space):
    print (' ', end="")
print ('#', end="")
