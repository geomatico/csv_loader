"""CREATE WINDFARM CLI

Usage:
    create_windfarm.py CSV [--geojson_path=<geojson_path>]
    create_windfarm.py -h | --help
    create_windfarm.py -v | --version

Options:
    CSV                                 The CSV.
    --geojson_path=<geojson_path>       Path where the geojson will be saved (/tmp/<dir>).
    --version                           Show version.
    -h --help                           Show this screen.
"""
from docopt import docopt
from csv_loader.csv_loader import create_geometries_from_csv

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    if arguments['CSV']:
        create_geometries_from_csv(arguments['CSV'])
    elif arguments['CSV'] and arguments['--geojson_path']:
        create_geometries_from_csv(arguments['CSV'], arguments['--geojson_path'])