#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
            
    def remove(self, data):
        if not self.head:
            raise Exception("List is empty")
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        last_node=self.head
        for Node in self:
            if node.data ==data:
                last_node.next=node.next
                return
            last_node=node
        
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next       
 
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end = '')

n = int(input('How many elements would you like to remove? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.remove(data)
print('The linked list: ', end = '')
a_llist.display()


# In[ ]:




