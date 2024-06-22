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
    neos = []

    with open(neo_csv_path, "r", newline="") as neo_csv:
        neo_reader = csv.DictReader(neo_csv)

        for neo_info in neo_reader:
            neo = NearEarthObject(neo_info["pdes"], neo_info["name"], neo_info["diameter"], neo_info["pha"])
            neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    cas = []

    with open(cad_json_path, "r", newline="") as cad_json_file:
        cad_json = json.load(cad_json_file)

    ca_info = cad_json["fields"]

    for ca_data in cad_json["data"]:
        ca_info = dict(zip(ca_info, ca_data))
        ca = CloseApproach(ca_info["des"], ca_info["cd"], ca_info["dist"], ca_info["v_rel"])
        cas.append(ca)

    return cas
