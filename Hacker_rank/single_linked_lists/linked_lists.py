class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_data(self, prev_node, data):
        if not prev_node:
            print("Node does" + prev_node + " does not exist in list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    def del_position(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        count = 1

        if count == pos:
            head = self.head
            cur_node = head.next
            head.next = cur_node.next
            cur_node = None
            return

        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    def length(self):
        count = 1
        cur_node = self.head

        while cur_node.next != None:
            cur_node = cur_node.next
            count +=1

        return count

    def node_swap(self, key_1, key_2):
        if key_1 == key_2:
            return

        cur_node_1 = self.head
        prev_node_1 = None

        while cur_node_1 and cur_node_1.data != key_1:
            prev_node_1 = cur_node_1
            cur_node_1 = cur_node_1.next

        cur_node_2 = self.head
        prev_node_2 = None

        while cur_node_2 and cur_node_2.data != key_2:
            prev_node_2 = cur_node_2
            cur_node_2 = cur_node_2.next

        if not cur_node_1 and cur_node_2:
            print("Either one or both of these nodes does not exist!")
            return

        cur_node_1.data = key_2
        cur_node_2.data = key_1

    def reverse(self):
        cur_node = self.head
        prev_node = None

        while cur_node:
            temp = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = temp
        self.head = prev_node

list = LinkedList()
list.append("A")
list.append("B")
list.append("C")
list.append("D")
print(list.reverse())
list.print_list()
