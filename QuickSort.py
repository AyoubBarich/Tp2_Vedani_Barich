import ArrayFunc

def Partition(Array,firstIndex,lastIndex):
    #we chose a random pivot 
    pivot = ArrayFunc.GetRandomIndex(firstIndex,lastIndex)
    #we define our pointer
    index = firstIndex-1
    #we put our pivot as the last element
    Array = ArrayFunc.iterate(Array,lastIndex,pivot)
    #we go through all elements and compare them with our pivot 
    for i in range(firstIndex,lastIndex):
        if Array[i]<=Array[lastIndex]:
            index+=1
            #if smaller than pivot we swap 
            Array = ArrayFunc.iterate(Array,index,i)
    #swap the pivot and the last element of our partition
    Array = ArrayFunc.iterate(Array,lastIndex,index+1)
    return index+1

def quickSort(Array,firstIndex, lastIndex):
    
    if firstIndex<lastIndex:
        #find our random pivot
        pivot = Partition(Array,firstIndex,lastIndex)
        #we call our recurscive function on both sides of our array seperated by our pivot
        quickSort(Array,firstIndex,pivot-1)
        quickSort(Array,pivot+1,lastIndex)
    
def main(Array):
    return quickSort(Array,0,len(Array)-1)


