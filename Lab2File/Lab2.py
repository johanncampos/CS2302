# Course: CS 2302 Data Structures
# Date of last modification: September 24
# Assignment: Lab 2 Quicksort
# TA: Anindita Nath
# Professor: Olac Fuentes
# Purpose: The purpose of this lab is to write algorithms that each properly find the smallest value of a given list,
#          and to then understand the relationship between the different implementations and their big-O running time
#          via experimental results.

import time

#Global variable for counting comparisons in all algorithms
count = 0

#Part 1

#1. Bubblesort Call
def select_bubble(L, k):
    #If element sought after is greater than length of list, return -1 to indicate failure
    start = time.time()
    if not L:
        print("\t\tList is empty.")
        return None
    if k > len(L) or k < 0:
        print("\t\tIndex is outside range.")
        return None
    global count
    count = 0
    #Take first element of unsorted portion of list
    LCopy = list()
    for i in range(len(L)):
        LCopy.append(L[i])
    for i in range(len(LCopy)):
        #Take each following element of unsorted portion of list
        for j in range(len(LCopy)):
            #Swap two elements if current first 
            #is less than given following element
            count += 1
            if LCopy[i] < LCopy[j]:
                LCopy[i], LCopy[j] = LCopy[j], LCopy[i]
    #Return sought for element after entire list is sortedw
    print("\t\tComparisons: ", count)
    end = time.time()
    total = end - start
    print("\t\tTime taken: %.6f" % total)
    return LCopy[k]

#Partition (used in both Recursive Quicksort and Recursive Modified Quicksort)
def partition(L, first, last):
    global count
    #Assign middle element to pivot
    midpoint = (int)(first + (last - first) / 2);
    #Create temporary first and last indices
    f = first
    l = last
    #Repeat sorting process until first index is at or below last index
    done = False
    while done == False:
      pivot = L[midpoint]
      #Increment f while L[f] < pivot
      while L[f] < pivot:
         f = f + 1
      #Decrement l while pivot < L[l]
      while pivot < L[l]:
         l = l - 1
      #If first index is at or below last index, sorting is finished
      count += 1
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

#Recursive Quicksort
def quicksort(L, first, last):
    #Begin recursive calls to quicksort 
    #if current portion of list has more than one element
#    global count
#    count += 1
    if first < last:
        #Sort portion of list
        p = partition(L, first, last)
        #Sort left half of list
        quicksort(L, first, p)
        #Sort right half of list
        quicksort(L, p+1, last)
        
#2. Quicksort Call
def select_quick(L, k):
    #If element sought after is greater than length of list, return -1 to indicate failure
    start = time.time()
    if not L:
        return None
    if k > len(L) or k < 0:
        print("\t\tIndex is outside range.")
        return None
    #Make copy of list
    LCopy = list()
    for i in range(len(L)):
        LCopy.append(L[i])
    #Quicksort entire list
    global count
    count = 0
    quicksort(LCopy, 0, len(L) - 1)
    print("\t\tComparisons: ", count)
    end = time.time()
    total = end - start
    print("\t\tTotal time: %.6f" % total)
    return LCopy[k]

#Recursive Modified Quicksort
def modified_quicksort(L, first, last, k):
#    global count
#    count += 1
    if first < last:
        p = partition(L, first, last)
        if p >= k:
            modified_quicksort(L, first, p, k)
        elif p < k:
            modified_quicksort(L, p+1, last, k)

#3. Modified Quicksort Call
def select_modified_quick(L, k):
    #If element sought after is greater than length of list, return -1 to indicate failure
    start = time.time()
    if not L:
        return None
    if k > len(L) or k < 0:
        print("\t\tIndex is outside range.")
        return None
    #Make copy of list
    LCopy = list()
    for i in range(len(L)):
        LCopy.append(L[i])
    #Modified_quicksort entire list
    global count
    count = 0
    modified_quicksort(LCopy, 0, len(L) - 1, k)
    print("\t\tComparisons: ", count)
    end = time.time()
    total = end - start
    print("\t\tTotal time: %.6f" % total)
    return LCopy[k]

#Part 2
    
#Partition Index (Used in both Stack Quicksort and While Modified Quicksort)
def partition_index(L, first, last):
    global count
    pivotIndex = first - 1
    lastValue = L[last]
    for i in range(first, last):
        #Find a value smaller than last value, and if found, swap with bigger value before it
        count += 1
        if L[i] <= lastValue:
            pivotIndex += 1
            L[pivotIndex], L[i] = L[i], L[pivotIndex]
    #Swap last value with bigger value
    L[pivotIndex + 1], L[last] = L[last], L[pivotIndex + 1]
    #Return last index
    return pivotIndex+1

#Stack Quicksort
def stack_quicksort(L, first, last): 
    #Place first and last indices in stack, last over first
    stack = []
    stack.append(first)
    stack.append(last)
    #Repeat index removal until no indices remain
    while len(stack) > 0:
        #print("stack: ", stack)
        #Remove both indices in appropriate order
        last = stack.pop()
        first = stack.pop()
        #Sort left half of list within first and last indices
        p = partition_index(L, first, last)
        #If pivot index is greater than first index, refill stack with first index and index before pivot index
        #This represents the left half of the list
        if(p - 1 > first):
            stack.append(first)
            stack.append(p - 1)
        #If pivot index is less than last index, refill stack with index after pivot index and last index
        #This represents the right half of the list
        if(p + 1 < last):
            stack.append(p + 1)
            stack.append(last)

#4. Stack Quicksort Call
def select_stack_quick(L, k):
    #If element sought after is greater than length of list, return -1 to indicate failure
    start = time.time()
    if not L:
        return None
    if k > len(L) or k < 0:
        print("\t\tIndex is outside range.")
        return None
    #Make copy of list
    LCopy = list()
    for i in range(len(L)):
        LCopy.append(L[i])
    #Stack_quicksort entire list
    global count
    count = 0
    stack_quicksort(LCopy, 0, len(L) - 1)
    #Print number of comparisons
    print("\t\tComparisons: ", count)
    end = time.time()
    total = end - start
    print("\t\tTotal time: %.6f" % total)
    return LCopy[k]

#While Loop Modified Quicksort 
def while_modified_quicksort(L, first, last, k):
    p = partition_index(L, first, last)
    while p != k:
        if(p > k):
            p = partition_index(L, first, p - 1)
        elif(p < k):
            p = partition_index(L, p + 1, last)
    return L[k]

#While Modified Quicksort Call
def select_while_modified_quick(L, k):
    #If element sought after is greater than length of list, return -1 to indicate failure
    start = time.time()
    if not L:
        return None
    if k > len(L) or k < 0:
        print("\t\tIndex is outside range.")
        return None
    LCopy = list()
    for i in range(len(L)):
        LCopy.append(L[i])
    global count
    count = 0
    while_modified_quicksort(L, 0, len(L) - 1, k)
    print("\t\tComparisons: ", count)
    end = time.time()
    total = end - start
    print("\t\tTotal time: %.6f" % total)
    return L[k]

