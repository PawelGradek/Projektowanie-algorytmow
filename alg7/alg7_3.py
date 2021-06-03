class NilNode(object):
    def __init__(self):
        self.red = False


NIL = NilNode()


class RBNode(object):
    def __init__(self,data):
        self.red = False
        self.parent = None
        self.data = data
        self.left = NIL
        self.right = NIL

class RedBlackTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self,data,curr = None):
        self.size += 1
        new_node = RBNode(data)
        if self.root == None:
            new_node.red = False
            self.root = new_node
            return

        currentNode = self.root
        while currentNode != NIL:
            potentialParent = currentNode
            if new_node.data < currentNode.data:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        new_node.parent = potentialParent
        if new_node.data < new_node.parent.data:
            new_node.parent.left = new_node
        else:
            new_node.parent.right = new_node
        self.fix_tree_after_add(new_node)

    def contains(self,data, curr=None):
        if curr == None:
            curr = self.root

        while curr != NIL and data != curr.data:
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def fix_tree_after_add(self,new_node):
        while new_node.parent.red == True and new_node != self.root:
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.red:
                    new_node.parent.red = False
                    uncle.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotate(new_node)

                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.red:

                    new_node.parent.red = False
                    uncle.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:

                        new_node = new_node.parent
                        self.right_rotate(new_node)

                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.left_rotate(new_node.parent.parent)
        self.root.red = False

    def left_rotate(self,new_node):
        sibling = new_node.right
        new_node.right = sibling.left

        if sibling.left != None:
            sibling.left.parent = new_node
        sibling.parent = new_node.parent

        if new_node.parent == None:
            self.root = sibling
        else:
            if new_node == new_node.parent.left:
                new_node.parent.left = sibling
            else:
                new_node.parent.right = sibling
        sibling.left = new_node
        new_node.parent = sibling

    def right_rotate(self,new_node):
        sibling = new_node.left
        new_node.right = sibling.right

        if sibling.right != None:
            sibling.right.parent = new_node
        sibling.parent = new_node.parent
        if new_node.parent == None:
            self.root = sibling
        else:
            if new_node == new_node.parent.right:
                new_node.parent.right = sibling
            else:
                new_node.parent.left = sibling
        sibling.right = new_node
        new_node.parent = sibling

    def is_red(self):
        return self.root != None and self.root.red == 1

    def is_black(self):
        return self.root != None and self.root.black == 1


if __name__ == "__main__":
    tree = RedBlackTree()
    tree.add(1)
    # print(tree.root)
    tree.add(3)
    tree.add(4)
    tree.add(3)
    tree.add(4)
    print(tree.contains(4))
    # print(tree.root)