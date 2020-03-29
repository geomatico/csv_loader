from typing import List
from shapely.geometry import Point, LineString

class Foundation(object):

    _x = 0
    _y = 1

    def __init__(self, name, coords):
        self._location = Point(coords[self._x], coords[self._y])
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, coords):
        self._location = Point(coords[self._x], coords[self._y])


class Road(object):

    def __init__(self, name, coords):
        self._path = LineString(list(zip(coords[0::2], coords[1::2])))
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, coords):
        self._path = LineString(list(zip(coords[0::2], coords[1::2])))