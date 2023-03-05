import ArrayFunc

def EntasserMax(Array,lenght,index):
    
    root=index
    
    leftChild=(2*index)+1 
    rightChild=(2*index) +2
    #we check if our left child is greater than our root
    if leftChild < lenght and Array[root]<Array[leftChild]:
        root = leftChild
    #we check if our right child is greater than our root
    if rightChild < lenght and Array[root]<Array[rightChild]:
        root = rightChild
    #we change our root if needed than apply the same function to heapify the whole tree
    if root != index:
        Array = ArrayFunc.iterate(Array,root,index)
        EntasserMax(Array,lenght,root)
    
#the sorting function     
def main (Array):
    
    lenght = len(Array)
    #we gothrouh all elements of our tree and aplly the heapify function to get a max heap so we can extract the last element and affect it into our sorted arrsay
    for i in range((lenght//2),-1,-1):
        EntasserMax(Array,lenght,i)
    
    for i in range(lenght-1,0,-1):
        Array = ArrayFunc.iterate(Array,i,0)
        
        EntasserMax(Array,i,0)
    


