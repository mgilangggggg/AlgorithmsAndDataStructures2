from turtle import right


class Node :
    def _init_(self, dataBaru) :
        self.left = None
        self.right = None
        self.data = dataBaru

    def tukarkan (self, first, second):
        bantu = first.data
        first.data = second.data
        second.data = bantu

    def maxHeap (self, root) :
        if (root is None) :
            return False
            self.maxHeap (root.left)
            self.maxHeap (root.right)
            if (root.left != None and root.left.data > root.data) :
                self.tukarkan(root, root.left)
                self.maxHeap(root)
        
        if (root.right != None and root.right.data > root.data) :


    # Pre-Order : Node -> Left -> Right 
    def PreOrderTraversal(self, root) :
        out = []
        if root :
            out.append(root.data)
            out = out + self.PreOrderTraversal(root.left)
            out = out + self.PreOrderTraversal(root.right)
        return out


    # In-Order : Left -> Node -> Right
    def InOrderTraversal(self, root) :
        out = []
        if root :
            out = out + self.InOrderTraversal(root.left)
            out.append(root.data)
            out = out + self.InOrderTraversal(root.right)
        return out


    # Post-Order : Left -> Right -> Node
    def PostOrderTraversal(self, root) :
        out = []
        if root :
            out = out + self.PostOrderTraversal(root.left)
            out.append(root.data)
            out = out + self.PostOrderTraversal(root.right)
        return out

def insertCBT(arr, i, n) :
    head = None

    if i < n :
        head = Node (arr[i])

        # Insert Left Child
        head.left = insertCBT(arr, 2 * i + 1, n)

        # Insert Right Child
        head.right = insertCBT(arr, 2 * i + 2, n)

    return head

# In-Order : Left -> Node -> Right
def InOrderTraversal(root) :
    out = []
    if root :
        out = out + InOrderTraversal(root.left)
        out.append(root.data)
        out = out + InOrderTraversal(root.right)
    return out

def tukarkan (first, second):
    bantu = first.data
    first.data = second.data
    second.data = bantu

def maxHeap (self, root) :
    if (root is None) :
        return False

        maxHeap (root.left)
        maxHeap (root.right)
        if (root.left != None and root.left.data > root.data) :
            self.tukarkan(root, root.left)
            self.maxHeap(root)
    
        if (root.right != None and root.right.data > root.data) :
            tukarkan(root, root.right)
            maxHeap(root)

def PertukaranHeap(Arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and Arr[left] > Arr[i] :
        largest = left
    else :
        largest = i


    if right < n and Arr[right] > Arr[largest] :
        largest = right

    # pertukaran
    if largest != i :
        Arr[i], Arr[largest] = Arr[largest], Arr[i]
        PertukaranHeap(Arr, n, largest)

def MaxHeapSort(Arr) :
    n = len(Arr)
    for i in range (n, -1, -1)
        PertukaranHeap(Arr, n, i)

    for i in range (n-1, 0, -1) :
        Arr[0],Arr[i] = Arr[i], Arr[0]

# memasukan Elemen Array
'''arr = []
n = int(input('Banyak Data : '))
for i in range (n) :
    print('Masukan Data Ke-',i+1 ':',end=' ')
    databaru = int(input(''))
    arr.append(databaru)'''

arr = [7,3,2,14,11,5]
n = len(arr)

head = insertCBT(arr, 0 , n)

print('--Tree Sebelum MaxHeap--')
print('In-Order Traversal')
print(InOrderTraversal(head))

maxHeap(head)
print('--Tree Sebelum MaxHeap--')
print('In-Order Traversal')
print(InOrderTraversal(head))

print()
print('--Max Heap Sort--')
MaxHeapSort(arr)
print(arr)