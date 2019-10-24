# Course: CS 2302 Data Structures
# Date of last modification: September 24
# Assignment: Lab 4 BST/B-Tree
# TA: Anindita Nath
# Professor: Olac Fuentes
# Purpose: The purpose of this lab is to implement BSTs and B-Trees to determine the differences in
#           running times for the constructions of these two data structures.

import numpy as np
import time

#WordEmbedding, BST, and BTree classes provided by Dr. Fuentes
class WordEmbedding(object):
    def __init__(self,word,embedding):
        # word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)

class BST(object):
    def __init__(self, data, left=None, right=None):  
        self.data = data
        self.left = left 
        self.right = right
    
    def Insert(T,newItem):
        if T == None:
            T = BST(newItem)
        elif T.data.word > newItem.word:
            T.left = BST.Insert(T.left,newItem)
        else:
            T.right = BST.Insert(T.right,newItem)
        return T
    
    #Methods from Exercises
    def Find(T, k):
        if T is None:
            return T
        if T.data.word > k:
            return BST.Find(T.left, k)
        if T.data.word < k:
            return BST.Find(T.right, k)
        return T

    def NumNodes(T):
        num = 0
        if T is not None:
            num = 1
        if T.left is not None:
            num += BST.NumNodes(T.left)
        if T.right is not None:
            num += BST.NumNodes(T.right)
        return num
    
    def Height(T):
        h = 0
        if T.left is not None:
            h += 1 + BST.Height(T.left)
        if T.right is not None:
            rH  = 1 + BST.Height(T.right)
            if rH > h:
                h = rH
        return h

