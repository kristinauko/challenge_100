'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

#Definition of Linked List
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x 
#         self.next = None


def removeElements(head:ListNode, val):
    """Take linked list, val and remove val elements from the list"""

    current = head
    
    while current and current.val == val:
        current = current.next
    
    new_head = current
    
    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return new_head  
