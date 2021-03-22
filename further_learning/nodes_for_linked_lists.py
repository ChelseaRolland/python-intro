class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

my_node = Node(44)
print(my_node.get_value())  #44

class LinkedList:
    def __init__(self, value = None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        str_lst = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                str_lst += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
        return str_lst

#Testing the Linked List Case
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
