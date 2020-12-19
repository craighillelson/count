"""
Import csv containing one column. The script will count occurences and output
a dictionary structured in the following way.
key: element
value: number of occurances
"""

from collections import (Counter,
                         namedtuple)
import csv
import re
import pyinputplus as pyip


def populate_list():
    """
    Open a one column csv and populate a list with the contents of the csv.
    """

    with open("filename.csv") as csv_file:
        lst = []
        f_csv = csv.reader(csv_file)
        headers = [re.sub('[^a-zA-Z_]', '_', header) for header in next(f_csv)]
        assembled_tuple = namedtuple('assembled_tuple', headers)
        for app_name in f_csv:
            row = assembled_tuple(*app_name)
            lst.append(row[0])

    return lst


def build_dct_of_counts():
    """
    Using Counter from Python's standard library, populate a dictionary
    structured in the following way.
    key: item
    value: number of occurances of item
    """

    dct = {}
    for element in elements:
        dct.setdefault(element, 0)
        dct[element] = dct[element] + 1

    return dct


def prompt_user_for_num_results():
    """Prompt user to specify the number of results they'd like to see."""

    return pyip.inputInt("\nHow many results would you like to see?\n> ")


def output_results():
    """
    Prompt user for the number of results they'd like to see. Output that
    number of results sorted in descending order by count.
    """

    element_count = Counter(elements_counts)
    element_count.most_common()
    dct = {}
    print("\nelement, count")
    for num, (element, element_count) in enumerate(element_count.most_common(num_results), 1):
        print(f"{num}. {element}, {element_count}")
        dct[element] = element_count
    return dct


def write_dct_to_csv(filename):
    """Write dictionary to csv."""

    with open(filename, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["element","count"])
        for element, count in element_count_to_export.items():
            keys_values = (element, count)
            out_csv.writerow(keys_values)

    print(f'\n"{filename}" exported successfully\n')


elements = populate_list()
elements_counts = build_dct_of_counts()
num_results = prompt_user_for_num_results()
element_count_to_export = output_results()
write_dct_to_csv("report.csv")
