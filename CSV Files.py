
# CSV Files - YouTube Examples

# instead of manually writing and reading, use : csv.writer and csv.reader
# csv.DictWriter and csv.Dictreader help you with named data
# the csv module also takes care of formatting edge cases, like commas in your string

"""    Explanation from YouTube    """

"""
    Example 1:

    This is the first version, which a newbie would probably write
    to save and open files in CSV. This is OKay, but it less flexible,
    as both functions are completed tied up to the "keys" in our dictionary,
    so, if one day the dictionary's key changes, these functions won't work
    properly as they should work.

    There is why we should use the built-in function CSV. Examples 2 and 3 will
    cover the usage of it.
"""
import csv

movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Green Book", "director": "Farrelly"},
    {"name": "Amadeus", "director": "Forman"}
]


def write_to_file(output):
     with open("youtube_way_file_1.csv", "w") as f:
        f.write("name,director\n")
        for line in output:
            f.write(f'{line["name"]},{line["director"]}\n')


def read_from_file():
    with open("youtube_way_file_1.csv", "r") as f:
        content = f.readlines()
        for line in content[1:]:
            columns = line.strip().split(",")
            print(f'Name: {columns[0]}\tDirector: {columns[1]}')


write_to_file(movies)
read_from_file()

"""
    Example 2:

    On this second version, using CSV built-in function, it creates lists of lists of our 
    elements and write each of the list in lines. However, as we need to manually write the
    headers as we are using a list of dictionaries, this version is not the perfect, as if 
    the headers changes in future, we will have to change the function as well.

    But this version is good for everything except dictionaries, in other words, when we do
    not need headers, like in a dictionary.

    The reading part also suffers from header's problems, as we cannot rely on the write mode
    to take care of the headers of our elements, the read mode also will not take care for 
    headers. In other words, both don't recognize headers, therefore we need to manually 
    introduce them when writing, and when reading, we will see them being printed out, and
    they shouldn't.

    So, the best version to work on CSV files from and to a dictionary, is the version 3, which
    is exclusively for dictionaries, everything else should be done by version 2.

"""

# import csv
#
# movies2 = [
#     {"name": "The Matrix", "director": "Wachowski"},
#     {"name": "Green Book", "director": "Farrelly"},
#     {"name": "Amadeus", "director": "Forman"}
# ]
#
#
# def write_to_file_2(output):
#     with open("youtube_way_file_2.csv", "w") as f:
#         writer = csv.writer(f)
#         f.write("name,director\n")  # Unfortunately, we need to manually write the headers
#         writer.writerows([elem.values() for elem in output])  # This creates lists of lists
#
#
# def read_from_file2():
#     with open("youtube_way_file_2.csv", "r") as f:
#         reader = csv.reader(f)
#         for line in reader:
#             print(f'Name: {line[0]}\tDirector: {line[1]}')
#
#
# write_to_file_2(movies2)
# read_from_file2()

"""
    Example 3:

    On this third version, which is exclusively done for working with dictionaries, we now can get the headers (keys)
    from the dictionary in both ways, manually or automatically when writing to a CSV file using the CSV bui;t-in
    function for dictionaries.

    However, reading from CSV to a dictionary, it seems that we still have to MANUALLY describe the HEADERS. I have 
    queried a automatic way to do that on the course Q&A. Hope we have a way such as the writing mode. 

"""

import csv

movies3 = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Green Book", "director": "Farrelly"},
    {"name": "Amadeus", "director": "Forman"}
]


def write_to_file_from_dict(output):
    with open("youtube_way_file_3.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=list(output[0].keys()))  # fieldnames=["name", "director"])
        writer.writeheader()
        writer.writerows(output)


def read_from_file_to_dict():
    with open("youtube_way_file_3.csv", "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


write_to_file_from_dict(movies3)
# read_from_file_to_dict()

list_from_reader = read_from_file_to_dict()
print(list_from_reader)
