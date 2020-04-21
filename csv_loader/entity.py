from typing import List
from shapely.geometry import Point, LineString, mapping

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