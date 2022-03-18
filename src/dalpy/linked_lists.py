"""Module that holds classes related to linked lists.

This module contains the ``SinglyLinkedListNode` and `DoublyLinkedListNode` classes. `SinglyLinkedListNode` can be used
to recursively define a singly linked list. `DoublyLinkedListNode` can be used to recursively define a doubly linked
list. Problems or algorithms that operate on linked lists should take an object of either of these classes.

Examples:
    A singly linked list can be created as follows:

        s = SinglyLinkedListNode(1)
        s.next = SinglyLinkedListNode(2)
        s.next.next = SinglyLinkedListNode(3)

    A doubly linked list can be created as follows:

        d = DoublyLinkedListNode(1)
        d.next = DoublyLinkedListNode(2)
        d.next.prev = d
        d.next.next = DoublyLinkedListNode(3)
        d.next.next.prev = d.next
"""


class SinglyLinkedListNode:
    """Represents a singly linked list node.

    Attributes:
        data: The data stored in the node. This can be any type.
        next: A `SinglyLinkedListNode` representing the node that follows it this node in a singly linked list.
    """

    def __init__(self, data=None, next_node=None):
        """Initializes a `SinglyLinkedListNode` in `O(1)` time.

        Args:
            data: The data to be stored in the node. This can be of any type. By default, this is `None`.
            next_node: The `SinglyLinkedListNode` to follow this `SinglyLinkedListNode`. By default, this is `None`.
        """
        self.data = data
        self.next = next_node


class DoublyLinkedListNode:
    """Represents a doubly linked list node.

    This class represents a doubly linked list node.

    Attributes:
        data: The data stored in the node. This can be of any type.
        next: A `DoublyLinkedListNode` representing the node that follows this node in a doubly linked list.
        prev: A `DoublyLinkedListNode` representing the node that precedes this node in a doubly linked list.
    """

    def __init__(self, data=None, next_node=None, prev_node=None):
        """Initializes a doubly linked list node in `O(1)` time.

        Args:
            data: The data to be stored in the node. This can be of any type. By default, this is `None`.
            next_node: The `DoublyLinkedListNode` to follow this `DoublyLinkedListNode`. By default, this is `None`.
            prev_node: The `DoublyLinkedListNode` to precede this `DoublyLinkedListNode`. By default, this is `None`.
        """
        self.data = data
        self.prev = prev_node
        self.next = next_node

