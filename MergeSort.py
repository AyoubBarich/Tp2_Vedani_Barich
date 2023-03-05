import ArrayFunc

def main(Array):
    if len(Array)>1:
        midPoint = len(Array)//2
        #we divide our array along the mid point
        rightArray = Array[midPoint:]
        leftArray = Array[:midPoint]
        #we sort the fist half
        main(rightArray)
        #we sort the seconf half
        main(leftArray)

        i=0
        j=0
        k=0
        #we compare the values in our givne array and we put them in the correct half 
        while i <len(leftArray) and j <len(rightArray):
            if leftArray[i]<=rightArray[j]:
                Array[k] = leftArray[i]
                i+=1
            else:
                Array[k] = rightArray[j]
                j+=1
            k+=1
        #we check if passed through all values in our array 
        while i < len(leftArray):
            Array[k]= leftArray[i]
            i+=1
            k+=1
        while j<len(rightArray):
            Array[k]=rightArray[j]
            j+=1
            k+=1
            