# -*- coding: utf-8 -*-
import unittest
import mycode

class validateFunctions(unittest.TestCase):
    """
    A very simple demonstration of unit testing on 
    one line method (hello_world()) in mycode.py
    """
    def test_hello_fun(self):
        self.assertEqual(mycode.hello_world(),'hello world')

if __name__ == '__main__':
    unittest.main()