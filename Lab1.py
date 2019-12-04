# Course: CS 2302 Data Structures
# Date of last modification: November 3
# Assignment: Lab 1 - Recursion
# TA: Anindita Nath
# Professor: Olac Fuentes
# Purpose: The purpose of this lab is to implement recursion 
#          in order to find anagrams of a given word in a list of words.

import sys
import time

def permutation(word): 
    #If word has no letters, no more permutations can be made
    if len(word) == 0: 
        return [] 
    #If word has one letter, only one permuatation (itself) can be made
    if len(word) == 1: 
        return [word] 
    #If word has two or more letters, recursive calls must be made to find permutations
    l = []#List to store all possible permuatations
    #Take each letter of the current part of the word
    for i in range(len(word)):
       m = word[i]
       #Take rest of word that is not current taken letter
       restWord = word[:i] + word[i+1:]
       #Recursively generate list of all possible permutations
       for p in permutation(restWord):
           #Put taken letter in front of each permutation and append to list to return
           l.append(m + p)
    #Return list of all possible permutations after paired with every letter taken
    return l

def anagram(word, word_set):
    anagram_list = []#List to hold necessary anagrams
    #Take each letter from word and place at beginning of potential anagram
    for i in range(len(word)):
        m = word[i]
        #Take remaining letters and begin to form permutations
        remLet = word[:i] + word[i+1:]
        for p in permutation(remLet):
            #Add given permutation to anagram list if it follows current leading letter in word set
            if m+p in word_set and m + p != word:
                anagram_list.append(m + p)
    #Return sorted list for alphabetical order and no duplicates
    return sorted(set(anagram_list))

def permutation_opt(word, prefix_set): 
    #If word has no letters, no more permutations can be made
    if len(word) == 0: 
        return [] 
    #If word has one letter, only one permuatation (itself) can be made
    if len(word) == 1: 
        return [word]
    #If word has two or more letters, recursive calls must be made to find permutations
    l = []#List to store all possible permuatations
    #Take each letter of the current part of the word, starting from last letter
    i = len(word) - 1
    while i > -1:
    #for i in range(len(word)):
       m = word[i]
       #Take rest of word that is not current taken letter
       restWord = word[:i] + word[i+1:]
       #Recursively generate list of all possible permutations
       for p in permutation_opt(restWord,prefix_set):
           #print('p(',restWord,'): ',p,end = ' ')
           #First check if given permutation is remotely within list
           if p in prefix_set:
               #print('Taken!',end=' ')
               #Put taken letter in front of each permutation and append to list to return
               l.append(p+m)
       i-=1
    #Return list of all possible, viable permutations after paired with every letter taken
    return l

def anagram_opt(word, word_set, prefix_set):
    anagram_list = []#List to hold necessary anagrams
    #Take each letter from word and place at beginning of potential anagram
    i = len(word) - 1#Start from last letter and work backwards
    while i > -1:
    #for i in range(len(word)):
        m = word[i]
        #Take remaining letters and begin to form permutations
        remLet = word[:i] + word[i+1:]
        for p in permutation_opt(remLet, prefix_set):
            #print('p:',p)
            #Add given permutation to anagram list if it follows current leading letter in word set
            if p+m in word_set and p+m != word:
                anagram_list.append(p+m)
        i-=1
    #Return sorted list for alphabetical order and no duplicates
    return sorted(set(anagram_list))

if __name__ == "__main__":#main method
    word_file = open("/Users/johanncampos369/Downloads/words_alpha.txt", "r")#access words_alpha.txt
    word_set = set()#create empty set
    
    for line in word_file:#read each word into empty set
        word_set.add(line[:-1])
    while(True):
        word = input('Enter a word or empty string to finish: ')#User Prompt
        if word == '':
            break
        #Unoptimized
        print('Part 1')
        start = time.time()
        anagram_list = anagram(word, word_set)
        end = time.time()
        print('The word',word,'has the following',len(anagram_list),'anagrams:')
        for i in range(len(anagram_list)):
            print(anagram_list[i])
        print('It took %.6f'%(end-start),'seconds to find the anagrams.')
        #Optimized
        print('Part 2')
        word_file = open("/Users/johanncampos369/Downloads/words_alpha.txt", "r")#access words_alpha.txt
        prefix_set = set()
        for line in word_file:#read each word into empty set
            for i in range(len(line) - 1):
                if line[:i] not in prefix_set:
                    prefix_set.add(line[:i])
        start = time.time()
        anagram_list = anagram_opt(word, word_set, prefix_set)
        end = time.time()
        print('The word',word,'has the following',len(anagram_list),'anagrams:')
        for i in range(len(anagram_list)):
            print(anagram_list[i])
        print('It took %.6f'%(end-start),'seconds to find the anagrams.')
    print("Bye, thanks for using this program!")
