# Course: CS 2302 Data Structures
# Date of last modification: September 24
# Assignment: Lab 3 SortedList
# TA: Anindita Nath
# Professor: Olac Fuentes
# Purpose: The purpose of this lab is to implement various methods in a sorted variant of the List class,
#          and compare the big-O running time of each method to those equivalent of the standard List class.

import time
import math

#Code for Node and List Classes provided by Dr. Fuentes
class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None

    def Print(self):
        # Prints list L's items in order using a loop
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()  # New line
        
    #Functions 2 - 10 implemented for Lab 3
    def Insert(self, i):
        start = time.time()
        i = Node(i)
        #If list is empty, assign node i to head and tail
        if self.head is None:
            self.head = i
            self.tail = i
        #Otherwise, insert i as tail.next
        else:
            self.tail.next = i
            #Update tail pointer to i
            self.tail = i
        end = time.time()
        print("\tTime taken(Insert): %.9f" % (end - start))
    
    def Delete(self, i):
        start = time.time()
        #Continue only if list is not empty
        if self.head is not None:
            i = Node(i)
            #Update head pointer if head.data is equal to i.data
            while self.head.data == i.data and self.head is not None:
                self.head = self.head.next
            #Remove remaining non-head, non-tail nodes from list if data is equal to i.data
            temp = self.head
            while temp.next.next is not None:
                if temp.next.data == i.data:
                    temp.next = temp.next.next
                if temp.next.next is not None:
                    temp = temp.next
            #Remove tail (AKA temp.next) if tail.data is equal to i.data
            if temp.next.data == i.data:
                temp.next = None
                #Update tail pointer to node before tail
                self.tail = temp
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
                
    def Merge(self, M):
        start = time.time()
        #Update tail pointer to tail of M
        self.tail.next = M.head
        self.tail = M.tail
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        
    def IndexOf(self, i):
        start = time.time()
        #Traverse list until first instance of i is found
        temp = self.head
        index = 0
        while temp is not None:
            if temp.data == i:
                end = time.time()
                print("\tTime taken: %.9f" % (end - start))
                return index
            index += 1
            temp = temp.next
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        #Return -1 if while loop was not entered since list is empty
        return -1
    
    def Clear(self, i):
        start = time.time()
        #Reset head and tail pointers to null
        self.head = None
        self.tail = None
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        
    def Min(self):
        start = time.time()
        #Traverse the list and keep track of the smallest value
        temp = self.head
        smallestValue = math.inf
        while temp is not None:
            if temp.data < smallestValue:
                smallestValue = temp.data
            temp = temp.next
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        return smallestValue
    
    def Max(self):
        start = time.time()
        #Traverse the list and keep track of the largest value
        temp = self.head
        largestValue = -math.inf
        while temp is not None:
            if temp.data > largestValue:
                largestValue = temp.data
            temp = temp.next
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        return largestValue
    
    def HasDuplicates(self):
        start = time.time()
        #Traverse the list once for each node and check to see if it has a duplicate in entire list
        temp = self.head
        temp2 = self.head
        while temp is not None:
            while temp2 is not None:
                if temp.data == temp2.data and temp is not temp2:
                    end = time.time()
                    print("\tTime taken: %.9f" % (end - start))
                    return True
                temp2 = temp2.next
            temp = temp.next
            temp2 = self.head
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        return False
    
    def Select(self, k):
        start = time.time()
        #Sort list by making a SortedList copy
        lastIndex = -1
        temp = self.head
        sortedSelf = SortedList()
        while temp is not None:
            sortedSelf.Insert(temp.data)
            lastIndex += 1
            temp = temp.next
        #If element sought after is greater than length of list, return math.inf to indicate failure
        if k > lastIndex:
            end = time.time()
            print("\tTime taken: %.9f" % (end - start))
            return math.inf
        i = 0
        temp = sortedSelf.head
        while i < k:
            temp = temp.next
            i += 1
        
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        return temp.data 

