import ArrayFunc

def EntasserMax(Array:list,lenght,index):
    
    root=index
    
    leftChild=2*index +1 
    rightChild=2*index +2

    if leftChild < lenght and Array[leftChild]>Array[index]:
        root = leftChild
    
    if rightChild< lenght and Array[rightChild]> Array[index]:
        root = rightChild
    
    if root!= index:
        Array = ArrayFunc.iterate(Array,root,index)

        EntasserMax(Array,lenght,root)
    
def main (Array:list):
    print("unsorted array :",Array)
    lenght = len(Array)
    for i in range((lenght//2)-1,-1,-1):
        EntasserMax(Array,lenght,i)
    
    for i in range(lenght-1,0,-1):
        Array = ArrayFunc.iterate(Array,0,i)
        EntasserMax(Array,i,0)
    return Array


print(main(ArrayFunc.GenerateRandomArray(5,-10,10)))
            
