class Node:
    def __init__(self, data, next_node=None):
        """
        Represent a linked list

        Args:
            data(int) - data to be inserted
            next_node(Node)- the next node of the linked list
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        self.__data = value


    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is not None and  not isinstance(value, int):
            raise TypeError("next node must be an Object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.head.data:
            new_node.__next_node = self.__head
            self.head = new_node