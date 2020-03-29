import unittest
import csv
import os

from csv_loader.use_cases import create_feature

CSV_FOLDER_PATH = 'tests/data'

class TestCSVLoader(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_load_csv(self):
        csv_name = 'test.csv'
        with open(os.path.join(CSV_FOLDER_PATH, csv_name)) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                feature = create_feature(row)
