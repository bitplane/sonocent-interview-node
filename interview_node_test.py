#!/usr/bin/env python3

import unittest

from interview_node import InterviewNode

class NodeTestCase(unittest.TestCase):
    """
    Holds all the test cases for the interview_node module
    """

    def test_add_child(self):
        """
        Test adding a child to a node
        """
        root = InterviewNode()
        new_node = InterviewNode()

        root.add_child(new_node)

        assert new_node in root.get_children(), "Ensure the node is now a child"


    def test_add_child_cyclic(self):
        """
        Test attempting to add children that are already in this graph
        """
        root = InterviewNode()
        child = InterviewNode()
        grandchild = InterviewNode()

        child.add_child(grandchild)
        grandchild.add_child(root)
        with self.assertRaises(ValueError):
            root.add_child(child)


    def test_get_children(self):
        """
        Test getting the collection of children from parents
        """
        root = InterviewNode()
        new_node = InterviewNode()
        assert len(new_node.get_children()) == 0, "A new node should have 0 children"

        root.add_child(new_node)
        assert len(root.get_children()) == 1, "There should be 1 node after adding one"
        

    def test_complex_graph(self):
        """
        Test a few types of more complex graph
        """

        # Linked-list of 3 items
        first, second, third = [InterviewNode() for _ in range(3)]
        first.add_child(second)
        second.add_child(third)

        assert second in first.get_children()
        assert third in second.get_children()
        assert len(first.get_children()) == 1
        assert len(second.get_children()) == 1
        assert len(third.get_children()) == 0

        # Node with multiple children
        first, second, third = [InterviewNode() for _ in range(3)]
        first.add_child(second)
        first.add_child(third)
        
        assert second in first.get_children()
        assert third in first.get_children()
        assert len(first.get_children()) == 2
        assert len(second.get_children()) == 0
        assert len(third.get_children()) == 0


    def test_get_descendants(self):
        """
        Tests for recursive search of descendants
        """
        root = InterviewNode()
        assert len(root.get_descendants()) == 0, "An empty node shouild have no descendants"

        child = InterviewNode()
        grandchild = InterviewNode()
        great_grandchild = InterviewNode()

        root.add_child(child)
        child.add_child(grandchild)
        grandchild.add_child(great_grandchild)
        descendants = root.get_descendants()

        assert len(descendants) == 3
        assert child in descendants
        assert grandchild in descendants
        assert great_grandchild in descendants


