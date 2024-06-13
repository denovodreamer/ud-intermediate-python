"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json

from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    with open(filename, 'w') as csvfile:

        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(fieldnames)

        for ca in results:
            data = [
                datetime_to_str(ca.time),
                ca.distance,
                ca.velocity,
                ca._designation,
                ca.neo.name,
                ca.neo.diameter,
                ca.neo.hazardous
            ]

            csv_writer.writerow(data)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    with open(filename) as json_file:

        data = []

        for ca in results:
            ca_data = {
                "datetime_utc": datetime_to_str(ca.time),
                "distance_au": ca.distance,
                "velocity_km_s": ca.velocity,
                "neo": {
                    "designation": ca.neo.designation,
                    "name": ca.neo.name,
                    "diameter_km": ca.neo.diameter,
                    "potentially_hazardous": ca.neo.hazardous
                }
            }
            data.append(ca_data)

        json.dump(data, json_file)

