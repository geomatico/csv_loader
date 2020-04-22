import csv
import os
import functools
import operator
from functools import reduce
from csv_loader.use_cases import create_feature, save_as_geojson
from csv_loader.entity import Foundation, Road

def create_geometries_from_csv(csv_path, geojson_path=None):
    features = []
    print('Creating geojson from {}'.format(csv_path))
    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        foundations = []
        roads = []
        for row in reader:
            feature = create_feature(row)
            if type(feature) is Foundation:
                foundations.append(feature)
            elif type(feature) is Road:
                roads.append(feature)
            
        save_as_geojson(roads, 'roads', geojson_path)
        save_as_geojson(foundations, 'foundations', geojson_path)

        return roads, foundations

def create_centroids_from_csv(csv_path, geojson_path=None):
    roads, foundations = create_geometries_from_csv(csv_path, geojson_path)
    centroids = functools.reduce(operator.iconcat, list(map(lambda road: road.centroids(), roads)), [])
    save_as_geojson(centroids, 'centroids', geojson_path)