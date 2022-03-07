from LinkedList import LinkedList

class AnimalShelter:

    def __init__(self):
        self.animals = LinkedList()

    def enqueue(self, ID, type):

        self.animals.add((type, ID))

    def dequeueAny(self):
        node = self.animals.head
        self.animals.head = self.animals.head.next

        return node.value

    def dequeueDog(self):

        node = self.animals.head

        if node.value[0] == 'dog':
            return node.next.value

        while node.next:
            if node.next.value[0] == 'dog':
                type, ID = node.next.value
                node.next = node.next.next
            node = node.next

        return type, ID

    def dequeueCat(self):
        node = self.animals.head

        if node.value[0] == 'cat':
            return node.next.value

        while node.next:
            if node.next.value[0] == 'cat':
                type, ID = node.next.value
                node.next = node.next.next
            node = node.next

        return type, ID
