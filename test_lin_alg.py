import unittest
import numpy as np
import math
import linear_algebra


class TestLinAlg(unittest.TestCase):
    def test_vect_add(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        self.assertEqual(linear_algebra.sum_of_vectors(a,b).all(), np.array([5, 7, 9]).all())

    def test_vect_sub(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        self.assertEqual(linear_algebra.diff_of_vectors(a,b).all(), np.array([-3, -3, -3]).all())
    
    def test_mat_add(self):
        a = np.array([[1, 2],[3, 4]])
        b = np.array([[5, 6],[7, 8]])
        self.assertEqual(linear_algebra.sum_of_matrices(a,b).all(), np.array([[6, 8],[10, 12]]).all())

    def test_mat_sub(self):
        a = np.array([[1, 2],[3, 4]])
        b = np.array([[5, 6],[7, 8]])
        self.assertEqual(linear_algebra.diff_of_matrices(a,b).all(), np.array([[6, 8],[10, 12]]).all())

    def test_vect_dot(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        self.assertEqual(linear_algebra.dot_of_vectors(a,b), 32)
    
    def test_mat_prod(self):
        a = np.array([[1, 2, 3],[4, 5, 6]])
        b = np.array([[7, 8, 9, 10],[11, 12, 13, 14],[15, 16, 17, 18]])
        self.assertEqual(linear_algebra.prod_of_matrices(a,b).all(), np.array([[74, 80, 86, 92],[173, 188, 203, 218]]).all())
    
    def test_vect_mag(self):
        a = np.array([1, 1, 2])
    
    def test_transpose(self):
        a = np.array([[1, 2],[3, 4]])
        self.assertEqual(linear_algebra.transpose(a).all(), np.array([[1, 3],[2, 4]]).all())



if __name__ == "__main__":
    unittest.main()
