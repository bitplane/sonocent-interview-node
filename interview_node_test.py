#!/usr/bin/env python3

import unittest

import interview_node

class NodeTestCase(unittest.TestCase):
    """
    Holds all the test cases for the interview_node module
    """

    root = None

    def setUp(self):
        """
        Construct stuff
        """
        self.root = interview_node.create()


    def test_create():
        """
        Test creation of the graph
        """
        assert self.root is not None, "Create the root node"
