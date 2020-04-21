import unittest
import os
from csv_loader.csv_loader import create_geometries_from_csv

class TestCSVLoader(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_load_csv(self):
        csv_path = os.path.join('tests/data', 'test.csv')
        geojson_path = 'tests/data'
        create_geometries_from_csv(csv_path, geojson_path)
        

