class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += str(temp.data) + " "
            temp = temp.next
        print(linked_list)

    def insert_node(self, val, pos):
        target = Node(val)

        if pos == 0:
            target.next = self.head
            self.head = target
            return

        def getPrev(pos):
            temp = self.head
            count = 1
            while count < pos:
                temp = temp.next
                count += 1

            return temp

        prev = getPrev(pos)
        target.next = prev.next
        prev.next = target

    def delete_node(self, key):
        temp = self.head

        if temp.data == key:
            self.head = temp.next
            temp = None
            return

        while temp.next.data != key:
            temp = temp.next

        target = temp.next
        temp.next = target.next
        target = None
        return




linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.printLinkedList()

linked_list.insert_node(10, 2)

linked_list.printLinkedList()

linked_list.delete_node(10)

linked_list.printLinkedList()

class hello:
    def __init__(self, a='Welcomn'):
        self.a = a


h = hello()


