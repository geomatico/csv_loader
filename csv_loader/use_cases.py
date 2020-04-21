import os
import json
from datetime import date
from csv_loader.entity import Foundation, Road

def create_feature(row):
    _index_name = 0
    object_info = row.pop(_index_name)
    type, windfarm, name = object_info.split('/')
    if len(row) % 2 != 0:
        raise(Exception('Unpair number of coordinates, impossible to generate a geometry'))
    coords = list(map(lambda coord: float(coord), row))
    if type == 'F':
        stuff = Foundation(name, windfarm, coords)
    elif type == 'R':
        stuff = Road(name, windfarm, coords)

    return stuff

def save_as_geojson(features, type, path=None):

    feature_collection = {
        "type": "FeatureCollection",
        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::4326" } },
        "features": []
    }

    for feature in features:
        feature_collection['features'].append(feature.to_geojson())

    today = date.today()
    name = '{type}_{day}.geojson'.format(type=type, day=today)

    if path:
        filepath = os.path.join(path, name)
    else:
        import tempfile
        filepath = os.path.join(tempfile.mkdtemp(), name)

    print('Saving geojson in {}'.format(filepath))
    with open(filepath, 'w') as geojson:
        json.dump(feature_collection, geojson)