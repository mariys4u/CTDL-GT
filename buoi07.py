"""
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    # delete
    def delete(self):
        self.list = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
print(customStack)"""

"---------------------------------------------------------"
"""
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    #  Push
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    # Pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
    
    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]

    #  delete
    def delete(self):
        self.list = None
    

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)"""

"---------------------------------------------------------"

"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("-----")
customStack.pop()
print(customStack)
"""

"----------------------Queue--------------------------------"
"""
class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "The is not any element in the Queue"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None




customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()"""

"---------------------------------------------------------"
"""class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
    
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None




custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.peek())
print(custQueue)"""

"---------------------Exercise1---------------------------------"
# Stack-contructor

"""class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class Stack:
    def __init__(self, value=None):
        self.top = Node(value)
        self.height = 1
my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)
"""


# Stack-pop
"""class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp

my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop().value)

print("\nStack after pop():")
my_stack.print_stack()
"""


# Stack-push
"""class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True


my_stack = Stack(2)

print("Stack before push(1):")
my_stack.print_stack()

my_stack.push(1)

print("\nStack after push(1):")
my_stack.print_stack()
"""
