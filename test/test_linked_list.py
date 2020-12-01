import unittest;

from algorithms.linked_list import *;


class TestNodeEmptyInit(unittest.TestCase):

    def setUp(self):
        self.node = LinkedList.Node();

    def test_data(self):
        self.assertIsNone(self.node.data);

    def test_prv(self):
        self.assertIsNone(self.node.prv);

    def test_nxt(self):
        self.assertIsNone(self.node.nxt);


class TestNodeWithArgsInit(unittest.TestCase):

    def setUp(self):
        self.prv = LinkedList.Node();
        self.nxt = LinkedList.Node();
        self.node = LinkedList.Node(data = 'data', prv = self.prv, nxt = self.nxt);

    def test_data(self):
        self.assertEqual(self.node.data, 'data');

    def test_prv(self):
        self.assertIs(self.node.prv, self.prv);

    def test_nxt(self):
        self.assertIs(self.node.nxt, self.nxt);


class TestNodeTypeError(unittest.TestCase):

    def setUp(self):
        self.obj = object();

    def test_type_error(self):
        with self.assertRaises(TypeError):
            LinkedList.Node(prv = self.obj);

    def test_type_error(self):
        with self.assertRaises(TypeError):
            LinkedList.Node(nxt = self.obj);


class TestLinkedListInit(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList();
        
    def testnil(self):
        self.assertIsInstance(self.linked_list.nil, LinkedList.Node);
    
    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty());


class TestLinkedListBehaviour(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList();
        self.nodes = [LinkedList.Node(data = i) for i in range(3)];

        for node in reversed(self.nodes[1:]):
            self.linked_list.insert(node);

    def test_delete(self):
        self.assertIs(self.linked_list.nil.nxt.nxt, self.nodes[2]);
        self.linked_list.delete(self.nodes[2]);
        self.assertIsNot(self.linked_list.nil.nxt.nxt, self.nodes[2]);

    def test_insert(self):
        self.assertIsNot(self.linked_list.nil.nxt, self.nodes[0]);
        self.linked_list.insert(self.nodes[0]);
        self.assertIs(self.linked_list.nil.nxt, self.nodes[0]);

    def test_search(self):
        self.assertIs(self.linked_list.search(0),self.linked_list.nil);
        self.assertIs(self.linked_list.search(2), self.nodes[2]);


class TestLinkedListError(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList();

    def test_delete_value_error(self):
        with self.assertRaises(ValueError):
            self.linked_list.delete(LinkedList.Node());
    
    def test_delete_type_error(self):
        with self.assertRaises(TypeError):
            self.linked_list.delete(object());

    def test_insert_type_error(self):
        with self.assertRaises(TypeError):
            self.linked_list.insert(object());