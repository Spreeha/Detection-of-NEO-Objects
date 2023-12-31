"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    

    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        neos = []
        for row in reader:
            row['pha'] = False if row["pha"] in ["", "N"] else True
            try:
                neo = NearEarthObject(
                    designation = row.get('pdes'),
                    name = row.get('name', None),
                    diameter = row.get('diameter',float('nan')),
                    hazardous = row['pha'],
                )
            except Exception as e:
                print(e)
            else:
                neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to  a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    
    
    with open(cad_json_path, 'r') as infile:
        reader = json.load(infile)
        reader = [dict(zip(reader["fields"], data)) for data in reader["data"]]
        cad_approaches = []
        for row in reader:
            try:
                cad_approach = CloseApproach(
                    designation = row.get('des'),
                    time = row.get('cd'),
                    distance = row.get('dist',0.0),
                    velocity = row.get('v_rel',0.0),
                )
            except Exception as e:
                print(e)
            else:
                cad_approaches.append(cad_approach) 
    return cad_approaches
