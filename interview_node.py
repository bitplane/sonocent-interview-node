"""
Module for interview test node thingy
"""

class InterviewNode(object):
    """
    Simple class for a node in a graph
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





