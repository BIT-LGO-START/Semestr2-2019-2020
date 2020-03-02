class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, first = None, last = None):
        self.first = first
        self.last = last
    
    def isEmpty(self):
        return self.first is None

    def makeFromArray(self, array):
        if len(array) == 0:
            return
        self.first = Node(array[0])
        p = self.first
        self.last = p
        for i in range(1, len(array)):
            q = Node(array[i])
            p.next = q
            p = q
            self.last = p
    
    def printToConsole(self):
        p = self.first
        while p is not None:
            print(p.val)
            p = p.next
    
    def hasOneElement(self):
        return self.first == self.last
    
def MergeSortedLists(List1, List2):
    if List1.isEmpty():
        return List2
    result = LinkedList()
    p = Node()
    q = Node()
    r = Node()
    if List1.first.val <= List2.first.val:
        result.first = List1.first
        r = result.first
        result.last = r
        p = List1.first.next
        q = List2.first

    else:
        result.first = List2.first
        r = result.first
        result.last = r
        p = List2.first.next
        q = List1.first
    while p is not None and q is not None:
        while p is not None and q is not None and p.val <= q.val:
            r.next = p
            r = r.next
            result.last = r
            p = p.next
        while q is not None and p is not None and q.val<=p.val:
            r.next = q
            r = r.next
            result.last = r
            q = q.next
    while p is not None:
        r.next = p
        r = r.next
        result.last = r
        p = p.next
    while q is not None:
        r.next = q
        r = r.next
        result.last = r
        q = q.next
    return result
def SplitListIntoHalves(List):
    len = 0
    p = List.first
    while p is not None:
        len+=1
        p=p.next
    newBegin = List.first
    newEnd = List.first
    for i in range(0, len//2):
        newEnd = newBegin
        newBegin = newBegin.next
    newBegin = newEnd.next
    newEnd.next = None
    return (LinkedList(List.first, newEnd), LinkedList(newBegin,List.last))
def MergeSortOnLinkedList(List):
    if List.isEmpty() or List.hasOneElement():
        return List
    firstHalf, secondHalf = SplitListIntoHalves(List)
    firstHalfSorted = MergeSortOnLinkedList(firstHalf)
    secondHalfSorted = MergeSortOnLinkedList(secondHalf)
    return MergeSortedLists(firstHalfSorted, secondHalfSorted)
def main():
   L = LinkedList()
   L.makeFromArray([11,58,900,33,24,56,78,90,55,76,3546435,666,777,909,9])
   L = MergeSortOnLinkedList(L)
   L.printToConsole()
main()

