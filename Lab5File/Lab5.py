# Course: CS 2302 Data Structures
# Date of last modification: December 5
# Assignment: Lab 5 Hash Table w/ Chaining/Linear Probing
# TA: Anindita Nath
# Professor: Olac Fuentes
# Purpose: The purpose of this lab is to implement hash tables with chaining and with linear probing in place of
#           BSTs and B-trees to compare the running times of all said data structures.

import numpy as np
import time

#WordEmbedding, HashTableChain, and HashTableLP classes provided by Dr. Fuentes
class WordEmbedding(object):
    def __init__(self,word,embedding):
        # word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32)

class HashTableChain(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size, c = 0):  
        self.bucket = [[] for i in range(size)]
        self.c = c
        
    def h(self,k):
        #Part 1
        #The length of the string % n
        if self.c == 1:
            return len(k.word) % len(self.bucket)
        #The ascii value (ord(c)) of the first character in the string % n
        elif self.c == 2:
            return ord(k.word[0]) % len(self.bucket)
        #The product of the ascii values of the first and last characters in the string % n
        elif self.c == 3:
            return (ord(k.word[0]) * ord(k.word[-1])) % len(self.bucket)
        #The sum of the ascii values of the characters in the string % n
        elif self.c == 4:
            ordAll = 0
            for l in range(len(k.word)):
                ordAll += ord(k.word[l])
            return ordAll % len(self.bucket)
        #The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n
        elif self.c == 5:
            if k.word == '':
                return 1
            else:
                s = WordEmbedding(k.word[1:], 0)
                return (ord(k.word[0]) + 255 * self.h(s)) % len(self.bucket)
        #Another function of your choice(The product of ascii values of characters in string % n)
        else:
            return (ord(k.word[0]) % ord(k.word[-1])) % len(self.bucket)
                                 #to sort WordEmbedding objects alphabetically by ASCII value

    def insert(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        b = self.h(k)
        if not k.word in self.bucket[b]:#Modified "k" to "k.word" for proper detection
            self.bucket[b].append(k)         #Insert new item at the end
            
    def find(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h(k)
        try:
            i = self.bucket[b].index(k)
        except:
            i = -1
        return b, i
     
    def print_table(self):
        print('Table contents:')
        for b in self.bucket:
            print(b)
    
    def delete(self,k):
        # Returns k from appropriate list
        # Does nothing if k is not in the table
        # Returns 1 in case of a successful deletion, -1 otherwise
        b = self.h(k)
        try:
            self.bucket[b].remove(k)
            return 1
        except:
            return -1
        
class HashTableLP(object):
    # Builds a hash table of size 'size', initilizes items to -1 (which means empty)
    # Constructor
    def __init__(self,size,c = 0):  
        self.item = np.zeros(size,dtype=np.int)-1
        self.c = c
        
    def insert(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        for i in range(len(self.item)): #Despite for loop, running time should be constant for table with low load factor
            pos = self.h(k)+i
            numK = []
            for i in range(len(k.emb)):
                numK = ''.join(str(k.emb[i]))
            numK = float(numK)
            if self.item[pos] < 0:
                self.item[pos] = numK
                return pos
        return -1
    
    def find(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        for i in range(len(self.item)):
            pos = self.h(k)+i
            if self.item[pos] == k:
                return pos
            if self.item[pos] == -1:
                return -1
        return -1
     
    def delete(self,k):
        # Deletes k from table. It returns the position where k was, or -1 if k was not in the table
        # Sets table item where k was to -2 (which means deleted)
        f = self.find(k)
        if f >=0:
            self.item[f] = -2
        return f
    
    def h(self,k):
        #Part 1
        #The length of the string % n
        if self.c == 1:
            return len(k.word) % len(self.item)
        #The ascii value (ord(c)) of the first character in the string % n
        elif self.c == 2:
            return ord(k.word[0]) % len(self.item)
        #The product of the ascii values of the first and last characters in the string % n
        elif self.c == 3:
            return (ord(k.word[0]) * ord(k.word[-1])) % len(self.item)
        #The sum of the ascii values of the characters in the string % n
        elif self.c == 4:
            ordAll = 0
            for l in range(len(k.word)):
                ordAll += ord(k.word[l])
            return ordAll % len(self.item)
        #The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n
        elif self.c == 5:
            if k.word == '':
                return 1
            else:
                s = WordEmbedding(k.word[1:], 0)
                return (ord(k.word[0]) + 255 * self.h(s)) % len(self.item)
        #Another function of your choice
        else:
            return #Modified "k%len(self.bucket)" to "ord(k.word[0])"
                                 #to sort WordEmbedding objects alphabetically by ASCII value
            
    
    def print_table(self):
        print('Table contents:')
        for b in self.bucket:
            print(b)

#My Code
if __name__ == "__main__":
    #Read file and create table based on tableChoice
    file = open("/Users/johanncampos369/Downloads/glove.6B/glove.6B.50d.txt", "r")
    
    while(True):
        print("Choose a hash table implementation.\nType 1 for chaining or 2 for linear probing.")
        tableChoice = int(input("Choice: "))
        print("Choose a hash function corresponding to Part 1 (1-6): ")
        c = int(input("Choice: "))
        #Store each WordEmbedding object in appropriate type of table
        if tableChoice == 1:
            start = time.time()
            htc = HashTableChain(255, c)#Set size to 255 to get buckets corresponding to ASCII values
                                        #Set c to determine which hash function to use.
            for f in file:
                words = f.split(" ")
                htc.insert(WordEmbedding(words[0], words[1:]))#Insert new object with word and emb list
            end = time.time()
            #Print stats of resulting 
            print("\nHash Table Chain stats: ")
            print("Running time for hash table chain construction: %.4f" % (end - start))
            break
        elif tableChoice == 2:
            #size = int(input(("Enter size of htlp: ")))
            print("\nBuilding Hash Table w/ Linear Probing.")
            start = time.time()
            htlp = HashTableLP(400001, c)
            for f in file:
                words = f.split(" ")#Split each line into list of word and emb
                htlp.insert(WordEmbedding(words[0], words[1:]))#Insert new object with word and emb list
            end = time.time()
            #Print stats of resulting B-tree
            print("\nHash Table LP Stats: ")
            print("Running time for hash table LP construction: %.4f" % (end - start))
            break
        else:
            print("Invalid entry. Please try again.")
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
        if tableChoice == 1:#htc
            word1b, word1i = htc.find(WordEmbedding(words[0], 0))#find returns bucket and index of WordEmbedding objects
            word2b, word2i = htc.find(WordEmbedding(words[1], 0))
            #Take necessary numbers to calculate similarity based on emb by accessing htc elements via bucket and index
            top = np.dot(htc.bucket[word1b][word1i].emb, htc.bucket[word2b][word2i].emb)
            bottom = np.dot(np.linalg.norm(htc.bucket[word1b][word1i].emb), np.linalg.norm(htc.bucket[word2b][word2i].emb))
        else:#Previous try-except allows for tableChoice to only be either 1 or 2, thus making this htlp
            word1 = htlp.find(WordEmbedding(words[0],0))#find returns index of WordEmbedding object that contains sought for word
            word2 = htlp.find(WordEmbedding(words[1],0))
            #Take necessary numbers to calculate similarity based on emb by accessing htlp elements via index
            top = np.dot(htlp.item[word1], htlp.item[word2])
            bottom = np.dot(np.linalg.norm(htlp.item[word1]), np.linalg.norm(htlp.item[word2]))
        #Calculate similarity based on emb from objects of either table
        sim = top / bottom
        end = time.time()
        total += end - start#Accumulates time taken for every similarity comparison
        print("Similarity ", words, " = %.4f" % sim)
    if tableChoice == 1:
        print("Running time for hash table chain query processing: %.4f" % total)
    else:
        print("Running time for hash table LP query processing: %.4f" % total)
