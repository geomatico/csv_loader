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