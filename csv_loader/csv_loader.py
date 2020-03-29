from csv_loader.use_cases import create_feature

def create_geometries_from_csv(csvreader):
    for row in csvreader:
        feature = create_feature(row)
        # create geojson 
        # insert objects into mysql spatial
        return False