import ArrayFunc

def EntasserMax(Array,lenght,index):
    
    root=index
    
    leftChild=(2*index)+1 
    rightChild=(2*index) +2

    if leftChild < lenght and Array[root]<Array[leftChild]:
        root = leftChild
    
    if rightChild < lenght and Array[root]<Array[rightChild]:
        root = rightChild
    
    if root != index:
        Array = ArrayFunc.iterate(Array,root,index)
        #Array[index], Array[root] = Array[root], Array[index]
        EntasserMax(Array,lenght,root)
    
    
def main (Array):
    
    lenght = len(Array)
    for i in range((lenght//2),-1,-1):
        EntasserMax(Array,lenght,i)
    
    for i in range(lenght-1,0,-1):
        Array = ArrayFunc.iterate(Array,i,0)
        #Array[i], Array[0]= Array[0], Array[i]
        EntasserMax(Array,i,0)
    


