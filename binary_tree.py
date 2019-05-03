class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def traverse(self, mode='in'):
        if mode == 'pre': print(self.data)
        if self.left != None: self.left.traverse(mode)
        if mode == 'in': print(self.data)
        if self.right != None: self.right.traverse(mode)
        if mode == 'post': print(self.data)

    def height(self):
        return 1 + max(-1 if self.left == None else self.left.height(), -1 if self.right == None else self.right.height())

    def checkbalanced(self):
        leftbalance = (True, -1) if self.left == None else self.left.checkbalanced()
        if not leftbalance[0]: return leftbalance
        rightbalance = (True, -1) if self.right == None else self.right.checkbalanced()
        if not rightbalance[0]: return rightbalance
        isbalanced = abs(leftbalance[1]-rightbalance[1]) <= 1
        height = max(leftbalance[1], rightbalance[1]) + 1
        return (isbalanced, height)

    def isbalanced(self):
        return self.checkbalanced()[0]

    @staticmethod
    def checksymmetric(me, other):
        if me == None and other == None: return True
        if me != None and other != None:
            return me.data == other.data and \
            Node.checksymmetric(me.left, other.right) and \
            Node.checksymmetric(me.right, other.left)
        return False

    def issymmetric(self):
        return Node.checksymmetric(self.left, self.right)

tree = Node(314, Node(6, right=Node(561, right=Node(3))), Node(7, Node(12, Node(1))))
print(tree.isbalanced())
