class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# def MiddleNode(head):
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow


# def remove_duplicates(head):
#     current = head
#     while current and current.next:
#         if current.val == current.next.val:
#             current.next = current.next.next
#         else:
#             current = current.next
#     return head


"""def print_nth_from_last(head, n):
    total_length = 0
    current = head
    while current:
        total_length += 1
        current = current.next
    current = head
    for i in range(total_length - n):
        current = current.next
    print(current.val)"""


"""def partition(head, x):
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
    return before_head.next"""


"""def sum_lists(l1, l2):
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
    return dummy.next"""


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
print_list(intersection(new_node, new_node2))
