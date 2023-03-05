
import ArrayFunc 


def main(Array:list):
    
    lenght = len(Array)
    #we go through all elements of our array
    for i in range(lenght):
        min=i
        #find the minimum element
        for i in range(i,lenght):
            if Array[min] < Array[i]:
                min=i
        #swap the minimum element with our current position
        if (Array[i]<Array[min]):
            tmp = Array[min]
            Array[min],Array[i] = Array[i],tmp
    return Array

        


    
    