#Part 1
#Bubblesort
print("Bubble Sort: ")
#Test empty list
test = []
print("\nTesting empty list, Index: ", 0)
print("\t\tElement is: ", select_bubble(test, 0))
#Test list w/ 10 elements
test = [1, 6, 2, 10, 3, 9, 7, 4, 8, 5]
#Test invalid index
print("\nTesting list w/ 10 elements, Index: ", -1)
print("\t\tElement is: ", select_bubble(test, -1))
#Test last index
print("\nTesting list w/ 10 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_bubble(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 10 elements, Index: ", 0)
print("\t\tElement is: ", select_bubble(test, 0))
#Test middle index
print("\nTesting list w/ 10 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_bubble(test, (len(test) - 1)//2))
#Test list w/ 100 elements
test = [66, 56, 7, 80, 87, 55, 15, 94, 20, 30, 24, 50, 10, 83, 53, 34, 40, 16, 26, 76, 92,
        48, 31, 27, 49, 82, 44, 0, 35, 36, 60, 93, 71, 32, 5, 47, 41, 33, 28, 46, 68, 67,
        37, 95, 11, 45, 84, 63, 1, 99, 6, 13, 98, 54, 17, 79, 85, 90, 21, 81, 62, 8, 19,14,
        23, 29, 9, 74, 91, 39, 69, 38, 25, 70, 12, 22, 52, 89, 75, 77, 73, 59, 4, 57, 2, 72,
        58, 78, 86, 43, 42, 96, 65, 88, 51, 18, 97, 61, 64, 3]
#Test last index
print("\nTesting list w/ 100 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_bubble(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 100 elements, Index: ", 0)
print("\t\tElement is: ", select_bubble(test, 0))
#Test middle index
print("\nTesting list w/ 100 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_bubble(test, (len(test) - 1)//2))
#Test list w/ 1000 elements
test = [ 761,    77,   665,   912,   735,   204,   232,   392,   457,   372, 
         169,    88,   599,   174,   487,   237,    39,   744,   406,   853,
         822,   650,   557,   170,   282,   620,   933,   514,    24,   532,
         281,   528,   880,   867,   595,   116,   136,   316,   710,   592,
         705,   998,   548,   707,   657,    27,   971,   790,   364,   297,
         563,   996,   764,   339,   641,   833,    44,   416,   508,   699,
         824,    64,   910,   308,   766,   486,   837,   943,   581,   763,
         262,   819,     2,   603,   239,     8,   129,   956,   186,   153,
         894,   538,   300,   846,   555,   358,   751,   816,   934,   544,
         724,   385,   271,   131,   353,   443,   938,   515,   451,   461,
         923,   311,   327,    94,   810,   211,   951,   433,   773,   340,
         417,   103,   166,   124,   654,   738,     3,   963,   458,   243,
         524,   474,    15,   804,   906,   442,   448,   957,   125,    43,
           9,   143,   628,   101,   468,   931,   789,   471,   962,   993,
         579,    26,   179,   578,   550,   689,   842,   574,   924,   877,
         848,   902,   704,   736,   376,   613,   369,   497,   975,   731,
         640,    80,   445,    46,   897,   834,   940,   401,   276,   412,
         283,   676,   172,   410,   695,   747,   739,   292,    58,   690,
         407,   110,   226,   331,   507,   512,   720,   757,   767,   825,
         355,   227,    10,   682,   980,   245,   498,   119,   632,   748,
         462,   255,   892,   301,   839,   138,   195,   240,   205,    53,
         114,   534,   829,   793,   459,   950,    98,   911,   264,    35,
         396,   554,   732,   249,   854,   694,   981,   164,    40,   875,
         881,   874,   955,   493,   404,   684,   772,   370,   248,    41,
         435,   759,   350,   835,   251,   500,   831,   286,   585,   201,
         161,   228,   740,   444,   658,   999,   769,   155,   711,   779,
         122,   415,   347,   527,   634,   898,   631,   545,   509,   291,
         193,   158,   389,   202,   304,   796,   882,   984,   216,   241,
         197,   623,   290,    34,   564,   115,   336,   974,    66,   489,
         754,   818,   441,   151,   787,   348,   883,    70,   345,   258,
         495,   231,   917,   360,   257,   536,   821,   750,   333,   289,
         171,    71,   485,   652,   323,   130,   797,   148,   588,   591,
         296,   386,   838,   338,   760,    22,   382,   855,   113,   572,
         850,    13,   567,   602,   379,   187,   212,   942,   845,    85,
         653,   728,   480,   925,   106,   961,   484,   896,    76,   828,
         893,   380,   436,   428,   782,   876,    95,   521,   413,   244,
         446,   671,   225,   247,   375,   402,   213,   150,   185,    29,
         268,   768,   270,   464,    37,   719,   843,   181,   667,   721,
         651,   215,   518,   180,   233,   614,   982,   176,   108,   807,
         997,   809,    47,   778,   619,   647,    67,   196,   117,   781,
         642,   183,   306,   708,   920,   277,   915,   496,   625,   713,
         985,   329,   165,   189,   414,   102,   558,   817,   659,   363,
         167,   491,   664,   646,    49,    12,   879,   856,    75,   274,
         173,   678,   944,    62,   844,   774,   419,   287,   672,   571,
         847,   299,    45,   899,    79,   542,   907,   742,   279,   252,
         863,   470,   969,   629,   655,   337,    23,   683,   222,   639,
         594,   887,   702,   666,   393,   149,    56,   775,   447,   147,
         288,   466,   878,   872,   703,   752,   284,   823,   156,   328,
         930,   992,   870,   673,   107,   517,    68,   315,   648,   709,
         743,   321,   792,   987,   675,   965,   325,   706,   530,   427,
         134,    83,    33,   686,   582,   903,  1000,   391,   697,   377,
         715,    31,    42,   604,   668,   373,   936,   723,   452,   952,
         207,     5,   589,   109,    84,    11,   139,   756,   700,   309,
         937,   749,   200,   783,   543,   994,   901,   206,   669,   140,
         294,   945,   182,   688,   168,   857,   976,   627,   141,   492,
         593,   577,   904,   312,   785,   400,   298,   511,   596,   522,
         234,   356,   909,   820,   873,   539,   209,   836,   939,   886,
         469,   849,   472,   959,   272,   569,   429,   800,   192,   948,
         367,   278,   583,   157,   431,   194,   601,   729,   794,   421,
         805,   871,   718,   786,   388,   953,   408,   622,   972,   858,
         784,    92,   440,   630,   502,   242,    69,   926,   454,   467,
         803,   701,   230,   302,   888,   905,   770,   615,    63,   889,
          93,   954,   529,   662,   977,   973,   541,   922,   811,   293,
         798,   253,   727,   403,   860,   776,   989,   335,   351,   758,
         832,    59,   162,   941,   269,   815,    89,    96,   568,   295,
         152,   482,   319,    17,   891,    19,   565,   163,   737,   535,
         420,   354,    82,   691,   146,   626,   198,   612,   679,   361,
         142,   730,   343,   449,   960,   132,   390,     7,   733,   256,
         562,   575,   516,   916,   546,   145,   621,    30,   580,   318,
         199,   605,   259,   970,   734,    55,   597,   128,   357,   520,
         313,   175,   504,   801,   552,   127,   395,   477,   610,   547,
         456,    48,   394,   929,   722,   598,   303,    14,   488,   908,
         238,   214,   978,   884,   827,    57,   123,   624,   865,   741,
         223,   506,   526,   914,   481,    60,    38,   366,   795,    21,
         932,   463,    78,    65,   553,   814,   365,   725,   104,   334,
         533,   317,   799,   280,   144,   714,    91,   120,   220,   967,
         864,   812,   966,   349,   556,   266,   422,   566,   342,   777,
         424,   362,   928,   432,   895,   649,   217,   949,   235,   483,
         990,   322,   159,   411,    74,    52,   802,   830,   381,   531,
          16,   154,   551,    72,    86,   869,   921,   927,   762,   946,
         218,   112,   320,    51,     6,   344,   285,   371,    50,   273,
         137,    81,   712,   341,   191,   885,   221,     4,   765,   935,
         638,   918,   913,    54,   160,   637,   606,   438,   586,   983,
         746,   409,    87,   378,   986,   852,   616,   726,   560,   771,
         851,   229,   246,   717,   118,   236,   780,   890,   958,   455,
         184,   178,    36,   525,   523,   561,   418,   479,   919,   250,
         587,   510,   968,   608,   453,   687,   437,   224,    32,   135,
          90,   549,     1,    97,   105,   590,    18,   397,   423,   991,
         434,   617,   540,   806,   584,   426,    61,   635,   210,   813,
         490,   260,   670,   439,   861,   501,    20,   600,   460,   121,
         753,   126,   368,   346,   868,   203,   359,   473,   398,   900,
         656,   383,   573,   324,   100,    73,   387,   696,   862,   826,
         788,   840,   494,   576,   677,   964,   133,   188,   607,   305,
         681,   505,   450,   476,   609,   111,   674,   519,   208,   808,
         465,   499,   384,   643,   636,   633,   698,   663,   645,   995,
         660,   693,    99,   618,   503,   265,   190,   611,   399,   352,
         979,   310,   513,   559,   267,   644,   478,   685,   219,   475,
         307,   661,   263,   261,   692,   866,   755,   275,    28,   947,
         332,   405,   841,   745,   430,   791,    25,   425,   314,   537,
         570,   988,   254,   374,   177,   859,   716,   326,   680,   330]
#Test last index
print("\nTesting list w/ 1000 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_bubble(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 1000 elements, Index: ", 0)
print("\t\tElement is: ", select_bubble(test, 0))
#Test middle index
print("\nTesting list w/ 1000 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_bubble(test, (len(test) - 1)//2))

#Quicksort
print("Quicksort: ")
#Test empty list
test = []
print("\nTesting empty list, Index: ", 0)
print("\t\tElement is: ", select_quick(test, 0))
#Test list w/ 10 elements
test = [1, 6, 2, 10, 3, 9, 7, 4, 8, 5]
#Test invalid index
print("\nTesting list w/ 10 elements, Index: ", -1)
print("\t\tElement is: ", select_quick(test, -1))
#Test last index
print("\nTesting list w/ 10 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 10 elements, Index: ", 0)
print("\t\tElement is: ", select_quick(test, 0))
#Test middle index
print("\nTesting list w/ 10 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_quick(test, (len(test) - 1)//2))
#Test list w/ 100 elements
test = [66, 56, 7, 80, 87, 55, 15, 94, 20, 30, 24, 50, 10, 83, 53, 34, 40, 16, 26, 76, 92,
        48, 31, 27, 49, 82, 44, 0, 35, 36, 60, 93, 71, 32, 5, 47, 41, 33, 28, 46, 68, 67,
        37, 95, 11, 45, 84, 63, 1, 99, 6, 13, 98, 54, 17, 79, 85, 90, 21, 81, 62, 8, 19,14,
        23, 29, 9, 74, 91, 39, 69, 38, 25, 70, 12, 22, 52, 89, 75, 77, 73, 59, 4, 57, 2, 72,
        58, 78, 86, 43, 42, 96, 65, 88, 51, 18, 97, 61, 64, 3]
#Test last index
print("\nTesting list w/ 100 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 100 elements, Index: ", 0)
print("\t\tElement is: ", select_quick(test, 0))
#Test middle index
print("\nTesting list w/ 100 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_quick(test, (len(test) - 1)//2))
#Test list w/ 1000 elements
test = [ 761,    77,   665,   912,   735,   204,   232,   392,   457,   372, 
         169,    88,   599,   174,   487,   237,    39,   744,   406,   853,
         822,   650,   557,   170,   282,   620,   933,   514,    24,   532,
         281,   528,   880,   867,   595,   116,   136,   316,   710,   592,
         705,   998,   548,   707,   657,    27,   971,   790,   364,   297,
         563,   996,   764,   339,   641,   833,    44,   416,   508,   699,
         824,    64,   910,   308,   766,   486,   837,   943,   581,   763,
         262,   819,     2,   603,   239,     8,   129,   956,   186,   153,
         894,   538,   300,   846,   555,   358,   751,   816,   934,   544,
         724,   385,   271,   131,   353,   443,   938,   515,   451,   461,
         923,   311,   327,    94,   810,   211,   951,   433,   773,   340,
         417,   103,   166,   124,   654,   738,     3,   963,   458,   243,
         524,   474,    15,   804,   906,   442,   448,   957,   125,    43,
           9,   143,   628,   101,   468,   931,   789,   471,   962,   993,
         579,    26,   179,   578,   550,   689,   842,   574,   924,   877,
         848,   902,   704,   736,   376,   613,   369,   497,   975,   731,
         640,    80,   445,    46,   897,   834,   940,   401,   276,   412,
         283,   676,   172,   410,   695,   747,   739,   292,    58,   690,
         407,   110,   226,   331,   507,   512,   720,   757,   767,   825,
         355,   227,    10,   682,   980,   245,   498,   119,   632,   748,
         462,   255,   892,   301,   839,   138,   195,   240,   205,    53,
         114,   534,   829,   793,   459,   950,    98,   911,   264,    35,
         396,   554,   732,   249,   854,   694,   981,   164,    40,   875,
         881,   874,   955,   493,   404,   684,   772,   370,   248,    41,
         435,   759,   350,   835,   251,   500,   831,   286,   585,   201,
         161,   228,   740,   444,   658,   999,   769,   155,   711,   779,
         122,   415,   347,   527,   634,   898,   631,   545,   509,   291,
         193,   158,   389,   202,   304,   796,   882,   984,   216,   241,
         197,   623,   290,    34,   564,   115,   336,   974,    66,   489,
         754,   818,   441,   151,   787,   348,   883,    70,   345,   258,
         495,   231,   917,   360,   257,   536,   821,   750,   333,   289,
         171,    71,   485,   652,   323,   130,   797,   148,   588,   591,
         296,   386,   838,   338,   760,    22,   382,   855,   113,   572,
         850,    13,   567,   602,   379,   187,   212,   942,   845,    85,
         653,   728,   480,   925,   106,   961,   484,   896,    76,   828,
         893,   380,   436,   428,   782,   876,    95,   521,   413,   244,
         446,   671,   225,   247,   375,   402,   213,   150,   185,    29,
         268,   768,   270,   464,    37,   719,   843,   181,   667,   721,
         651,   215,   518,   180,   233,   614,   982,   176,   108,   807,
         997,   809,    47,   778,   619,   647,    67,   196,   117,   781,
         642,   183,   306,   708,   920,   277,   915,   496,   625,   713,
         985,   329,   165,   189,   414,   102,   558,   817,   659,   363,
         167,   491,   664,   646,    49,    12,   879,   856,    75,   274,
         173,   678,   944,    62,   844,   774,   419,   287,   672,   571,
         847,   299,    45,   899,    79,   542,   907,   742,   279,   252,
         863,   470,   969,   629,   655,   337,    23,   683,   222,   639,
         594,   887,   702,   666,   393,   149,    56,   775,   447,   147,
         288,   466,   878,   872,   703,   752,   284,   823,   156,   328,
         930,   992,   870,   673,   107,   517,    68,   315,   648,   709,
         743,   321,   792,   987,   675,   965,   325,   706,   530,   427,
         134,    83,    33,   686,   582,   903,  1000,   391,   697,   377,
         715,    31,    42,   604,   668,   373,   936,   723,   452,   952,
         207,     5,   589,   109,    84,    11,   139,   756,   700,   309,
         937,   749,   200,   783,   543,   994,   901,   206,   669,   140,
         294,   945,   182,   688,   168,   857,   976,   627,   141,   492,
         593,   577,   904,   312,   785,   400,   298,   511,   596,   522,
         234,   356,   909,   820,   873,   539,   209,   836,   939,   886,
         469,   849,   472,   959,   272,   569,   429,   800,   192,   948,
         367,   278,   583,   157,   431,   194,   601,   729,   794,   421,
         805,   871,   718,   786,   388,   953,   408,   622,   972,   858,
         784,    92,   440,   630,   502,   242,    69,   926,   454,   467,
         803,   701,   230,   302,   888,   905,   770,   615,    63,   889,
          93,   954,   529,   662,   977,   973,   541,   922,   811,   293,
         798,   253,   727,   403,   860,   776,   989,   335,   351,   758,
         832,    59,   162,   941,   269,   815,    89,    96,   568,   295,
         152,   482,   319,    17,   891,    19,   565,   163,   737,   535,
         420,   354,    82,   691,   146,   626,   198,   612,   679,   361,
         142,   730,   343,   449,   960,   132,   390,     7,   733,   256,
         562,   575,   516,   916,   546,   145,   621,    30,   580,   318,
         199,   605,   259,   970,   734,    55,   597,   128,   357,   520,
         313,   175,   504,   801,   552,   127,   395,   477,   610,   547,
         456,    48,   394,   929,   722,   598,   303,    14,   488,   908,
         238,   214,   978,   884,   827,    57,   123,   624,   865,   741,
         223,   506,   526,   914,   481,    60,    38,   366,   795,    21,
         932,   463,    78,    65,   553,   814,   365,   725,   104,   334,
         533,   317,   799,   280,   144,   714,    91,   120,   220,   967,
         864,   812,   966,   349,   556,   266,   422,   566,   342,   777,
         424,   362,   928,   432,   895,   649,   217,   949,   235,   483,
         990,   322,   159,   411,    74,    52,   802,   830,   381,   531,
          16,   154,   551,    72,    86,   869,   921,   927,   762,   946,
         218,   112,   320,    51,     6,   344,   285,   371,    50,   273,
         137,    81,   712,   341,   191,   885,   221,     4,   765,   935,
         638,   918,   913,    54,   160,   637,   606,   438,   586,   983,
         746,   409,    87,   378,   986,   852,   616,   726,   560,   771,
         851,   229,   246,   717,   118,   236,   780,   890,   958,   455,
         184,   178,    36,   525,   523,   561,   418,   479,   919,   250,
         587,   510,   968,   608,   453,   687,   437,   224,    32,   135,
          90,   549,     1,    97,   105,   590,    18,   397,   423,   991,
         434,   617,   540,   806,   584,   426,    61,   635,   210,   813,
         490,   260,   670,   439,   861,   501,    20,   600,   460,   121,
         753,   126,   368,   346,   868,   203,   359,   473,   398,   900,
         656,   383,   573,   324,   100,    73,   387,   696,   862,   826,
         788,   840,   494,   576,   677,   964,   133,   188,   607,   305,
         681,   505,   450,   476,   609,   111,   674,   519,   208,   808,
         465,   499,   384,   643,   636,   633,   698,   663,   645,   995,
         660,   693,    99,   618,   503,   265,   190,   611,   399,   352,
         979,   310,   513,   559,   267,   644,   478,   685,   219,   475,
         307,   661,   263,   261,   692,   866,   755,   275,    28,   947,
         332,   405,   841,   745,   430,   791,    25,   425,   314,   537,
         570,   988,   254,   374,   177,   859,   716,   326,   680,   330]
#Test last index
print("\nTesting list w/ 1000 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 1000 elements, Index: ", 0)
print("\t\tElement is: ", select_quick(test, 0))
#Test middle index
print("\nTesting list w/ 1000 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_quick(test, (len(test) - 1)//2))

#Modified Quicksort
print("Modified Quicksort: ")
#Test empty list
test = []
print("\nTesting empty list, Index: ", 0)
print("\t\tElement is: ", select_modified_quick(test, 0))
#Test list w/ 10 elements
test = [1, 6, 2, 10, 3, 9, 7, 4, 8, 5]
#Test invalid index
print("\nTesting list w/ 10 elements, Index: ", -1)
print("\t\tElement is: ", select_modified_quick(test, -1))
#Test last index
print("\nTesting list w/ 10 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_modified_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 10 elements, Index: ", 0)
print("\t\tElement is: ", select_modified_quick(test, 0))
#Test middle index
print("\nTesting list w/ 10 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_modified_quick(test, (len(test) - 1)//2))
#Test list w/ 100 elements
test = [66, 56, 7, 80, 87, 55, 15, 94, 20, 30, 24, 50, 10, 83, 53, 34, 40, 16, 26, 76, 92,
        48, 31, 27, 49, 82, 44, 0, 35, 36, 60, 93, 71, 32, 5, 47, 41, 33, 28, 46, 68, 67,
        37, 95, 11, 45, 84, 63, 1, 99, 6, 13, 98, 54, 17, 79, 85, 90, 21, 81, 62, 8, 19,14,
        23, 29, 9, 74, 91, 39, 69, 38, 25, 70, 12, 22, 52, 89, 75, 77, 73, 59, 4, 57, 2, 72,
        58, 78, 86, 43, 42, 96, 65, 88, 51, 18, 97, 61, 64, 3]
#Test last index
print("\nTesting list w/ 100 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_modified_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 100 elements, Index: ", 0)
print("\t\tElement is: ", select_modified_quick(test, 0))
#Test middle index
print("\nTesting list w/ 100 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_modified_quick(test, (len(test) - 1)//2))
#Test list w/ 1000 elements
test = [ 761,    77,   665,   912,   735,   204,   232,   392,   457,   372, 
         169,    88,   599,   174,   487,   237,    39,   744,   406,   853,
         822,   650,   557,   170,   282,   620,   933,   514,    24,   532,
         281,   528,   880,   867,   595,   116,   136,   316,   710,   592,
         705,   998,   548,   707,   657,    27,   971,   790,   364,   297,
         563,   996,   764,   339,   641,   833,    44,   416,   508,   699,
         824,    64,   910,   308,   766,   486,   837,   943,   581,   763,
         262,   819,     2,   603,   239,     8,   129,   956,   186,   153,
         894,   538,   300,   846,   555,   358,   751,   816,   934,   544,
         724,   385,   271,   131,   353,   443,   938,   515,   451,   461,
         923,   311,   327,    94,   810,   211,   951,   433,   773,   340,
         417,   103,   166,   124,   654,   738,     3,   963,   458,   243,
         524,   474,    15,   804,   906,   442,   448,   957,   125,    43,
           9,   143,   628,   101,   468,   931,   789,   471,   962,   993,
         579,    26,   179,   578,   550,   689,   842,   574,   924,   877,
         848,   902,   704,   736,   376,   613,   369,   497,   975,   731,
         640,    80,   445,    46,   897,   834,   940,   401,   276,   412,
         283,   676,   172,   410,   695,   747,   739,   292,    58,   690,
         407,   110,   226,   331,   507,   512,   720,   757,   767,   825,
         355,   227,    10,   682,   980,   245,   498,   119,   632,   748,
         462,   255,   892,   301,   839,   138,   195,   240,   205,    53,
         114,   534,   829,   793,   459,   950,    98,   911,   264,    35,
         396,   554,   732,   249,   854,   694,   981,   164,    40,   875,
         881,   874,   955,   493,   404,   684,   772,   370,   248,    41,
         435,   759,   350,   835,   251,   500,   831,   286,   585,   201,
         161,   228,   740,   444,   658,   999,   769,   155,   711,   779,
         122,   415,   347,   527,   634,   898,   631,   545,   509,   291,
         193,   158,   389,   202,   304,   796,   882,   984,   216,   241,
         197,   623,   290,    34,   564,   115,   336,   974,    66,   489,
         754,   818,   441,   151,   787,   348,   883,    70,   345,   258,
         495,   231,   917,   360,   257,   536,   821,   750,   333,   289,
         171,    71,   485,   652,   323,   130,   797,   148,   588,   591,
         296,   386,   838,   338,   760,    22,   382,   855,   113,   572,
         850,    13,   567,   602,   379,   187,   212,   942,   845,    85,
         653,   728,   480,   925,   106,   961,   484,   896,    76,   828,
         893,   380,   436,   428,   782,   876,    95,   521,   413,   244,
         446,   671,   225,   247,   375,   402,   213,   150,   185,    29,
         268,   768,   270,   464,    37,   719,   843,   181,   667,   721,
         651,   215,   518,   180,   233,   614,   982,   176,   108,   807,
         997,   809,    47,   778,   619,   647,    67,   196,   117,   781,
         642,   183,   306,   708,   920,   277,   915,   496,   625,   713,
         985,   329,   165,   189,   414,   102,   558,   817,   659,   363,
         167,   491,   664,   646,    49,    12,   879,   856,    75,   274,
         173,   678,   944,    62,   844,   774,   419,   287,   672,   571,
         847,   299,    45,   899,    79,   542,   907,   742,   279,   252,
         863,   470,   969,   629,   655,   337,    23,   683,   222,   639,
         594,   887,   702,   666,   393,   149,    56,   775,   447,   147,
         288,   466,   878,   872,   703,   752,   284,   823,   156,   328,
         930,   992,   870,   673,   107,   517,    68,   315,   648,   709,
         743,   321,   792,   987,   675,   965,   325,   706,   530,   427,
         134,    83,    33,   686,   582,   903,  1000,   391,   697,   377,
         715,    31,    42,   604,   668,   373,   936,   723,   452,   952,
         207,     5,   589,   109,    84,    11,   139,   756,   700,   309,
         937,   749,   200,   783,   543,   994,   901,   206,   669,   140,
         294,   945,   182,   688,   168,   857,   976,   627,   141,   492,
         593,   577,   904,   312,   785,   400,   298,   511,   596,   522,
         234,   356,   909,   820,   873,   539,   209,   836,   939,   886,
         469,   849,   472,   959,   272,   569,   429,   800,   192,   948,
         367,   278,   583,   157,   431,   194,   601,   729,   794,   421,
         805,   871,   718,   786,   388,   953,   408,   622,   972,   858,
         784,    92,   440,   630,   502,   242,    69,   926,   454,   467,
         803,   701,   230,   302,   888,   905,   770,   615,    63,   889,
          93,   954,   529,   662,   977,   973,   541,   922,   811,   293,
         798,   253,   727,   403,   860,   776,   989,   335,   351,   758,
         832,    59,   162,   941,   269,   815,    89,    96,   568,   295,
         152,   482,   319,    17,   891,    19,   565,   163,   737,   535,
         420,   354,    82,   691,   146,   626,   198,   612,   679,   361,
         142,   730,   343,   449,   960,   132,   390,     7,   733,   256,
         562,   575,   516,   916,   546,   145,   621,    30,   580,   318,
         199,   605,   259,   970,   734,    55,   597,   128,   357,   520,
         313,   175,   504,   801,   552,   127,   395,   477,   610,   547,
         456,    48,   394,   929,   722,   598,   303,    14,   488,   908,
         238,   214,   978,   884,   827,    57,   123,   624,   865,   741,
         223,   506,   526,   914,   481,    60,    38,   366,   795,    21,
         932,   463,    78,    65,   553,   814,   365,   725,   104,   334,
         533,   317,   799,   280,   144,   714,    91,   120,   220,   967,
         864,   812,   966,   349,   556,   266,   422,   566,   342,   777,
         424,   362,   928,   432,   895,   649,   217,   949,   235,   483,
         990,   322,   159,   411,    74,    52,   802,   830,   381,   531,
          16,   154,   551,    72,    86,   869,   921,   927,   762,   946,
         218,   112,   320,    51,     6,   344,   285,   371,    50,   273,
         137,    81,   712,   341,   191,   885,   221,     4,   765,   935,
         638,   918,   913,    54,   160,   637,   606,   438,   586,   983,
         746,   409,    87,   378,   986,   852,   616,   726,   560,   771,
         851,   229,   246,   717,   118,   236,   780,   890,   958,   455,
         184,   178,    36,   525,   523,   561,   418,   479,   919,   250,
         587,   510,   968,   608,   453,   687,   437,   224,    32,   135,
          90,   549,     1,    97,   105,   590,    18,   397,   423,   991,
         434,   617,   540,   806,   584,   426,    61,   635,   210,   813,
         490,   260,   670,   439,   861,   501,    20,   600,   460,   121,
         753,   126,   368,   346,   868,   203,   359,   473,   398,   900,
         656,   383,   573,   324,   100,    73,   387,   696,   862,   826,
         788,   840,   494,   576,   677,   964,   133,   188,   607,   305,
         681,   505,   450,   476,   609,   111,   674,   519,   208,   808,
         465,   499,   384,   643,   636,   633,   698,   663,   645,   995,
         660,   693,    99,   618,   503,   265,   190,   611,   399,   352,
         979,   310,   513,   559,   267,   644,   478,   685,   219,   475,
         307,   661,   263,   261,   692,   866,   755,   275,    28,   947,
         332,   405,   841,   745,   430,   791,    25,   425,   314,   537,
         570,   988,   254,   374,   177,   859,   716,   326,   680,   330]
#Test last index
print("\nTesting list w/ 1000 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_modified_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 1000 elements, Index: ", 0)
print("\t\tElement is: ", select_modified_quick(test, 0))
#Test middle index
print("\nTesting list w/ 1000 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_modified_quick(test, (len(test) - 1)//2))

#Stack Quicksort
print("Stack Quicksort: ")
#Test empty list
test = []
print("\nTesting empty list, Index: ", 0)
print("\t\tElement is: ", select_stack_quick(test, 0))
#Test list w/ 10 elements
test = [1, 6, 2, 10, 3, 9, 7, 4, 8, 5]
#Test invalid index
print("\nTesting list w/ 10 elements, Index: ", -1)
print("\t\tElement is: ", select_stack_quick(test, -1))
#Test last index
print("\nTesting list w/ 10 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_stack_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 10 elements, Index: ", 0)
print("\t\tElement is: ", select_stack_quick(test, 0))
#Test middle index
print("\nTesting list w/ 10 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_stack_quick(test, (len(test) - 1)//2))
#Test list w/ 100 elements
test = [66, 56, 7, 80, 87, 55, 15, 94, 20, 30, 24, 50, 10, 83, 53, 34, 40, 16, 26, 76, 92,
        48, 31, 27, 49, 82, 44, 0, 35, 36, 60, 93, 71, 32, 5, 47, 41, 33, 28, 46, 68, 67,
        37, 95, 11, 45, 84, 63, 1, 99, 6, 13, 98, 54, 17, 79, 85, 90, 21, 81, 62, 8, 19,14,
        23, 29, 9, 74, 91, 39, 69, 38, 25, 70, 12, 22, 52, 89, 75, 77, 73, 59, 4, 57, 2, 72,
        58, 78, 86, 43, 42, 96, 65, 88, 51, 18, 97, 61, 64, 3]
#Test last index
print("\nTesting list w/ 100 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_stack_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 100 elements, Index: ", 0)
print("\t\tElement is: ", select_stack_quick(test, 0))
#Test middle index
print("\nTesting list w/ 100 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_stack_quick(test, (len(test) - 1)//2))
#Test list w/ 1000 elements
test = [ 761,    77,   665,   912,   735,   204,   232,   392,   457,   372, 
         169,    88,   599,   174,   487,   237,    39,   744,   406,   853,
         822,   650,   557,   170,   282,   620,   933,   514,    24,   532,
         281,   528,   880,   867,   595,   116,   136,   316,   710,   592,
         705,   998,   548,   707,   657,    27,   971,   790,   364,   297,
         563,   996,   764,   339,   641,   833,    44,   416,   508,   699,
         824,    64,   910,   308,   766,   486,   837,   943,   581,   763,
         262,   819,     2,   603,   239,     8,   129,   956,   186,   153,
         894,   538,   300,   846,   555,   358,   751,   816,   934,   544,
         724,   385,   271,   131,   353,   443,   938,   515,   451,   461,
         923,   311,   327,    94,   810,   211,   951,   433,   773,   340,
         417,   103,   166,   124,   654,   738,     3,   963,   458,   243,
         524,   474,    15,   804,   906,   442,   448,   957,   125,    43,
           9,   143,   628,   101,   468,   931,   789,   471,   962,   993,
         579,    26,   179,   578,   550,   689,   842,   574,   924,   877,
         848,   902,   704,   736,   376,   613,   369,   497,   975,   731,
         640,    80,   445,    46,   897,   834,   940,   401,   276,   412,
         283,   676,   172,   410,   695,   747,   739,   292,    58,   690,
         407,   110,   226,   331,   507,   512,   720,   757,   767,   825,
         355,   227,    10,   682,   980,   245,   498,   119,   632,   748,
         462,   255,   892,   301,   839,   138,   195,   240,   205,    53,
         114,   534,   829,   793,   459,   950,    98,   911,   264,    35,
         396,   554,   732,   249,   854,   694,   981,   164,    40,   875,
         881,   874,   955,   493,   404,   684,   772,   370,   248,    41,
         435,   759,   350,   835,   251,   500,   831,   286,   585,   201,
         161,   228,   740,   444,   658,   999,   769,   155,   711,   779,
         122,   415,   347,   527,   634,   898,   631,   545,   509,   291,
         193,   158,   389,   202,   304,   796,   882,   984,   216,   241,
         197,   623,   290,    34,   564,   115,   336,   974,    66,   489,
         754,   818,   441,   151,   787,   348,   883,    70,   345,   258,
         495,   231,   917,   360,   257,   536,   821,   750,   333,   289,
         171,    71,   485,   652,   323,   130,   797,   148,   588,   591,
         296,   386,   838,   338,   760,    22,   382,   855,   113,   572,
         850,    13,   567,   602,   379,   187,   212,   942,   845,    85,
         653,   728,   480,   925,   106,   961,   484,   896,    76,   828,
         893,   380,   436,   428,   782,   876,    95,   521,   413,   244,
         446,   671,   225,   247,   375,   402,   213,   150,   185,    29,
         268,   768,   270,   464,    37,   719,   843,   181,   667,   721,
         651,   215,   518,   180,   233,   614,   982,   176,   108,   807,
         997,   809,    47,   778,   619,   647,    67,   196,   117,   781,
         642,   183,   306,   708,   920,   277,   915,   496,   625,   713,
         985,   329,   165,   189,   414,   102,   558,   817,   659,   363,
         167,   491,   664,   646,    49,    12,   879,   856,    75,   274,
         173,   678,   944,    62,   844,   774,   419,   287,   672,   571,
         847,   299,    45,   899,    79,   542,   907,   742,   279,   252,
         863,   470,   969,   629,   655,   337,    23,   683,   222,   639,
         594,   887,   702,   666,   393,   149,    56,   775,   447,   147,
         288,   466,   878,   872,   703,   752,   284,   823,   156,   328,
         930,   992,   870,   673,   107,   517,    68,   315,   648,   709,
         743,   321,   792,   987,   675,   965,   325,   706,   530,   427,
         134,    83,    33,   686,   582,   903,  1000,   391,   697,   377,
         715,    31,    42,   604,   668,   373,   936,   723,   452,   952,
         207,     5,   589,   109,    84,    11,   139,   756,   700,   309,
         937,   749,   200,   783,   543,   994,   901,   206,   669,   140,
         294,   945,   182,   688,   168,   857,   976,   627,   141,   492,
         593,   577,   904,   312,   785,   400,   298,   511,   596,   522,
         234,   356,   909,   820,   873,   539,   209,   836,   939,   886,
         469,   849,   472,   959,   272,   569,   429,   800,   192,   948,
         367,   278,   583,   157,   431,   194,   601,   729,   794,   421,
         805,   871,   718,   786,   388,   953,   408,   622,   972,   858,
         784,    92,   440,   630,   502,   242,    69,   926,   454,   467,
         803,   701,   230,   302,   888,   905,   770,   615,    63,   889,
          93,   954,   529,   662,   977,   973,   541,   922,   811,   293,
         798,   253,   727,   403,   860,   776,   989,   335,   351,   758,
         832,    59,   162,   941,   269,   815,    89,    96,   568,   295,
         152,   482,   319,    17,   891,    19,   565,   163,   737,   535,
         420,   354,    82,   691,   146,   626,   198,   612,   679,   361,
         142,   730,   343,   449,   960,   132,   390,     7,   733,   256,
         562,   575,   516,   916,   546,   145,   621,    30,   580,   318,
         199,   605,   259,   970,   734,    55,   597,   128,   357,   520,
         313,   175,   504,   801,   552,   127,   395,   477,   610,   547,
         456,    48,   394,   929,   722,   598,   303,    14,   488,   908,
         238,   214,   978,   884,   827,    57,   123,   624,   865,   741,
         223,   506,   526,   914,   481,    60,    38,   366,   795,    21,
         932,   463,    78,    65,   553,   814,   365,   725,   104,   334,
         533,   317,   799,   280,   144,   714,    91,   120,   220,   967,
         864,   812,   966,   349,   556,   266,   422,   566,   342,   777,
         424,   362,   928,   432,   895,   649,   217,   949,   235,   483,
         990,   322,   159,   411,    74,    52,   802,   830,   381,   531,
          16,   154,   551,    72,    86,   869,   921,   927,   762,   946,
         218,   112,   320,    51,     6,   344,   285,   371,    50,   273,
         137,    81,   712,   341,   191,   885,   221,     4,   765,   935,
         638,   918,   913,    54,   160,   637,   606,   438,   586,   983,
         746,   409,    87,   378,   986,   852,   616,   726,   560,   771,
         851,   229,   246,   717,   118,   236,   780,   890,   958,   455,
         184,   178,    36,   525,   523,   561,   418,   479,   919,   250,
         587,   510,   968,   608,   453,   687,   437,   224,    32,   135,
          90,   549,     1,    97,   105,   590,    18,   397,   423,   991,
         434,   617,   540,   806,   584,   426,    61,   635,   210,   813,
         490,   260,   670,   439,   861,   501,    20,   600,   460,   121,
         753,   126,   368,   346,   868,   203,   359,   473,   398,   900,
         656,   383,   573,   324,   100,    73,   387,   696,   862,   826,
         788,   840,   494,   576,   677,   964,   133,   188,   607,   305,
         681,   505,   450,   476,   609,   111,   674,   519,   208,   808,
         465,   499,   384,   643,   636,   633,   698,   663,   645,   995,
         660,   693,    99,   618,   503,   265,   190,   611,   399,   352,
         979,   310,   513,   559,   267,   644,   478,   685,   219,   475,
         307,   661,   263,   261,   692,   866,   755,   275,    28,   947,
         332,   405,   841,   745,   430,   791,    25,   425,   314,   537,
         570,   988,   254,   374,   177,   859,   716,   326,   680,   330]
#Test last index
print("\nTesting list w/ 1000 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_stack_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 1000 elements, Index: ", 0)
print("\t\tElement is: ", select_stack_quick(test, 0))
#Test middle index
print("\nTesting list w/ 1000 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_stack_quick(test, (len(test) - 1)//2))

#While Modified Quicksort
print("While Modified Quicksort: ")
#Test empty list
test = []
print("\nTesting empty list, Index: ", 0)
print("\t\tElement is: ", select_while_modified_quick(test, 0))
#Test list w/ 10 elements
test = [1, 6, 2, 10, 3, 9, 7, 4, 8, 5]
#Test invalid index
print("\nTesting list w/ 10 elements, Index: ", -1)
print("\t\tElement is: ", select_while_modified_quick(test, -1))
#Test last index
print("\nTesting list w/ 10 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_while_modified_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 10 elements, Index: ", 0)
print("\t\tElement is: ", select_while_modified_quick(test, 0))
#Test middle index
print("\nTesting list w/ 10 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_while_modified_quick(test, (len(test) - 1)//2))
#Test list w/ 100 elements
test = [66, 56, 7, 80, 87, 55, 15, 94, 20, 30, 24, 50, 10, 83, 53, 34, 40, 16, 26, 76, 92,
        48, 31, 27, 49, 82, 44, 0, 35, 36, 60, 93, 71, 32, 5, 47, 41, 33, 28, 46, 68, 67,
        37, 95, 11, 45, 84, 63, 1, 99, 6, 13, 98, 54, 17, 79, 85, 90, 21, 81, 62, 8, 19,14,
        23, 29, 9, 74, 91, 39, 69, 38, 25, 70, 12, 22, 52, 89, 75, 77, 73, 59, 4, 57, 2, 72,
        58, 78, 86, 43, 42, 96, 65, 88, 51, 18, 97, 61, 64, 3]
#Test last index
print("\nTesting list w/ 100 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_while_modified_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 100 elements, Index: ", 0)
print("\t\tElement is: ", select_while_modified_quick(test, 0))
#Test middle index
print("\nTesting list w/ 100 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_while_modified_quick(test, (len(test) - 1)//2))
#Test list w/ 1000 elements
test = [ 761,    77,   665,   912,   735,   204,   232,   392,   457,   372, 
         169,    88,   599,   174,   487,   237,    39,   744,   406,   853,
         822,   650,   557,   170,   282,   620,   933,   514,    24,   532,
         281,   528,   880,   867,   595,   116,   136,   316,   710,   592,
         705,   998,   548,   707,   657,    27,   971,   790,   364,   297,
         563,   996,   764,   339,   641,   833,    44,   416,   508,   699,
         824,    64,   910,   308,   766,   486,   837,   943,   581,   763,
         262,   819,     2,   603,   239,     8,   129,   956,   186,   153,
         894,   538,   300,   846,   555,   358,   751,   816,   934,   544,
         724,   385,   271,   131,   353,   443,   938,   515,   451,   461,
         923,   311,   327,    94,   810,   211,   951,   433,   773,   340,
         417,   103,   166,   124,   654,   738,     3,   963,   458,   243,
         524,   474,    15,   804,   906,   442,   448,   957,   125,    43,
           9,   143,   628,   101,   468,   931,   789,   471,   962,   993,
         579,    26,   179,   578,   550,   689,   842,   574,   924,   877,
         848,   902,   704,   736,   376,   613,   369,   497,   975,   731,
         640,    80,   445,    46,   897,   834,   940,   401,   276,   412,
         283,   676,   172,   410,   695,   747,   739,   292,    58,   690,
         407,   110,   226,   331,   507,   512,   720,   757,   767,   825,
         355,   227,    10,   682,   980,   245,   498,   119,   632,   748,
         462,   255,   892,   301,   839,   138,   195,   240,   205,    53,
         114,   534,   829,   793,   459,   950,    98,   911,   264,    35,
         396,   554,   732,   249,   854,   694,   981,   164,    40,   875,
         881,   874,   955,   493,   404,   684,   772,   370,   248,    41,
         435,   759,   350,   835,   251,   500,   831,   286,   585,   201,
         161,   228,   740,   444,   658,   999,   769,   155,   711,   779,
         122,   415,   347,   527,   634,   898,   631,   545,   509,   291,
         193,   158,   389,   202,   304,   796,   882,   984,   216,   241,
         197,   623,   290,    34,   564,   115,   336,   974,    66,   489,
         754,   818,   441,   151,   787,   348,   883,    70,   345,   258,
         495,   231,   917,   360,   257,   536,   821,   750,   333,   289,
         171,    71,   485,   652,   323,   130,   797,   148,   588,   591,
         296,   386,   838,   338,   760,    22,   382,   855,   113,   572,
         850,    13,   567,   602,   379,   187,   212,   942,   845,    85,
         653,   728,   480,   925,   106,   961,   484,   896,    76,   828,
         893,   380,   436,   428,   782,   876,    95,   521,   413,   244,
         446,   671,   225,   247,   375,   402,   213,   150,   185,    29,
         268,   768,   270,   464,    37,   719,   843,   181,   667,   721,
         651,   215,   518,   180,   233,   614,   982,   176,   108,   807,
         997,   809,    47,   778,   619,   647,    67,   196,   117,   781,
         642,   183,   306,   708,   920,   277,   915,   496,   625,   713,
         985,   329,   165,   189,   414,   102,   558,   817,   659,   363,
         167,   491,   664,   646,    49,    12,   879,   856,    75,   274,
         173,   678,   944,    62,   844,   774,   419,   287,   672,   571,
         847,   299,    45,   899,    79,   542,   907,   742,   279,   252,
         863,   470,   969,   629,   655,   337,    23,   683,   222,   639,
         594,   887,   702,   666,   393,   149,    56,   775,   447,   147,
         288,   466,   878,   872,   703,   752,   284,   823,   156,   328,
         930,   992,   870,   673,   107,   517,    68,   315,   648,   709,
         743,   321,   792,   987,   675,   965,   325,   706,   530,   427,
         134,    83,    33,   686,   582,   903,  1000,   391,   697,   377,
         715,    31,    42,   604,   668,   373,   936,   723,   452,   952,
         207,     5,   589,   109,    84,    11,   139,   756,   700,   309,
         937,   749,   200,   783,   543,   994,   901,   206,   669,   140,
         294,   945,   182,   688,   168,   857,   976,   627,   141,   492,
         593,   577,   904,   312,   785,   400,   298,   511,   596,   522,
         234,   356,   909,   820,   873,   539,   209,   836,   939,   886,
         469,   849,   472,   959,   272,   569,   429,   800,   192,   948,
         367,   278,   583,   157,   431,   194,   601,   729,   794,   421,
         805,   871,   718,   786,   388,   953,   408,   622,   972,   858,
         784,    92,   440,   630,   502,   242,    69,   926,   454,   467,
         803,   701,   230,   302,   888,   905,   770,   615,    63,   889,
          93,   954,   529,   662,   977,   973,   541,   922,   811,   293,
         798,   253,   727,   403,   860,   776,   989,   335,   351,   758,
         832,    59,   162,   941,   269,   815,    89,    96,   568,   295,
         152,   482,   319,    17,   891,    19,   565,   163,   737,   535,
         420,   354,    82,   691,   146,   626,   198,   612,   679,   361,
         142,   730,   343,   449,   960,   132,   390,     7,   733,   256,
         562,   575,   516,   916,   546,   145,   621,    30,   580,   318,
         199,   605,   259,   970,   734,    55,   597,   128,   357,   520,
         313,   175,   504,   801,   552,   127,   395,   477,   610,   547,
         456,    48,   394,   929,   722,   598,   303,    14,   488,   908,
         238,   214,   978,   884,   827,    57,   123,   624,   865,   741,
         223,   506,   526,   914,   481,    60,    38,   366,   795,    21,
         932,   463,    78,    65,   553,   814,   365,   725,   104,   334,
         533,   317,   799,   280,   144,   714,    91,   120,   220,   967,
         864,   812,   966,   349,   556,   266,   422,   566,   342,   777,
         424,   362,   928,   432,   895,   649,   217,   949,   235,   483,
         990,   322,   159,   411,    74,    52,   802,   830,   381,   531,
          16,   154,   551,    72,    86,   869,   921,   927,   762,   946,
         218,   112,   320,    51,     6,   344,   285,   371,    50,   273,
         137,    81,   712,   341,   191,   885,   221,     4,   765,   935,
         638,   918,   913,    54,   160,   637,   606,   438,   586,   983,
         746,   409,    87,   378,   986,   852,   616,   726,   560,   771,
         851,   229,   246,   717,   118,   236,   780,   890,   958,   455,
         184,   178,    36,   525,   523,   561,   418,   479,   919,   250,
         587,   510,   968,   608,   453,   687,   437,   224,    32,   135,
          90,   549,     1,    97,   105,   590,    18,   397,   423,   991,
         434,   617,   540,   806,   584,   426,    61,   635,   210,   813,
         490,   260,   670,   439,   861,   501,    20,   600,   460,   121,
         753,   126,   368,   346,   868,   203,   359,   473,   398,   900,
         656,   383,   573,   324,   100,    73,   387,   696,   862,   826,
         788,   840,   494,   576,   677,   964,   133,   188,   607,   305,
         681,   505,   450,   476,   609,   111,   674,   519,   208,   808,
         465,   499,   384,   643,   636,   633,   698,   663,   645,   995,
         660,   693,    99,   618,   503,   265,   190,   611,   399,   352,
         979,   310,   513,   559,   267,   644,   478,   685,   219,   475,
         307,   661,   263,   261,   692,   866,   755,   275,    28,   947,
         332,   405,   841,   745,   430,   791,    25,   425,   314,   537,
         570,   988,   254,   374,   177,   859,   716,   326,   680,   330]
#Test last index
print("\nTesting list w/ 1000 elements, Index: ", len(test) - 1)
print("\t\tElement is: ", select_while_modified_quick(test, len(test) - 1))
#Test first index
print("\nTesting list w/ 1000 elements, Index: ", 0)
print("\t\tElement is: ", select_while_modified_quick(test, 0))
#Test middle index
print("\nTesting list w/ 1000 elements, Index: ", (len(test) - 1)//2)
print("\t\tElement is: ", select_while_modified_quick(test, (len(test) - 1)//2))
