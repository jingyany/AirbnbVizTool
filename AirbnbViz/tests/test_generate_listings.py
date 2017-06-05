import os
import unittest
import urllib3
from generate_listings import generate_listings

file_path = "../html/js/listings.js"

class TestCase(unittest.TestCase):
    # case: if file is present under path
    def test_file_exist(self):
        generate_listings()
        is_exist = os.path.exists(file_path)
        self.assertTrue(is_exist)


if __name__ == '__main__':
    unittest.main()