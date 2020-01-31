"""
Module for nodes in the DAG project
"""

class InterviewNode(object):
    """
    Simple class for a node in a directed asyclic graph
    """

    _children = None

    def __init__(self):
        """
        Construct empty node
        """
        self._children = set()


    def add_child(self, other):
        """
        Add the child to this parent
        """
        if other is self:
            raise ValueError("Can't add a node to itself")

        if other in self._children:
            raise ValueError("This node can't contain a reference to itself")

        if self in other.get_descendants():
            raise ValueError("Can't add cyclic references to a DAG")

        self._children.add(other)


    def get_children(self):
        """
        Returns children of this node
        """
        return self._children


    def get_descendants(self):
        """
        Return all descendants
        """
        ret = set()
        
        for child in self.get_children():
            if child not in ret:
                ret.add(child)
                ret = ret | child.get_descendants()

        return ret

