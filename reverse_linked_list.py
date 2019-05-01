class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        values = []

        iter = self

        while iter != None:
            values.append(iter.value)
            iter = iter.next

        return ' -> '.join(values)

    @staticmethod
    def makelist(values):
        node = None

        for i in range(len(values)-1, -1, -1):
            node = Node(values[i], node)

        return node

def reverse(node, s, f):
    dummy = Node(0, node)
    iter = node
    start = dummy
    end = node
    rstart = node
    rend = node

    i = 1

    if s == f: return node

    while i < s:
        start = iter
        if iter != None:
            iter = iter.next
        else:
            return node
        i += 1

    rstart = iter
    prev = iter

    if iter == None: return node

    next = iter.next

    while i < f:
        curr = next
        if next != None:
            next = next.next
        else:
            return node
        curr.next = prev
        prev = curr
        i += 1

    rend = prev
    end = next

    start.next = rend
    rstart.next = end

    return dummy.next

values = input('Enter a list: ').split(',')
s, f = map(lambda x: int(x), input('Enter start and finish: ').split(','))
node = Node.makelist(values)
print(node)
print(reverse(node, s, f))
