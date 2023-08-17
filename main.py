from tools import Tools


class Node:

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(Tools):

    def insert_front(self, data):
        """
        usage:
        insert data to the beginning of the list
        :param data: the data
        """
        node = Node(data=data)
        node.next = self.head
        if self.head:
            self.head.prev = node

        self.head = node
        return node

    def insert_after(self, prev, data):
        """
        usage:
        insert data after a specific node
        :param prev: the node to insert after
        :param data: the data
        """
        if not prev:
            print("The prev node cannot be null")
            return

        node = Node(data=data)
        node.next = prev.next
        prev.next = node
        node.prev = prev

        # check if the next node after prev is null
        if node.next:
            node.next.prev = node
        return

    def insert_back(self, data):
        """
        usage:
        insert data to the end of the list
        :param data: the data
        """
        node = Node(data=data)
        if not self.head:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = node
        node.prev = last
        return

    def remove(self, element=None, index=0):
        """
        usage:
        remove a specific element whether by value or index
        :param element: element to be removed
        :param index: index of the element to be removed
        :return: the instance itself
        """
        if index:
            element = self.get_by_index(index)
        temp = self.head
        while temp.data != element and temp.next:
            temp = temp.next

        # if it is between two elements
        if temp.next and temp.prev:
            temp.prev.next = temp.next
            temp.prev = temp.next.prev

        # if it is the head
        elif not temp.prev:
            self.head = temp.next
            temp.next.prev = None

        # if it is the last element
        elif not temp.next:
            temp.prev.next = None

    def print_backward(self):
        """
        usage:
        print the list from tail to head i.e.(reverse)
        """
        full_list = ""
        last = self.get_last()
        while last:
            full_list += f" <--> [{last.data}]"
            last = last.prev

        print("None" + full_list)

    def reverse(self):
        """
        usage:
        reverse the list
        """
        new_head = self.head
        temp = self.head
        while temp:
            prev_node = temp.prev
            next_node = temp.next
            temp.next = prev_node
            temp.prev = next_node
            new_head = temp
            temp = next_node
        if not temp:
            self.head = new_head

    def slice(self, start, end, step=1):
        """
        note:
        it modifies the current list, you can use clone() method to make copy
        usage:
        slice list from start to end with step
        :param start: the starting index
        :param end: the ending index
        :param step: the step u need to take
        :return:
        """

        if step > end:
            raise Exception("SlicingError")

        if start > end and step < 0:
            clone_list = self.clone()
            self.head = self.get_by_index(start, node=True)
            print(self.head.data)
            temp = self.head
            counter = start + step

            while counter >= end:
                try:
                    temp.next = clone_list.get_by_index(counter, node=True)
                except Exception:
                    break
                temp = temp.next
                counter += step
            temp.next = None

        elif step >= 1:
            clone_list = self.clone()
            self.head = self.get_by_index(start, node=True)
            temp = self.head
            counter = start + step
            while counter <= end:
                try:
                    temp.next = clone_list.get_by_index(counter, node=True)
                    print(temp.next.data)
                except Exception:
                    break
                counter += step
                temp = temp.next

            temp.next = None

    def clone(self):
        """
        usage:
        make a list copy
        :return: Object
        """
        clone_data = []
        temp = self.head
        clone_list = DoublyLinkedList()
        while temp:
            clone_data.append(temp.data)
            temp = temp.next
        for data in clone_data:
            clone_list.insert_back(data)
        return clone_list




if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_front(1)
    dll.insert_front(2)
    dll.insert_front(3)
    dll.insert_front(4)
    dll.insert_front(5)
    node = dll.insert_front(6)
    dll.insert_front(7)

    dll.print_forward()
    dll.slice(5, 1, -2)
    dll.print_forward()
