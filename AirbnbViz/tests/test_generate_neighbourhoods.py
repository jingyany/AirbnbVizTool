import os
import unittest
import urllib3
from generate_neighbourhoods import generate_neighbourhoods

file_path1 = "../html/js/ranked_price.js"
file_path2 = "../html/js/ranked_rating.js"
file_path3 = "../html/js/neighbourhoods.json"
file_path4 = "../html/js/neighbourhoods.js"

class TestCase(unittest.TestCase):
    # case: if file1 is present under path
    def test_file_exist(self):
        generate_neighbourhoods()
        is_exist = os.path.exists(file_path1)
        self.assertTrue(is_exist)

    # case: if file2 is present under path
    def test_file_exist(self):
        generate_neighbourhoods()
        is_exist = os.path.exists(file_path2)
        self.assertTrue(is_exist)

	# case: if file3 is present under path
    def test_file_exist(self):
        generate_neighbourhoods()
        is_exist = os.path.exists(file_path3)
        self.assertTrue(is_exist)

    # case: if file3 is present under path
    def test_file_exist(self):
        generate_neighbourhoods()
        is_exist = os.path.exists(file_path4)
        self.assertTrue(is_exist)


if __name__ == '__main__':
    unittest.main()