class BTree(object):
    def __init__(self,data,child=[],isLeaf=True,max_data=5):  
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data

    def FindChild(T,k):
        # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
        for i in range(len(T.data)):
            if k.word < T.data[i].word:
                return i
        return len(T.data)
                 
    def InsertInternal(T,i):
        # T cannot be Full
        if T.isLeaf:
            BTree.InsertLeaf(T,i)
        else:
            k = BTree.FindChild(T,i)   
            if BTree.IsFull(T.child[k]):
                m, l, r = BTree.Split(T.child[k])
                T.data.insert(k,m) 
                T.child[k] = l
                T.child.insert(k+1,r) 
                k = BTree.FindChild(T,i)  
            BTree.InsertInternal(T.child[k],i)   
                
    def Split(T):
        mid = T.max_data//2
        if T.isLeaf:
            leftChild = BTree(T.data[:mid],max_data=T.max_data) 
            rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
        else:
            leftChild = BTree(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
            rightChild = BTree(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
        return T.data[mid], leftChild,  rightChild   
          
    def InsertLeaf(T,i):
        T.data.append(i)  
        BTree.quicksort(T.data, 0, len(T.data) - 1)
        
    #Partition and quicksort used for sorting leaf nodes in InsertLeaf() method above
    def partition(L, first, last):
        #Assign middle element to pivot
        midpoint = (int)(first + (last - first) / 2);
        pivot = L[midpoint]
        #Create temporary first and last indices
        f = first
        l = last
        #Repeat sorting process until first index is at or below last index
        done = False
        while done == False:
          #Increment f while L[f] < pivot
          while L[f].word < pivot.word:
             f = f + 1
          #Decrement l while pivot < L[l]
          while pivot.word < L[l].word:
             l = l - 1
          #If first index is at or below last index, sorting is finished
          if f >= l:
             done = True
          else:
             #Swap L[f] and L[l]
             L[f], L[l] = L[l], L[f]
             #Increment f and decrement l before continuing through the loop
             f = f + 1
             l = l - 1
        #When loop is done, last index is equal to new index of pivot
        return l;
    def quicksort(L, first, last):
        if first < last:
            p = BTree.partition(L, first, last)
            BTree.quicksort(L, first, p)
            BTree.quicksort(L, p+1, last)
        
    def IsFull(T):
        return len(T.data) >= T.max_data
    
    def Leaves(T):
        # Returns the leaves in a b-tree
        if T.isLeaf:
            return [T.data]
        s = []
        for c in T.child:
            s = s + BTree.Leaves(c)
        return s
            
    def Insert(T,i):
        if not BTree.IsFull(T):
            BTree.InsertInternal(T,i)
        else:
            m, l, r = BTree.Split(T)
            T.data =[m]
            T.child = [l,r]
            T.isLeaf = False
            k = BTree.FindChild(T,i)  
            BTree.InsertInternal(T.child[k],i) 
    
    def Height(T):
        if T.isLeaf:
            return 0
        return 1 + BTree.Height(T.child[0])
    
    def Search(T,k):
        # Returns object that has k from node where k is, or None if k is not in the tree
        for i in range(len(T.data)):
            if T.data[i].word == k:
                return T.data[i]
        if T.isLeaf:
            return None
        return BTree.Search(T.child[BTree.FindChild(T,WordEmbedding(k, []))],k)
            
    #Method from exercises
    def NumNodes(T):
        num = 0
        if T is not None:
            num = 1
        if not T.isLeaf:
            for c in T.child:
                num += BTree.NumNodes(c)
        return num

#My Code
while True:
    #Item 1
    try:#User Prompt
        #Item 2
        #Read file and create tree based on treeChoice
        file = open("/Users/johanncampos369/Downloads/glove.6B/glove.6B.50d.txt", "r")
        #print("Choose a tree implementation. 1 for BST, 2 for B-Tree: ", end = '')
        print("Choose a tree implementation.\nType 1 for binary search tree or 2 for B-tree.")
        treeChoice = int(input("Choice: "))
        #Store each WordEmbedding object in appropriate type of tree
        if treeChoice == 1:
            print("\nBuilding binary search tree")
            start = time.time()
            #Split first line into list of word and emb so that initial BST can be constructed
            firstLine = file.readline()
            words = firstLine.split(" ")
            tree = BST(WordEmbedding(words[0], words[1:]))
            for f in file:
                words = f.split(" ")#Split each remaining line into list of word and emb
                tree.Insert(WordEmbedding(words[0], words[1:]))#Insert new object with word and emb list
            end = time.time()
            #Print stats of resulting BST
            print("\nBinary Search Tree stats: ")
            print("Number of nodes: ", tree.NumNodes())
            print("Height: ", tree.Height())
            print("Running time for binary search tree construction: %.4f" % (end - start))
        elif treeChoice == 2:
            maxItems = int(input("Maximum number of items in node: "))
            print("\nBuilding B-tree")
            start = time.time()
            tree = BTree([], max_data = maxItems)
            for f in file:
                words = f.split(" ")#Split each line into list of word and emb
                tree.Insert(WordEmbedding(words[0], words[1:]))#Insert new object with word and emb list
            end = time.time()
            #Print stats of resulting B-tree
            print("\nB-tree Stats: ")
            print("Number of nodes: ", tree.NumNodes())
            print("Height: ", tree.Height())
            print("Running time for B-tree construction: %.4f" % (end - start))
        else:
            raise Exception()
        break
    except:#If neither 1 nor 2 are entered
        print("Invalid entry.\n")

#Item 3
#Read second file containing pairs of words
print("\nReading word file to determine similarities")
file2 = open("/Users/johanncampos369/Downloads/glove.6B/wordpairs.txt", "r")
#Compare words in file2 line by line, finding them in tree made from first file
print("\nWord similarities found: ")
total = 0.0
lines = file2.read().splitlines()#Make list of lines without \n
for i in range(len(lines)):
    start = time.time()
    words = lines[i].split(" ")#Makes list of two words for given line
    if treeChoice == 1:#BST
        word1 = tree.Find(words[0]).data.emb#Find returns node at which WordEmbedding object containing word is
        word2 = tree.Find(words[1]).data.emb#Thus, we take the embs of the data of said objects
    else:#Previous try-except allows for treeChoice to only be either 1 or 2, thus making this B-Tree
        word1 = tree.Search(words[0]).emb#Search returns WordEmbedding object that contains sought for word
        word2 = tree.Search(words[1]).emb#Thus, we take the embs of the data of said objects
    sim = np.dot(word1, word2) / np.dot(np.linalg.norm(word1), np.linalg.norm(word2))
    end = time.time()
    total += end - start#Accumulates time taken for every similarity comparison
    print("Similarity ", words, " = %.4f" % sim)
if treeChoice == 1:
    print("Running time for binary search tree query processing: %.4f" % total)
else:
    print("Running time for B-tree query processing (with max_items =", maxItems,"): %.4f" % total)
