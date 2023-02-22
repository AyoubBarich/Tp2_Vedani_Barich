
from random import randint
import time
import matplotlib.pyplot as plt
import math
import HeapSort,InsertionSort,MergeSort,QuickSort,SelectionSort,ArrayFunc





###########################################TEST###########################################


#First test : we test the if the results of each function is compatible with the others

def TestCompatibility(testArray):

    heapSort = HeapSort.main(testArray)
    insertionSort = InsertionSort.main(testArray)
    mergeSort = MergeSort.main(testArray)
    quickSort = QuickSort.main(testArray)
    #selectionSort = SelectionSort.selectionSort(testArray)

    if heapSort==insertionSort and mergeSort== quickSort and insertionSort == mergeSort:
        return True
def Tester(size,numberOftests):
    for i in range (numberOftests):
        print(TestCompatibility(ArrayFunc.GenerateRandomArray(size,-10,10)))
    



#Second test : we plot the execution time of each function with a given array size

CONST=1000

def plotter(methode,sizeMax,step,color):
    
    Xcoord=[]
    Ycoord=[]
    for i in range(5,sizeMax,step):
        start = time.time()
        methode.main(ArrayFunc.GenerateRandomArray(i,-10,10))
        execTime = time.time()-start

        Xcoord.append(i)
        Ycoord.append(execTime*CONST)


    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps")
    return plt.plot(Xcoord,Ycoord,color)

def complexityPlot(Method,Complexity,sizeMax,step):
    Xcoord=[]
    Ycoord=[]
    YcoordOfComplexity=[]
    for i in range(5,sizeMax,step):
        start = time.time()
        Method.main(ArrayFunc.GenerateRandomArray(i,-10,10))
        execTime = time.time()-start
        Xcoord.append(i)
        Ycoord.append(execTime*CONST)
        YcoordOfComplexity.append(Complexity(i)/CONST)

    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps")
    return (plt.plot(Xcoord,YcoordOfComplexity,"b"),plt.plot(Xcoord,Ycoord,"r"))

# def Cube(x):
#     return x*x*x

def Square(x):
    return x*x

def NLog(x):
    return x*math.log2(x)
###########################################GRAPH###########################################



###########################################All Functions###########################################
size=2000
plotter(SelectionSort,size,5,'r')
plotter(InsertionSort,size,5,'g')
plotter(QuickSort,size,5,'b')
plotter(HeapSort,size,5,'y')
plotter(MergeSort,size,5,'c')
plt.show()
###########################################Selection Sort###########################################

# complexityPlot(SelectionSort,Square,size,50)
# plt.show()

###########################################Insertion Sort###########################################

# complexityPlot(InsertionSort,Square,size,50)
# plt.show()

###########################################Quick Sort###########################################

# complexityPlot(QuickSort,NLog,size,50)
# plt.show()

###########################################Heap Sort###########################################


# complexityPlot(HeapSort,NLog,size,50)
# plt.show()

###########################################merge Sort###########################################

# complexityPlot(MergeSort,NLog,size,5)
# plt.show()
