# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, data, left_node, right_node, parent_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        self.parent_node = parent_node

    def get_item(self):
        print (self.data, self.left_node, self.right_node, self.parent_node)

    def set_left_node(self, num):
        self.left_node = num

    def set_right_node(self, num):
        self.right_node = num

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def get_parent_node(self):
        return self.parent_node


class BinaryTree(object):
    def __init__(self):
        self.head = None

    def print_tree(self):


tree = TreeNode(1,2,3,None)
tree.get_item()
tree.set_left_node(100)
tree.get_item()



