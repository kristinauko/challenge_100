"""Queue practice: implement Queue class and its methods enqueue(), dequeue(), 
is_empty(), size() and printQueue(). 

Use methods to create a queue and write a function which checks for an item
in the queue. Return True if item exists and False if it was not found."""


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def printQueue(self):
        return self.queue


def pushItemsToQueue(num):

    lst = Queue()

    for i in range(num):
        lst.enqueue(i)

    return lst


def findItem(num):

    queue = pushItemsToQueue(8)
    size = queue.size()
    i = 0

    while i < size:
        item = queue.dequeue()

        if num == item:
            return True

        i += 1

    return False


print(findItem(8))






