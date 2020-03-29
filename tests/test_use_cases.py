import unittest
from csv_loader.use_cases import create_feature
from shapely.geometry import Point, LineString

class TestUseCases(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_create_feature(self):
        row = ['F/Fake WindFarm/AE01', '10', '10']
        foundation = create_feature(row)

        self.assertEqual(foundation.name, 'AE01')
        self.assertEqual(foundation.windfarm, 'Fake WindFarm')
        self.assertTrue(foundation.location.equals(Point(10, 10)))

        row = ['R/Fake WindFarm/EJE_O01.02', '100', '100', '200', '100', '200', '200', '300', '200', '300', '300', '400', '300']
        road = create_feature(row)

        self.assertEqual(road.name, 'EJE_O01.02')
        self.assertEqual(road.windfarm, 'Fake WindFarm')
        self.assertTrue(road.path.equals(LineString([(100, 100), (200, 100), (200, 200), (300, 200), (300, 300), (400, 300)])))

        row = ['R/Fake WindFarm/EJE_O01.02', '100', '100', '200', '100', '200', '200', '300', '200', '300', '300', '400']

        is_raised = False
        try:
            create_feature(row)
        except:
            is_raised = True
        
        self.assertTrue(is_raised)
