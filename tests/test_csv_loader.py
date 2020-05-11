import unittest
import os
from csv_loader.csv_loader import create_geometries_from_csv, create_centroids_from_csv

class TestCSVLoader(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_load_csv(self):
        csv_path = os.path.join('tests/data', 'test.csv')
        geojson_path = 'tests/data'
        create_geometries_from_csv(csv_path, geojson_path)

    def test_centroids_csv(self):
        csv_path = os.path.join('tests/data', 'test_centroids.csv')
        geojson_path = 'tests/data'
        create_centroids_from_csv(csv_path, geojson_path)    
        
    def test_centroids_shorter_csv(self):
        csv_path = os.path.join('tests/data', 'test_centroids_shorter.csv')
        geojson_path = 'tests/data'
        create_centroids_from_csv(csv_path, geojson_path)
        

