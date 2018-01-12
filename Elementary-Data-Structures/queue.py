class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None
        
class queue :
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else :
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
