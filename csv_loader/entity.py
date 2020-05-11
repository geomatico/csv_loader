import pyproj
import math
from typing import List
from shapely.geometry import Point, LineString, mapping
from shapely.ops import transform as shapely_transform

class Foundation(object):

    _x = 0
    _y = 1

    def __init__(self, name, windfarm, coords):
        self._location = Point(coords[self._x], coords[self._y])
        self._name = name
        self._windfarm = windfarm

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def windfarm(self):
        return self._windfarm

    @windfarm.setter
    def windfarm(self, windfarm):
        self._windfarm = windfarm

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, coords):
        self._location = Point(coords[self._x], coords[self._y])

    def to_geojson(self):
        return {
            "type": "Feature",
            "geometry": mapping(self._location),
            "properties": {
                "name": self._name,
                "windfarm": self._windfarm
            }
        }

class Centroid(object):

    def __init__(self, point):
        self._location = point

    @property
    def location(self):
        return self._location

    def to_geojson(self):
        return {
            "type": "Feature",
            "geometry": mapping(self._location),
            "properties": {}
        }


class Road(object):

    def __init__(self, name, windfarm, coords):
        self._path = LineString(list(zip(coords[0::2], coords[1::2])))
        self._name = name
        self._windfarm = windfarm

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name    
        
    @property
    def windfarm(self):
        return self._windfarm

    @windfarm.setter
    def windfarm(self, windfarm):
        self._windfarm = windfarm

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, coords):
        self._path = LineString(list(zip(coords[0::2], coords[1::2])))


    def to_geojson(self):
        return {
            "type": "Feature",
            "geometry": mapping(self._path),
            "properties": {
                "name": self._name,
                "windfarm": self._windfarm
            }
        }

    def centroids(self, size: int=300) -> List[Point]:
        """
        It generates the Centroids of a LineString. It walks the LineString generating centroids every buffer distance
        passed as parameter until the envelope of the buffer does not intersects twice with the road. This avoids 
        getting envelopes where road finishing inside.

        Parameters:
            size (int): the desired size of the image. 300m as default

        Returns:
            MultiPoint: MultiPoint generated with all centroids in EPSG:4326
        """
        _first = 0
        centroids = []
        wgs84_to_mercator = pyproj.Transformer.from_crs('EPSG:4326', 'EPSG:3857', always_xy=True)
        mercator_to_wgs84 = pyproj.Transformer.from_crs('EPSG:3857', 'EPSG:4326', always_xy=True)
        road_3857 = shapely_transform(wgs84_to_mercator.transform, self.path)
        size_3857 = size / math.cos(math.pi * self.path.centroid.y / 180)
        distance_3857 = size_3857 / 2
        max_distance_3857 = road_3857.length - distance_3857

        if size_3857 > road_3857.length:
            centroids.append(Centroid(shapely_transform(mercator_to_wgs84.transform, road_3857.centroid)))

        while distance_3857 <= max_distance_3857:
            centroid_3857 = road_3857.interpolate(distance_3857)
            centroids.append(Centroid(shapely_transform(mercator_to_wgs84.transform, centroid_3857)))
            distance_3857 += size_3857

        return centroids
