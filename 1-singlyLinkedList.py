# Singly-Linked List

class ListNode:
    def __init__(self, inputData):
        self.data = inputData
        self.child = None

    def data(self):
        return self.data

    def child(self):
        return self.child

    def update(self, inputData):
        self.data = inputData

    def setChild(self, inputchild):
        self.child = inputchild


class SinglyLinkedList:
    def __init__(self, inputNode=None):
        self.length = 0
        self.head = inputNode
        if (inputNode):
            self.length += 1

    def length(self):
        return self.length

    def head(self):
        return self.head

    def append(self, inputNode):
        if (self.head == None):
            self.head = inputNode
        else:
            currentNode = self.head

            for _ in range(self.length - 1):
                currentNode = currentNode.child

            currentNode.child = inputNode

        self.length += 1

    def insert(self, inputNode, pos):
        assert 0 <= pos <= self.length, "Out of Index"

        prevNode = None
        currentNode = self.head
        for _ in range(pos):
            prevNode = currentNode
            currentNode = currentNode.child

        # TODO: Insert

    def remove(self, pos):
        assert self.length != 0, "Empty List"
        assert 0 <= pos <= self.length - 1, "Out of Index"

        prevNode = None
        currentNode = self.head

        for _ in range(pos):
            prevNode = currentNode
            currentNode = currentNode.child

        # TODO: Update Nodes

        self.length -= 1

        return currentNode

    def pop(self):
        return self.remove(self.length - 1)

    def get(self, pos):
        currentNode = self.head

        for _ in range(pos):
            currentNode = currentNode.child

        return currentNode

    def __str__(self):
        tempArray = []
        currentNode = self.head
        for _ in range(self.length):
            tempArray.append(currentNode.data)
            currentNode = currentNode.child
        return str(tempArray)

    def fullPrint(self):
        tempArray = []
        currentNode = self.head
        for _ in range(self.length):
            tempArray.append([currentNode.data, currentNode.child.data])
            currentNode = currentNode.child
        print(str(tempArray))


if __name__ == "__main__":
    # Test empty list
    emptyList = SinglyLinkedList()
    assert (emptyList.length == 0)
    assert (emptyList.head == None)

    # Create first node
    testData = "first"
    firstNode = ListNode(testData)
    assert (firstNode.data == testData)
    assert (firstNode.child == None)

    # Create list with first node
    firstList = SinglyLinkedList(firstNode)
    assert (firstList.length == 1)
    assert (firstList.head == firstNode)

    # Insert into empty list
    emptyList.append(firstNode)
    assert (emptyList.length == 1)
    assert (emptyList.head == firstNode)

    # Pop from "emptyList"
    poppedNode = emptyList.pop()
    assert (emptyList.length == 0)
    assert (emptyList.head == None)
    assert (poppedNode == firstNode)

    # Larger list [0, 1, ..., n-1, n]
    n = 3

    largerList = SinglyLinkedList()
    for i in range(n):
        tempNode = ListNode(i)
        largerList.append(tempNode)
    assert (largerList.length == n)

    largerList.fullPrint()

    # Larger list tests
    # Content
    for i in range(n):
        assert (largerList.get(i).data == i)

    # Remove at index x
    x = 1
    removedNode = largerList.remove(x)
    assert (largerList.length == n - 1)
    assert (removedNode.data == x)

    largerList.fullPrint()

    # Insert x+1 at x
    newNode = ListNode(x+1)
    largerList.insert(newNode, x)
