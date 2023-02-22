import ArrayFunc

def Partition(Array,firstIndex,lastIndex):

    pivot = ArrayFunc.GetRandomIndex(firstIndex,lastIndex)
    index = firstIndex-1
    Array = ArrayFunc.iterate(Array,lastIndex,pivot)
    for i in range(firstIndex,lastIndex):
        if Array[i]<=Array[lastIndex]:
            index+=1
            Array = ArrayFunc.iterate(Array,index,i)
    Array = ArrayFunc.iterate(Array,lastIndex,index+1)
    return index+1

def quickSort(Array,firstIndex, lastIndex):
    print("Unsorted Array : ",Array)
    if firstIndex<lastIndex:
        pivot = Partition(Array,firstIndex,lastIndex)
        quickSort(Array,firstIndex,pivot-1)
        quickSort(Array,pivot+1,lastIndex)
    print("Sorted Array :",Array)

quickSort(ArrayFunc.GenerateRandomArray(5,-10,10),0,4)

