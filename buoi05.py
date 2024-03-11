"-----------------List-----------------"
"""import random

city_names = ["Paris", "London", "Rome", "Berlin", "Marid"]
city_temps = {city: random.randint(20, 30) for city in city_names}
print(city_temps)

above_25 = {city: temp for (city, temp) in city_temps.items() if temp > 25}
print(above_25)
"""

"""words = ["apple", "orange", "banana", "apple", "orange", "apple"]


def counts_word_frequency(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq


print(counts_word_frequency(words))"""

# Common Keys


"""def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
print(merge_dicts(dict1, dict2))"""


"""# Key with the Highest Value
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)


my_dict = {"a": 5, "b": 9, "c": 2}

print(max_value_key(my_dict))"""


"""# Reverse Key-Value Pairs
def reverse_dict(my_dict):
    return {value: key for key, value in my_dict.items()}


my_dict = {"a": 1, "b": 2, "c": 3}
print(reverse_dict(my_dict))"""


"""# Conditinal Filter
def filter_dict(d, condition):
    return {k: v for k, v in d.items() if condition(k, v)}


my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
print(filtered_dict)  # Output: {'b': 2, 'd': 4}
"""

"""# Same Frequency
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]


def check_same_frequency(list1, list2):
    return sorted(list1) == sorted(list2)

print(check_same_frequency(list1, list2))  # Output: False"""
"------------- Tuple ---------------"
"""newTuple = ('a', 'b', 'c', 'd', 'e')
print(newTuple) # Output: ('a', 'b', 'c', 'd', 'e')
newTuple1 = tuple("abcde")
print(newTuple1) # Output: ('a', 'b', 'c', 'd', 'e')
print(newTuple[1]) # Output: b
print(newTuple[-1]) # Output: e
print(newTuple[-2]) # Output: d
print(newTuple[1:3]) # Output: ('b', 'c')
print(newTuple[:3]) # Output: ('a', 'b', 'c')
print(newTuple[1:]) #Output: ('b', 'c', 'd', 'e')
print(newTuple[:]) # Output: ('a', 'b', 'c', 'd', 'e')
newTuple[0] = 'f' # Error: 'tuple' object does not support item assignment
for i in newTuple:
    print(i) # Output: a b c d e
    
for i in range(len(newTuple)):
    print(newTuple[i]) # Output: a b c d e
    
print('a' in newTuple) # Output: True

print(newTuple.index('c')) # Output: 2

def searchTuple(p_tuple, element):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"Element {element} found at index {i}"
    return f"Element {element} not found"
    
print(searchTuple(newTuple, 'b')) # Output: Element c found at index 1
"""
"""myTuple = (1, 2, 3, 4, 5)
myTuple1 = (1, 2, 6, 9, 8, 7)

print(myTuple + myTuple1)  # Output: (1, 2, 3, 4, 5, 1, 2, 6, 9, 8, 7)
print(myTuple * 4)  #Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)"""

"""myTuple = (1, 4, 3, 2, 5, 2)
myTuple1 = (1, 2, 6, 9, 8, 7)
print(myTuple.count(2))  # Output: 2"""

# print(tuple([1, 2, 3, 4])) # Output: (1, 2, 3, 4)

"""list1 = [0, 1, 2, 3, 4, 5, 6, 7]
list1[3] = 3
print(list1)  # Output: [0, 1, 2, 3, 4, 5, 6, 7]"""


"""
list1 = [0, 1, 2, 3, 4, 5, 6, 7]
tuple1 = 0, 1, 2, 3, 4, 5, 6, 7

tuple1[1] = 3  # Error: 'tuple' object does not support item assignment
print(list1) #Output [0, 3, 2, 3, 4, 5, 6, 7]
print(tuple1) #Output (0, 1, 2, 3, 4, 5, 6, 7)"""


"""input_tuple = (1, 2, 3, 4)

def sum_product(input_tuple):
    sum = 0
    product = 1
    for i in input_tuple:
        sum += i
        product *= i
    return sum, product


sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)
"""


"""
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

def tuple_elementwise_sum(t1, t2):
    return tuple(map(sum, zip(t1, t2)))
output = tuple_elementwise_sum(tuple1, tuple2)
print(output)  # Output: (5, 7, 9)"""

"""input_tuple = ('Hello', 'World', 'from', 'Python')

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

output_string = concatenate_strings(input_tuple)
print(output_string)  # Output: Hello World from Python"""

"""input_tuple = ((1,2,3), (4,5,6), (7,8,9))

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

output = get_diagonal(input_tuple)
print(output)  # Output: (1, 5, 9)"""


"""tuple1 = (1,2,3,4,5)
tuple2 = (4,5,6,7,8)
def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

output = common_elements(tuple1, tuple2)
print(output)  # Output: (4, 5) """

"------------------Object Oriented Programming-------------------"
"""class StarCookie:
    pass

star_cookie1 = StarCookie()
print(star_cookie1)  # Output: <__main__.StarCookie object at 0x7f8e3c3e3d30>
star_cookie1.weight = 15
star_cookie1.color = "Red"
print(star_cookie1.weight)  # Output: 15
print(star_cookie1.color)  # Output: Red
star_cookie2 = StarCookie()
star_cookie2.weight = 16
star_cookie2.color = "Blue"
print(star_cookie2.weight)  # Output: 16
print(star_cookie2.color)  # Output: Blue"""

"""class StarCookie:
    def __init__(self,color, weight):
        self.color = color
        self.weight = weight
        
starCookie1 = StarCookie("Red",16)
print(starCookie1.color)  # Output: Red
print(starCookie1.weight)  # Output: 16"""

"""class Youtube:
    def __init__(self, username, subscribers):
        self.username = username
        self.subscribers = subscribers
        
user1 = Youtube("Elshad", 0)
print(user1.username)  # Output: Elshad
print(user1.subscribers)  # Output: 0

user2 = Youtube("Renad")
print(user2.username)  # Output: Renad
print(user2.subscribers)  # Output: 0

user2 = Youtube("Renad")
user2.subscribers = 5
print(user2.username)  # Output: Renad
print(user2.subscribers)  # Output: 5"""

"""class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
        
        def subscribe(self,user):
            user.subscribers += 1
            self.subscriptions += 1
            
user1 = Youtube("Elshad")
user2 = Youtube("Renad")
user1.subscribe(user2)
user2.subscribe(user1)
print(f"User1 subscribers: {user1.subscribers}")
print(f"User1 subscriptions: {user1.subscriptions}")
print(f"User2 subscribers: {user2.subscribers}")
print(f"User2 subscriptions: {user2.subscriptions}")"""

"---------------------LinkedList--------------------------"


"""class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


# new_node = Node(10)
# print(new_node)  # Output: 10
new_linked_list = LinkedList(10)
print(new_linked_list.head.data)  # Output: 10"""


# Create Singly Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1


# Test the LinkedList
linked_list = LinkedList("Nguyễn Gia Lộc")
print(linked_list.head.value)  # Output: 'A'
print(linked_list.tail.value)  # Output: 'A'
print(linked_list.length)  # Output: 1
