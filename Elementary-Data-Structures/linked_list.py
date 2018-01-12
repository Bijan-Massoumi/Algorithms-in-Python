

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.prev = self.head
            self.head.next = new_node
            self.head = new_node

    def pop_front(self):
        if self.head.prev != None:
            self.head = self.head.prev
            self.head.next = None

    def push_back (self,data):
        new_node = Node(data)
        new_node.next = self.tail
        self.tail.prev = new_node
        self.tail = new_node

    def print_list(self):
        def _print_list(node,acc):
            if node != None:
                acc.append(node.data)
                return _print_list(node.next,acc)
            return acc

        print(_print_list(self.tail,[]))


love = List()
love.push_front(7)
love.push_front(8)
love.push_front(9)
love.push_back(10)
love.push_back(8)
love.print_list()

