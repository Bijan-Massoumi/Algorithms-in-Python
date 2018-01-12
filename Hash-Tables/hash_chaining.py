import math

class ChainHash:

    def __init__(self,size):
        self.num_buckets = size
        self.num_elem = 0
        self.bucket_array = [None] * self.num_buckets

    def hash(self,key,m): #hashes strings and numeric types
        if type(key) is str:
            return divmod(len(key),m)[1]
        else:
            return divmod(key, m)[1]

    def insert(self, key, data):
        hash_val = self.hash(key, self.num_buckets)

        if self.bucket_array[hash_val] is None:
            self.bucket_array[hash_val] = BucketList()
            self.bucket_array[hash_val].push_front(data,key)
        elif self.bucket_array[hash_val].exists(lambda x: x.key == key):
            def reassign(node):
                if node.key == key:
                    node.data = data
            self.bucket_array[hash_val].apply(reassign)
        else:
            self.bucket_array[hash_val].push_front(data,key)

        self.num_elem += 1
        self.handle_load()

    def get(self, key):
        hash_val = self.hash(key,self.num_buckets)
        if self.bucket_array[hash_val] is not None:
            return self.bucket_array[hash_val].extract(lambda x: x.key == key )[0]

    def handle_load(self):
        if self.num_elem/float(self.num_buckets) >= .75:
            temp_table = ChainHash(math.floor(2 * self.num_elem))


            for bucket in self.bucket_array:
                if bucket is not None:
                    bucket.apply(lambda x: temp_table.insert(x.key, x.data))
            self = temp_table

class Node:
    def __init__(self,data,key):
        self.next = None
        self.prev = None
        self.data = data
        self.key = key


class BucketList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elem = 0

    def push_front(self,data,key):
        new_node = Node(data,key)

        if self.tail is None:
            self.tail = new_node
            self.head = self.tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.num_elem += 1
        return new_node

    def remove_node(self,node):
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

    def apply(self,func):
        def traverse(node):
            if node is not None:
                func(node)
                traverse(node.next)
        traverse(self.head)

    def extract(self,func): # pass a method that returns a boolean
        def traverse(node, accu):
            if node is None:
                return accu
            elif func(node):
                accu.append(node.data)
            return traverse(node.next,accu)
        return traverse(self.head,[])

    def exists(self,func): #pass a method that returns a beef boolean
        def traverse(node):
            if node is None:
                return False
            elif func(node):
                return True
            return traverse(node.next)
        return traverse(self.head)





if __name__ == "__main__":
    love = ChainHash(10)
    for i in range(0,100):
        love.insert(i,i)
    print(love.get(7))




