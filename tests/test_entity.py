import unittest

from csv_loader.entity import Foundation, Road
from shapely.geometry import Point, LineString

class TestEntity(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_foundation(self):
        coords = [99.99, 99.99]
        foundation = Foundation('fake_foundation', 'fake winfarm', coords)
        fake_point = Point(99.99, 99.99)
        self.assertTrue(foundation.location.equals(fake_point))

    def test_road(self):
        coords = [99.99, 99.99, 199.99, 199.99, 299.99, 299.99]
        road = Road('fake_road', 'fake winfarm', coords)
        fake_road = LineString([(99.99, 99.99), (199.99, 199.99), (299.99, 299.99)])
        self.assertTrue(road.path.equals(fake_road))
    
    def test_road_centroids(self):
        coords = [0, 0, 0.002, -0.003, 0.003, 0.002, 0.005, -0.003, 0.006, 0.002, 0.007, -0.003]
        road = Road('fake_road', 'fake winfarm', coords)
        centroids = road.centroids()
        
        self.assertEqual(len(centroids), 9)