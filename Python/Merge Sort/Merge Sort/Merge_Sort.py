"""
Author: Alexandre Lepage
Date: May 2019
"""
import random
import time

ALGORITHM_NAME = "Merge Sort" # The name of the algorithm used for sorting
random.seed(2019) # Random Seed number to keep values constant.
LIST_SIZE = 25000 # Set the size of the list to 25,000.

def main():
    myList = [0] * LIST_SIZE # A list to be sorted.
    PopulateList(myList) # Fill the list with random numbers.
    
    #PrintList(myList) # Display list before sorting.

    ticks = time.time() # Get the time before sorting.
    MergeSort(myList) # Sort the list
    ticks = time.time() - ticks # Get the time difference after sorting.

    #PrintList(myList) # Display list after sorting.

    print("Sorting an array of type", type(myList), "of", LIST_SIZE, "elements.") # Print the type of the list and the amount of element in it.
    print("Algorithm: ", ALGORITHM_NAME) # Print the name of the algorithm used.
    print("Total Seconds : ", ticks) # Print the time spent in seconds.

def MergeSort(A:list, p:int=None, r:int=None):
    """
    Sort the list using merge sort algorithm
    -----PSEUDO CODE-----
    (A is an Array with index 0..n)
    (p and r are indexes) 
    MergeSort(A,p,r)
     if p < r
         q =  FLOOR[(p + r) / 2]
         MergeSort(A,p,q)
         MergeSort(A,q+1,r)
         Merge(A,p,q,r)
    -----PSEUDO CODE-----

    Keyword arguments:
    A:list: list to be sorted
    p:int: start index of list
    r:int: end index of list
    """
    if p is None or r is None:
        MergeSort(A, 0, len(A) - 1)
        return
    if p < r:
        q = int((p + r) / 2)
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)

def Merge(A:list, p:int, q:int, r:int):
    """
    Merge the 2 array portions together.
    -----PSEUDO CODE-----
    (A is an Array with index 0..n)
    (p, q and r are indexes)
    Merge(A,p,q,r)
     n1 = q - p + 1
     n2 = r - q
     let L[0..n1+1] and R[0..n2+1] be new arrays
     for i = 0 to n1 - 1
         L[i] = A[p + i]
     for j = 0 to n2 - 1
         R[j] = A[q + j + 1]
     L[n1] = INFINITY
     R[n2] = INFINITY
     x = 0
     y = 0
     for k = p to r
         if L[x] <= R[y]
             A[k] = L[x]
             x = x + 1
         else
             A[k] = R[y]D
             y = y + 1
    -----PSEUDO CODE-----

    Keyword arguments:
    A:list: list to be sorted
    p:int: start index of first portion of the list
    q:int: end index of first portion of the list
    r:int: end index of second portion of the list
    """
    
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L[n1] = float("infinity")
    R[n2] = float("infinity")
    x = 0
    y = 0
    for k in range(p, r):
        if L[x] <= R[y]:
            A[k] = L[x]
            x += 1
        else:
            A[k] = R[y]
            y += 1
    
def PopulateList(A:list):
    """
    Populate a list with random numbers between -100,000 to 100,000
    
    Keyword arguments:
    A:list: the list to populate
    """
    for i in range(0, len(A)):
        A[i] = random.randint(-100000,100000)

def PrintList(A:list):
    """ 
    Print the list's elements

    Keyword arguments:
    A:list: the list to populate
    """
    print("---- List ----")
    print(A)
    print("---- ----")

"""Entry point"""
if __name__ == "__main__":
    main()