#SortedList Class
class SortedList(object):
    # Constructor (Same as List Constructor)
    def __init__(self): 
        self.head = None
        self.tail = None
    
    #Same Print method as provided by Dr.Fuentes
    def Print(self):
        # Prints list L's items in order using a loop
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()  # New line
    
    #Functions 2 - 10 implemented for Lab 3
    def Insert(self, i):
        start = time.time()
        i = Node(i)
        #If list is empty, assign node i to head
        if self.head is None:
            self.head = i
            self.tail = i
        #If i is less than head node, assign node i to head
        elif self.head.data > i.data:
            i.next = self.head
            self.head = i
        #Otherwise, traverse list until node can be placed at proper position
        else:
            temp = self.head
            while temp is not None:
                #If end of list is reached, assign node i to tail and stop traversal
                if temp.next is None:
                    temp.next = i
                    self.tail = i
                    break
                #Once node with larger value is found, insert i and stop traversal
                elif temp.next.data > i.data:
                    i.next = temp.next
                    temp.next = i
                    break
                temp = temp.next
        end = time.time()
        print("\tTime taken(Insert): %.9f" % (end - start))

    def Delete(self, i):
        start = time.time()
        #Only continue if list is not empty and i is within range of sorted list
        if self.head is not None and i >= self.head.data and i <= self.tail.data:
            i = Node(i)
            #Update head pointer if head.data is equal to i.data
            if self.head.data == i.data:
                while self.head.data == i.data and self.head is not None:
                    self.head = self.head.next
            #Otherwise, check nodes until nodes > i, nodes == i, or tail is reached 
            else:
                temp = self.head
                #Traverse list up to node(s) greater than or equal to i
                while temp is not None:
                    if temp.next.data >= i.data:
                        break
                    temp = temp.next
                #Remove all non-tail nodes equal to i
                while temp.next.next is not None and temp.next.data == i.data:
                    temp.next = temp.next.next
                #If tail node equal to i, remove tail
                if temp.next.data == i.data:
                    temp.next = None
                    self.tail = temp
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
                    

    def Merge(self, M):
        start = time.time()
        #Insert data from SortedList M into self with Insert() method, M.data by M.data
        tempM = M.head
        while tempM is not None:
            self.Insert(tempM.data)
            tempM = tempM.next
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        
    def IndexOf(self, i):
        start = time.time()
        #If list is empty or i is out of range, return -1
        if self.head is None or i < self.head.data or i > self.tail.data:
            end = time.time()
            print("\tTime taken: %.9f" % (end - start))
            return -1
        #Otherwise, traverse the list until first instance of i is found
        temp = self.head
        index = 0
        while temp is not None:
            if temp.data == i:
                end = time.time()
                print("\tTime taken: %.9f" % (end - start))
                return index
            index += 1
            temp = temp.next
            
    def Clear(self, i):
        start = time.time()
        #Reset head and tail pointers to null
        self.head = None
        self.tail = None
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
    
    def Min(self):
        start = time.time()
        #If list is empty, return math.inf
        if self.head is None:
            end = time.time()
            print("\tTime taken: %.9f" % (end - start))
            return math.inf
        #Otherwise, return head, the smallest value in a sorted list
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        return self.head.data
    
    def Max(self):
        start = time.time()
        #If list is empty, return -math.inf
        if self.tail is None:
            end = time.time()
            print("\tTime taken: %.9f" % (end - start))
            return -math.inf
        #Otherwise, return tail, the largest value in a sorted list
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        return self.tail.data
    
    def HasDuplicates(self):
        start = time.time()
        #Compare each node with its successor which, in a sorted list, is the only value that could be a duplicate
        temp = self.head
        while temp.next is not None:
            if temp.data == temp.next.data:
                end = time.time()
                print("\tTime taken: %.9f" % (end - start))
                return True
            temp = temp.next
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        return False
    
    def Select(self, k):
        start = time.time()
        temp = self.head
        i = 0
        while i < k:
            if temp is None:
                end = time.time()
                print("\tTime taken: %.9f" % (end - start))
                return math.inf
            temp = temp.next
            i += 1
        end = time.time()
        print("\tTime taken: %.9f" % (end - start))
        return temp.data

#Testing Methods in SortedList()
print("SortedList() Methods")
test = SortedList()

print("Testing Insert()")
test.Insert(49)
test.Insert(-2)
test.Insert(6)
test.Insert(-27)
test.Insert(14)
test.Insert(-27)
test.Insert(50)
test.Insert(14)
test.Print()

print("Testing Select(6)")
print(test.Select(6))
print("Testing Select(4000)")
print(test.Select(4000))

print("Testing HasDuplicates() (True)")
print(test.HasDuplicates())

print("Testing Delete()")
test.Delete(-27)
test.Print()
test.Delete(14)
test.Print()
test.Delete(50)
test.Print()
test.Delete(4000)
test.Print()

#For merge, create second SortedList M that contains no duplicates of its or of current list's elements
print("Creating new list M")
test2 = SortedList()
test2.Insert(42)
test2.Insert(14)
test2.Insert(-27)
test2.Insert(50)
print("Testing Merge(), M: ", end = '')
test2.Print()
test.Merge(test2)
test.Print()

print("Testing IndexOf(50) and IndexOf(4000)")
print(test.IndexOf(50))
print(test.IndexOf(4000))

print("Testing Min()")
print(test.Min())

print("Testing Max()")
print(test.Max())

print("Testing HasDuplicates() (False)")
print(test.HasDuplicates())

print("Testing Clear(0)")
test.Clear(0)
test.Print()

print("Testing Min() of empty list")
print(test.Min())

print("Testing Max() of empty list")
print(test.Max())

#Testing Methods in List()
print("\nList Methods")
test = List()

print("Testing Insert()")
test.Insert(49)
test.Insert(-2)
test.Insert(6)
test.Insert(-27)
test.Insert(14)
test.Insert(-27)
test.Insert(50)
test.Insert(14)
test.Print()

print("Testing Select(6)")
print(test.Select(6))
print("Testing Select(4000)")
print(test.Select(4000))

print("Testing HasDuplicates() (True)")
print(test.HasDuplicates())

print("Testing Delete()")
test.Delete(-27)
test.Print()
test.Delete(14)
test.Print()
test.Delete(50)
test.Print()
test.Delete(4000)
test.Print()

#For merge, create second list M that contains no duplicates of its or of current list's elements
print("Creating new list M")
test2 = List()
test2.Insert(42)
test2.Insert(14)
test2.Insert(-27)
test2.Insert(50)
print("Testing Merge(), M: ", end = '')
test2.Print()
test.Merge(test2)
test.Print()

print("Testing IndexOf(50) and IndexOf(4000)")
print(test.IndexOf(50))
print(test.IndexOf(4000))

print("Testing Min()")
print(test.Min())

print("Testing Max()")
print(test.Max())

print("Testing HasDuplicates() (False)")
print(test.HasDuplicates())

print("Testing Clear(0)")
test.Clear(0)
test.Print()

print("Testing Min() of empty list")
print(test.Min())

print("Testing Max() of empty list")
print(test.Max())
