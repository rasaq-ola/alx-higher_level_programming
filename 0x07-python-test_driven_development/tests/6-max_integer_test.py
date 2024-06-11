#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_max_at_end(self):
        """Test list where the max value is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test list where the max value is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test list where the max value is in the middle."""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_negative(self):
        """Test list with one negative number."""
        self.assertEqual(max_integer([1, -4, 3, -2]), 3)

    def test_all_negative(self):
        """Test list with all negative numbers."""
        self.assertEqual(max_integer([-1, -4, -3, -2]), -1)

    def test_one_element(self):
        """Test list with a single element."""
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_none(self):
        """Test None as input."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integers(self):
        """Test list with non-integer types."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3, 4])

if __name__ == '__main__':
    unittest.main()
