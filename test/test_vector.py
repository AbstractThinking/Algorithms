import unittest;

from algorithms.vector import Vector;

class VectorCase(unittest.TestCase):

    def test_init(self):
        v = Vector.create(2, val=1);
        self.assertEqual(v, [1,1]);
        v = Vector(v);
        self.assertEqual(v.get_vector(), [1,1]);
        v.set_vector([0]);
        self.assertEqual(v.get_vector(), [0]);

    def test_add(self):
        self.assertEqual(Vector.add([1,1], [1,2]), [2,3]);

    def test_subtract(self):
        self.assertEqual(Vector.subtract([1,2], [1,1]), [0,1]);

    def test_opposite(self):
        self.assertEqual(Vector.opposite([1,1]), [-1,-1]);

    def test_dot_product(self):
        self.assertEqual(Vector.dot_product([1,2],[3,4]), 11);

    

if __name__ == '__main__':
    unittest.main();