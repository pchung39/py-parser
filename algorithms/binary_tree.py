# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def get_left_node(self):
        return(self.left_node)

    def get_right_node(self):
        return(self.right_node)

    def add(self,value):
        if self.root == None:
            self.root = TreeNode(value)
        else:


    def insert_left(self, node):
        if self.left_node == None:
            self.left_node = TreeNode(node)
        else:
            new_node = TreeNode(node)
            new_node.left_node = self.left_node
            self.left_node = new_node.left_node

    def insert_right(self, node):
        if self.right_node == None:
            self.right_node = TreeNode(node)
        else:
            new_node = TreeNode(node)
            new_node.right_node = self.right_node
            self.right_node = new_node.right_node


tree = BinaryTree()
t = TreeNode('a')
tree.insert_left('b')
print(t.left_node)
tree.insert_right('c')
print(t.right_node)



