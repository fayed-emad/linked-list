
class Tools:

    def __init__(self):
        self.head = None

    def update_element(self, old_ele, new_ele):
        """
        usage:
        replace an element with new one
        :param old_ele: the old element
        :param new_ele: the new one
        :return: None
        """
        temp = self.head
        while temp.data != old_ele and temp:
            temp = temp.next
        temp.data = new_ele

    def get_length(self) -> int:
        """
        usage:
        getting the length of the list
        :return: length of the list [int]
        """
        temp = self.head
        if not temp:
            return 0

        counter = 1
        while temp.next:
            counter += 1
            temp = temp.next
        return counter

    def get_last(self):
        """
        usage:
        get the last node
        :return: last node [object]
        """
        last = self.head
        while last.next:
            last = last.next
        return last

    def peak(self):
        return self.head.data

    def print_from(self, start_node):
        """
        usage:
        print list starting from a specific node
        :param start_node: the starting node
        """
        full_list = ""
        counter = 0
        while start_node:
            if not counter:
                full_list += f"[{start_node.data}] <--> "
            else:
                full_list += f"[{start_node.data}] <--> "
            start_node = start_node.next
            counter += 1

        print(full_list + "None")

    def get_by_index(self, index, is_dll=True, node=False):
        """
        note:
        index starting from 1 not 0
        usage:
        get a specific element by index
        you can use negative to get the image index
        example -1 = last element
        :param index: the element position
        :param is_dll: is DoublyLinkedList or not default: True
        :return temp.data: the node data
        """
        # checks if index is greater than the list length
        # of equal to zero
        if abs(index) > self.get_length() or not index:
            raise Exception("ListOutOfIndex")

        # if the index is negative
        # search backward
        if index < 0 and is_dll:
            temp = self.get_last()
            counter = self.get_length()
            index = (self.get_length() + 1) + index
            while counter != index and temp:
                temp = temp.prev
                counter -= 1
            if node:
                return temp
            return temp.data
        # if it is positive
        # search forward
        elif index > 0:
            temp = self.head
            counter = 1
            while counter != index and temp:
                counter += 1
                temp = temp.next
            if node:
                return temp
            return temp.data

    def get_element_index(self, element):
        """
        usage:
        get the index of the passed element
        :param element: the element
        :return: the element index [int]
        """
        temp = self.head
        counter = 1
        while temp.data != element and temp:
            temp = temp.next
            counter += 1
        return counter

    def print_forward(self):
        """
        usage:
        print the list from head to tail
        """
        temp = self.head

        full_list = ""
        while temp:
            full_list += f"[{temp.data}] <--> "
            temp = temp.next
        print(full_list + "None")


