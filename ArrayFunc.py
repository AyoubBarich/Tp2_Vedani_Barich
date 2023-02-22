
from random import randint
Array=[]

#Generate a random array with a given size , a lower bound and an upper bound for the elements of the array
def GenerateRandomArray(size,lowerBound,upperBound):  
    Array=[randint(lowerBound,upperBound) for i in range(size)]
    return Array
#returns a sub array of a given array ,the first index and the last index 
def GetSubArray(Array:list,firstIndex,lastIndex): 
    if (firstIndex==lastIndex):
        return Array[firstIndex]
    sub=[Array[i] for i in range(firstIndex,lastIndex+1)]
    return sub
#returns the sum of all the elements in the given array
def Somme(Array):
    Sum=0
    if isinstance(Array,list):
        for i in Array:
            Sum+=i
        return Sum
    return Array

def iterate(Array:list,firstIndex,secondIndex):
    tmp=Array[firstIndex]
    Array[firstIndex]=Array[secondIndex]
    Array[secondIndex]=tmp
    return Array
    

def getMin(Array:list,firstIndex):
    min=firstIndex
    for i in range(firstIndex+1,len(Array)):
        
        if Array[min] < Array[i]:
            min=i
    return min

def GetRandomIndex(firstIndex,lastIndex):
    return randint(firstIndex,lastIndex)
