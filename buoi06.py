"""class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, data):  # Cau 2: Insert at the begining of the linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, data):  # Cau 3: Insert at the end of the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            deleted_node = temp_node.next
            temp_node.next = temp_node.next.next
            if temp_node.next is None:
                self.tail = temp_node
        self.length -= 1
        return deleted_node.data

    def reverse(self):  # Cau 5: Reverse the linked list
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def middle(self):  # Cau 6: Middle of the linked list
        if self.head is None:
            return
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.data)
        while current_node.next:
            if current_node.next.data in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.data)
                current_node = current_node.next
        self.tail = current_node

    def merge(self, llist):  # Cau 8: Merging two sorted linked list
        p = self.head
        q = llist.head
        s = None
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s
        while p is not None and q is not None:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if p is None:
            s.next = q
        if q is None:
            s.next = p
        return new_head

    # Cau 9 Remove duplicate sorted linked list
    def remove_duplicate_sorted(self):
        current = self.head
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
                self.length -= 1
            else:
                current = current.next
        return self.head

    # Cau 10 Remove Linked List Elements
    def remove_elements(self, val):
        current = self.head
        while current.next is not None:
            if current.next.data == val:
                current.next = current.next.next
                self.length -= 1
            else:
                current = current.next
        return self.head

    # Cau 11: Reverse Linked List II
    def reverse_between(self, m, n):
        if m == n:
            return self.head
        prev = None
        current = self.head
        for i in range(m - 1):
            prev = current
            current = current.next
        connection = prev
        tail = current
        for i in range(n - m + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        if connection:
            connection.next = prev
        else:
            self.head = prev
        tail.next = current
        return self.head

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.data)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result"""

# new_linked_list = LinkedList()
# new_linked_list.append(1)
# new_linked_list.append(2)
# new_linked_list.append(3)
# new_linked_list.append(4)
# new_linked_list.append(5)
# print(new_linked_list)  # Cau 1
# new_linked_list.prepend(0)  # Cau 2
# new_linked_list.append(1)  # Cau 3
# print(new_linked_list.delete_at_index(0))  # Cau 4
# print(new_linked_list.reverse())  # Cau 5
# print(new_linked_list.middle())  # Cau 6

# Cau 7
# new_linked_list = LinkedList()
# new_linked_list.append(1)
# new_linked_list.append(2)
# new_linked_list.append(4)
# new_linked_list.append(3)
# new_linked_list.append(4)
# new_linked_list.append(2)
# new_linked_list.remove_duplicates()
# print(new_linked_list)  # 1 -> 2 -> 4 -> 3


#     # Cau 8

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         temp_node = self
#         result = ""
#         while temp_node is not None:
#             result += str(temp_node.val)
#             if temp_node.next is not None:
#                 result += " -> "
#             temp_node = temp_node.next
#         return result

# def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
#     # Check if either of the lists is null
#     if l1 is None:
#         return l2
#     if l2 is None:
#         return l1
#     # Choose head which is smaller of the two lists
#     if l1.val < l2.val:
#         temp = head = ListNode(l1.val)
#         l1 = l1.next
#     else:
#         temp = head = ListNode(l2.val)
#         l2 = l2.next
#     # Loop until any of the list becomes null
#     while l1 is not None and l2 is not None:
#         if l1.val < l2.val:
#             temp.next = ListNode(l1.val)
#             l1 = l1.next
#         else:
#             temp.next = ListNode(l2.val)
#             l2 = l2.next
#         temp = temp.next
#     # Add all the nodes in l1, if remaining
#     while l1 is not None:
#         temp.next = ListNode(l1.val)
#         l1 = l1.next
#         temp = temp.next
#     # Add all the nodes in l2, if remaining
#     while l2 is not None:
#         temp.next = ListNode(l2.val)
#         l2 = l2.next
#         temp = temp.next
#     return head


# # Input: l1 = [1,2,4], l2 = [1,3,4]
# # Output: [1,1,2,3,4,4]
# l1 = ListNode()
# l2 = ListNode(1)
# print(mergeTwoLists(l1, l2))  # 1 -> 1 -> 2 -> 3 -> 4 -> 4


"""# Cau 9
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        temp_node = self
        result = ""
        while temp_node is not None:
            result += str(temp_node.val)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    def remove_duplicates(self):
        current = self
        while current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return self


# # Input: head = [1,1,2,3,3]
# Output: [1,2,3]
l1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print(l1.remove_duplicates())  # 1 -> 2 -> 3"""


"""# Cau 10
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def remove_elements(self, val):
        current = self.head
        while current.next is not None:
            if current.next.data == val:
                current.next = current.next.next
                self.length -= 1
            else:
                current = current.next
        return self.head"""


"""# Cau 11
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev"""


"""# Cau 12
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        temp_node = self
        result = ""
        while temp_node is not None:
            result += str(temp_node.val)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result


def Palindrome(head: ListNode) -> bool:
    # Create a list to store the values of the linked list
    values = []
    # Create a pointer to the head of the linked list
    current = head
    # Iterate through the linked list and store the values in the list
    while current is not None:
        values.append(current.val)
        current = current.next
    # Check if the list is a palindrome
    return values == values[::-1]


# Test cases
# Create a linked list
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
# Test the function
print(Palindrome(head))  # True"""


"""# Cau 13
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


def MiddleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


new_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
middle = MiddleNode(new_list)
print(middle.val)"""


# Question interview 1
"""class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


new_node = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
print_list(new_node) # 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5 -> None
print_list(remove_duplicates(new_node)) # 1 -> 2 -> 3 -> 4 -> 5 -> None"""

# Question interview 2
"""class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def print_nth_from_last(head, n):
    total_length = 0
    current = head
    while current:
        total_length += 1
        current = current.next
    current = head
    for i in range(total_length - n):
        current = current.next
    print(current.val)


new_node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(new_node) # 1 -> 2 -> 3 -> 4 -> 5 -> None
print_nth_from_last(new_node, 2) # 4"""


# Question interview 3
"""class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
def partition(head, x):
    before = before_head = ListNode(0)
    after = after_head = ListNode(0)
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_head.next
    return before_head.next


new_node = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
print_list(new_node) # 1 -> 4 -> 3 -> 2 -> 5 -> 2 -> None
print_list(partition(new_node, 3)) # 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None
"""

# Question interview 4
"""class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
def sum_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        value = 0
        if l1:
            value += l1.val
            l1 = l1.next
        if l2:
            value += l2.val
            l2 = l2.next
        value += carry
        carry = value // 10
        value = value % 10
        current.next = ListNode(value)
        current = current.next
    return dummy.next


new_node = ListNode(7, ListNode(1, ListNode(6)))
new_node2 = ListNode(5, ListNode(9, ListNode(2)))
print_list(sum_lists(new_node, new_node2))  # Output: 2 -> 1 -> 9 -> None"""


"""# Question interview 5
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def intersection(l1, l2):
    if not l1 or not l2:
        return None
    a = l1
    b = l2
    while a != b:
        a = a.next if a else l2
        b = b.next if b else l1
    return a


new_node = ListNode(3, ListNode(1, ListNode(5, ListNode(9))))
new_node2 = ListNode(2, ListNode(4, ListNode(6)))
print_list(intersection(new_node, new_node2)) # None"""
