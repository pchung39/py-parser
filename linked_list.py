#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item(object):
    def __init__(self, data, next_item = None):
        self.data = data
        self.next_item = next_item

    def get_item(self):
        return self.data

    def set_next(self, setnext):
        self.next_item = setnext

    def get_next(self):
        return self.next_item

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self,item):
        temp = Item(item)
        temp.set_next(self.head)
        self.head = temp

    def find(self, item):
        current = self.head
        while current != None:
            if current == item:
                print "Found It!"
            else:
                current = current.get_next()

    def print_list(self):
        node = self.head
        while node:
            print node.get_item()
            node = node.get_next()

    def size(self):
        index = 0
        current = self.head
        while current != None:
            index += 1
            current = current.get_next()
        print index

    def insert(self,item,lpos):
        if lpos == 0:
            item_insert = Item(item, self.head)
            self.head = item_insert
            return
        previous = self.head
        current = self.head.get_next()
        index = 1
        while index != lpos:
            index += 1
            previous = current
            current = current.get_next()
            if current == None:
                return None

        item_insert = Item(item, current)
        previous.set_next(item_insert)

    def remove(self,item):
        current_node = self.head
        prev_node = None

        while current_node != None:
            print current_node
            if current_node.data == item:
                prev_node.next_item = current_node.next_item

            prev_node = current_node
            current_node = current_node.next_item

    def sort(self):
        node = self.head
        next_node = node.get_next()
        while node and next_node != None:
            if node > next_node:
                node, next_node = next_node, node
            return node, next_node


    def sort_list(self):
        if self.head and self.head.next_item:
            i = self.head
            while i.next_item:
                selected = i
                j = i.next_item
                while j:
                    if j.data < selected.data:
                        selected = j
                    j = j.next_item
                if not selected == i:
                    i.data, selected.data = selected.data, i.data
                i = i.next_item



'''
        while True:
            if node < next_node:
                node, next_node = next_node, node
                next_node.set_next(node)
                node.set_next(next_node + 1)
            node = node.get_next()
            next_node = node.get_next()
        print node, next_node
            node = next_node
            next_node = node.next_item
'''
myList = LinkedList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
myList.add(5)
myList.sort_list()
myList.print_list()


