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
    
    def add(self, val):
        node = Node(val)
        if self.isEmpty():
            self.first = node
            self.last = node
            return
        self.last.next = node
        self.last = node

def ConcatenateLinkedLists(arrayOfLinkedLists):
    result = LinkedList()
    foundBegining = False
    for i in arrayOfLinkedLists:
        if not i.isEmpty():
            i.last.next  = None
    for i in arrayOfLinkedLists:
        if not foundBegining and not i.isEmpty():
            foundBegining = True
            result.first = i.first
            result.last = i.last
        elif not i.isEmpty():
            result.last.next = i.first
            result.last = i.last
    return result

def QuickSortOnLinkedList(List):
    if List.isEmpty() or List.hasOneElement():
        return List
    smaller = LinkedList()
    equal = LinkedList()
    greater = LinkedList()
    p = List.first
    while p is not None:
        if p.val<List.last.val:
            smaller.add(p.val)
        elif p.val == List.last.val:
            equal.add(p.val)
        else:
            greater.add(p.val)
        p=p.next
    return ConcatenateLinkedLists([QuickSortOnLinkedList(smaller), equal, QuickSortOnLinkedList(greater)])
def main():
    L = LinkedList()
    L.makeFromArray([124513,64356,24567567,544342456,876767,1342462467,6545451,245635678789,0])
    L = QuickSortOnLinkedList(L)
    L.printToConsole()
main()




