class Node:
    def __init__(self, data):
        self.data = data  # hodnota uzla
        self.next = None  # odkaz na ďalší uzol

class LinkedList:
    def __init__(self):
        self.head = None  # začiatok zoznamu

    def insert_at_beginning(self, value):
        new_node = Node(value)      # vytvoríme nový uzol
        new_node.next = self.head   # nový uzol ukazuje na pôvodný začiatok
        self.head = new_node        # nový uzol sa stáva novým začiatkom

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")