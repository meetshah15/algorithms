# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, val, pos):
        target = ListNode(val)
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


class Solution:
    def addTwoNumbers(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
        first_num = 0
        i = 1
        while l1.next:
            first_num += l1.val * i
            l1 = l1.next
            i *= 10
        first_num += l1.val * i

        second_num = 0
        i = 1
        while l2.next:
            second_num += l2.val * i
            l2 = l2.next
            i *= 10
        second_num += l2.val * i

        sum = str(first_num + second_num)[::-1]

        final = LinkedList()
        head = None

        for i in sum:
            new_node = ListNode(i)
            if head:
                while final.next:
                    final = final.next
                final.next = new_node
            else:
                head = True
                final.next = new_node

        return final


if __name__ == '__main__':
    solution = Solution()
    linked_list = LinkedList()
    linked_list.head = ListNode(2)

    second_node = ListNode(4)
    third_node = ListNode(6)

    linked_list.head.next = second_node
    second_node.next = third_node

    linked_list1 = LinkedList()
    linked_list1.head = ListNode(5)

    second_node = ListNode(6)
    third_node = ListNode(4)

    linked_list1.head.next = second_node
    second_node.next = third_node

    solution.addTwoNumbers(linked_list, linked_list1)
