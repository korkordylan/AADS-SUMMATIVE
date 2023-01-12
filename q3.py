class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def check(self, data_list):
        contents = []
        node = self.head
        while node != None:
            contents += [node.data]
            node = node.next
        return contents == data_list

class HashTable():
    """implements a hash table of size k with all entries empty linked lists

    For a HashTable h:
        h.lookup(pos) returns the linked list in position pos
        h.check(data) checks that the current content is the same as data
        h.print_table prints a representation of h
    """
    def __init__(self, k):
        self.__table = []
        self.__size = k
        for idx in range(k):
            L = LinkedList()
            self.__table += [L]
            
    def lookup(self, pos):
        return self.__table[pos]
    
    def _contents(self):
        buckets = []
        for idx in range(self.__size):
            bucket = []
            node = self.__table[idx].head
            while node != None:
                bucket += [node.data]
                node = node.next
            buckets += [bucket]
        return buckets
    
    def check(self, data):
        if len(data) != self.__size: return False
        for idx in range(self.__size):
            bucket = self._contents()[idx][:]
            bucket.sort()
            bucket2 = data[idx][:]
            bucket2.sort()
            if bucket != bucket2: return False
        return True

    def print_table(self):
        print (self._contents())

#ANSWER HERE 

def hash(d):
    """given a list d of instructions to add or delete keys to a hash table 
    returns the hash table after these instructions have been applied using
    hash function h(k) = 2k + 4 mod 13 
    
    the instructions are either '+k' or '-k' for some positive integer k to indicate
    that k is to be added or deleted
        
    separate chaining is used for collision handling
    """
    
    h = HashTable(13)                             
    
    # Your code to apply the instructions goes here
    # create a function that inserts the value into the hash table
    def insert(self,key,value):
        linked_list = h.lookup(value)
        node = linked_list.head
        while node is not None:
            if node.data == key:
                node.data = (key)
                return
            node = node.next
        node = Node(key)
        node.next = linked_list.head
        linked_list.head = node
        linked_list.size += 1

    def delete(self,key,value):
        linked_list = h.lookup(value)
        node = linked_list.head 

        if node.data == key:
            linked_list.head = node.next
            node.next = None
            linked_list.size -= 1 
        else:
            prev = node
            node = node.next
            while node is not None:
                if node.data == key:
                    prev.next = node.next
                    node.next = None 
                    linked_list.size -= 1 
                    break
                prev = node
                node = node.next



    # Split the string in the array to change it into an integer
    for x in d:
        # idx = (2*key+4)%13
        if "+" in x:    
            key = int(x.split('+')[1])
            idx = (2*key+4)%13
            insert(h,key, idx)
        else:
            key = int(x.split('-')[1])
            idx = (2*key+4)%13
            delete(h,key,idx)
            
        # if x > 0:
        #     insert(h,key, idx)

        # else:
        #     delete(h,key,idx)


    return h
            
            
            



    




