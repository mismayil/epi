class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.max = value

    def __str__(self):
        values = []

        iter = self

        while iter != None:
            values.append(str(iter.value))
            iter = iter.next

        return ' -> '.join(values)

    @staticmethod
    def makelist(values):
        node = None

        for i in range(len(values)-1, -1, -1):
            node = Node(values[i], node)

        return node

class Stack:
    def __init__(self):
        self.node = None

    def push(self, value):
        maxval = value

        if self.node != None and int(value) < self.node.max:
            maxval = self.node.max

        self.node = Node(value, self.node)
        self.node.max = maxval

    def pop(self):
        value = None

        if self.node != None:
            value = self.node.value
            self.node = self.node.next

        return value

    def max(self):
        return self.node.max

    def __str__(self):
        return str(self.node)

values = map(lambda x: int(x), input('Enter values: ').split(','))
stack = Stack()
for val in values:
    stack.push(val)

print(stack)
print(stack.max())
print(stack.pop())
print(stack)
print(stack.max())
