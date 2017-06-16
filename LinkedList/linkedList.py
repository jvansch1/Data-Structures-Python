from node import Node

class LinkedList:

    def __init__(self):
        self.head = None;

    def addNode(self, value):
        newNode = Node(value, None)

        if (self.head == None):
            self.head = newNode
            return

        currentNode = self.head

        while currentNode.next_node != None:
            currentNode = currentNode.next_node

        currentNode.next_node = newNode


    def printList(self):
        if self.head == None:
            return "List is empty"

        currentNode = self.head

        while currentNode != None:
            print currentNode.value
            currentNode = currentNode.next_node

node = Node(1)
LinkedList = LinkedList()
LinkedList.addNode(1)
LinkedList.addNode(2)
LinkedList.addNode(3)
LinkedList.printList()
