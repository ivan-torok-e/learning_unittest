import os
import sys
sys.path.append(os.getcwd())
import unittest
import source.hello_world as hello_world

class test_hellow_world(unittest.TestCase):

    def test_hw(self):
        self.assertEqual(hello_world.hw(), 'Hello world!')


if __name__ == '__main__':
    unittest.main()