
#inserting a node at begninng
def push(self,new_data):
    new_node=Node(new_data)
    self.new_node=self.head
    self.head=new_node

#inserting a node in b/w linked list

def insertbetween(self,prev_node,new_node):
    if prev_node is None:
        print("previous node exists:")
        return
    new_node=Node(new_data)
    new_node.next=prev_node.next#make next of new node as next of previous node
    prev_node.next=new_node

#insering a node in last of node

def append(self,new_data):

    new_node=Node(new_data)

    if self.head is None:
        self.head=new_node
        return
    last = self.head
    while (last.next):
        last = last.next

    # 6. Change the next of last node
    last.next = new_node
