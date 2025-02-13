# Dylan Stitt
# Unit 5 Lab 5
# Positional List

from PositionalDoublyBase import *

class PositionalList(PositionalDoublyBase):

    class Position:

        def __init__(self, memberOf, node):
            self.__member_of = memberOf
            self.__node = node

        def __eq__(self, other):
            """Checks if two positions are equal"""
            return (type(self) == type(other)) and (self.__node is other._Position__node)

        def __ne__(self, other):
            """Checks if two positions are not equal"""
            return not (self == other)

        def get_value(self):
            """Returns the value of the position's node"""
            return self.__node.value

    def __iter__(self):
        """Iterator for the Positional List"""
        node = self.header.next
        while node.value is not None:
            yield node.value
            node = node.next

    def __validate(self, position):
        """Return node in specified position or raise exception if position does not belong to list or not a position"""
        if type(position) != self.Position:
            raise TypeError("Position must be of same type")

        if self is not position._Position__member_of:
            raise ValueError("Position does not belong to list")

        return position._Position__node

    def __make_position(self, node):
        """Return new position object for a given node or return None if sentinel"""
        if node is self.header or node is self.trailer:
            return None
        return self.Position(self, node)

    def __insert_between(self, element, pred=None, succ=None):
        """Copy of parent method, returns position object"""
        node = super()._PositionalDoublyBase__insert_between(element, pred, succ)
        return self.__make_position(node)

    def first(self):
        """Make & return the position container of first element in list"""
        return self.__make_position(self.header.next)

    def last(self):
        """Make & return the position container of last element in list"""
        return self.__make_position(self.trailer.prev)

    def before(self, position):
        """Make & return the position container of element before given position"""
        node = self.__validate(position)
        if node.prev is self.header:
            return None
        return self.__make_position(node.prev)

    def after(self, position):
        """Make & return the position container of element after given position"""
        node = self.__validate(position)
        if node.next is self.trailer:
            return None
        return self.__make_position(node.next)

    def add_first(self, element):
        """Add new element to front of list, return new position container"""
        return self.__insert_between(element, self.header, self.header.next)

    def add_last(self, element):
        """Add new element to end of list, return new position container"""
        return self.__insert_between(element, self.trailer.prev, self.trailer)

    def add_before(self, element, position):
        """Insert new element before specified position container, return new position container"""
        node = self.__validate(position)
        return self.__insert_between(element, node.prev, node)

    def add_after(self, element, position):
        """Insert new element after specified position container, return new position container"""
        node = self.__validate(position)
        return self.__insert_between(element, node, node.next)

    def replace(self, position, element):
        """Change the element/node in the specified container, return old element"""
        node = self.__validate(position)
        oldVal = node.value
        node.value = element
        return oldVal

    def delete(self, position):
        """Remove and return element at specified position"""
        node = self.__validate(position)
        return super()._PositionalDoublyBase__delete_node(node)
