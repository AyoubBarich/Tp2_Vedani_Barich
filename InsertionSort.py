import ArrayFunc

def main(Array) :
    #we go through all ellements of the given array
    for k in range (1,len(Array)):
        key = Array[k]
        i = k-1
        #if the value of our element key is lesser than the Arraty[i] we moe it one posuion ahead of our current position
        while i>=0 and Array[i]>key :

            Array[i+1] = Array[i]
            i = i-1
            Array[i+1] = key
    return(Array)
    
print(ArrayFunc.GenerateRandomArray(5,-10,10))