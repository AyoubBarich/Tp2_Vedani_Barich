
import ArrayFunc 


def main(Array:list):
    print(Array)
    lenght = len(Array)
    for i in range(lenght):
        min = ArrayFunc.getMin(Array,i)
        if (Array[i]<Array[min]):
            Array = ArrayFunc.iterate(Array,min,i)
    return Array



print(main(ArrayFunc.GenerateRandomArray(5,-10,10)))
        


    
    