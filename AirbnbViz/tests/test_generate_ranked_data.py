import os
import unittest
import urllib3
from generate_ranked_data import generate_ranked_data

file_path1 = "../html/js/ranked_rating_data_by_group.js"
file_path2 = "../html/js/ranked_price_data_by_group.js"


class TestCase(unittest.TestCase):
    # case: if file1 is present under path
    def test_file_exist(self):
        generate_ranked_data()
        is_exist = os.path.exists(file_path1)
        self.assertTrue(is_exist)

    # case: if file2 is present under path
    def test_file_exist(self):
        generate_ranked_data()
        is_exist = os.path.exists(file_path2)
        self.assertTrue(is_exist)


if __name__ == '__main__':
    unittest.main()