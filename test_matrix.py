import unittest;

from algorithms.matrix import Matrix;

class MatrixCase(unittest.TestCase):

    def setUp(self):
        self.matrix = [[1,1],[1,1]];

    def test_init(self):
        result = Matrix(self.matrix);
        self.assertEqual(result.get_matrix(), [[1,1],[1,1]]);

    def test_add(self):
        result = Matrix.add(self.matrix, [[1,2],[3,4]]);
        self.assertEqual(result, [[2,3],[4,5]]);
 
    def test_opposite(self):
        result = Matrix.opposite(self.matrix);
        self.assertEqual(result, [[-1,-1],[-1,-1]]);
 
    def test_subtract(self):
        result = Matrix.subtract(self.matrix, [[1,1],[1,1]]);
        self.assertEqual(result, [[0,0],[0,0]]);
 
    def test_multiply(self):
        result = Matrix.strassen_multiply_recursive(self.matrix, [[1,2],[3,4]]);
        self.assertEqual(result, [[4,6],[4,6]]);
