# CSV Loader

## CLI

Typing `python create_winfarm.py --help`

```bash
CREATE WINDFARM CLI

Usage:
    create_windfarm.py CSV [--geojson_path=<geojson_path>] [--centroids]
    create_windfarm.py -h | --help
    create_windfarm.py -v | --version

Options:
    CSV                                 The CSV.
    --geojson_path=<geojson_path>       Path where the geojson will be saved (/tmp/<dir>).
    --version                           Show version.
    -h --help                           Show this screen.
```

To create centroids:

```bash
python create_winfarm.py /home/michogarcia/geomati.co/GAMESA/data/CSVs/agua_clara_procesado.csv --centroids
```