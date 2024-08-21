class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.head = None

    def inserAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node
    
    def printer(self):
        cur = self.head
        print(self.head.data,end=' ')
        while(cur.next):
            print(cur.next.data,end=' ')
            cur = cur.next
        print('\n')

    def remDuplicate(self):
        cur = self.head
        
        

    
head = Node(1)

head.inserAtEnd(2)
head.inserAtEnd(3)
head.inserAtEnd(3)
head.inserAtEnd(3)
head.inserAtEnd(4)
head.inserAtEnd(4)
head.inserAtEnd(5)

head.printer()
   

