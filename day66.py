"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    def push(self, new_data):
        new_node = ListNode(new_data)
        if self.head == None:
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node
        
        self.tail = new_node

    def printNode(self):
        curr = self.head
        while curr:
           print(curr.data)
           curr = curr.next

    def removeNode(self, val):

        if self.head != None and self.head.data == val:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
                return

        current = self.head

        while current.next != None:
            if current.next.data == val:
                current.next = current.next.next
                if current.next == None:
                    self.tail = current
            else:
                current = current.next

        return


if __name__== "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(6)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    print(llist.tail.data)
    llist.removeNode(6)
    llist.printNode()
    print(llist.tail.data)




