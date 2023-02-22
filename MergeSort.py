import ArrayFunc

def mergeSort(Array):
    if len(Array)>1:
        midPoint = len(Array)//2

        rightArray = Array[midPoint:]
        leftArray = Array[:midPoint]

        mergeSort(rightArray)
        mergeSort(leftArray)

        i=0
        j=0
        k=0

        while i <len(leftArray) and j <len(rightArray):
            if leftArray[i]<=rightArray[j]:
                Array[k] = leftArray[i]
                i+=1
            else:
                Array[k] = rightArray[j]
                j+=1
            k+=1

        while i < len(leftArray):
            Array[k]= leftArray[i]
            i+=1
            k+=1
        while j<len(rightArray):
            Array[k]=rightArray[j]
            j+=1
            k+=1
            