# day54.py
# Day 54: Intro to Unit Testing with unittest

import unittest

# --- 1. FUNCTIONS WE WANT TO TEST ---

def add(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

def reverse_string(text):
    return text[::-1]


# --- 2. UNIT TEST CLASS ---

class TestMyFunctions(unittest.TestCase):

    # Test 1: Testing the add() function
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # Test 2: Testing the is_even() function
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    # Test 3: Testing the reverse_string() function
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")


# --- 3. RUNNING THE TESTS ---
if __name__ == '__main__':
    unittest.main()