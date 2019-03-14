class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def get_stack(self):
        return self.items

def reverse_string(stack, input_string):
    reverse_string = ""

    for i in input_string:
        stack.push(i)

    for i in range(0, len(input_string)):
        reverse_string += stack.pop()

    return reverse_string

def binary(stack, num):
    bin_str = ""

    if num == 0:
        return 0

    else:
        while num // 2 != 0:
            if(num % 2 == 1):
                stack.push("1")
            elif(num % 2 == 0):
                stack.push("0")
            num = num // 2

        stack.push("1")
        length = len(stack.get_stack())

        for i in range(0, length):
            bin_str += stack.pop()

        return bin_str

def is_match(p1, p2):
    if(p1 == "{" and p2 == "}"):
        return True
    elif(p1 == "(" and p2 == ")"):
        return True
    elif(p1 == "[" and p2 == "]"):
        return True
    else:
        return False

def balanced(input_string):
    stack = Stack()
    length = len(input_string)
    is_balanced = True
    index = 0

    while index < length and is_balanced:
        paren = input_string[index]

        if paren in "{[(":
            stack.push(paren)
        else:
            if stack.is_empty():
                is_balanced = False
            else:
                top = stack.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if stack.is_empty() and is_balanced:
        return True
    else:
        return False

# s = Stack()
# s.push("A")
# s.push("B")
# s.push("C")
# s.push("D")
# print(s.get_stack())
# s.pop()
# print(s.get_stack())
# print(s.peek())
# print(s.is_empty())
#
# print(reverse_string(s, "hello"))

# print(binary(s, 20))
# print(binary(s, 2))

print(balanced("(({{{}}}))"))
# print(s.get_stack())
