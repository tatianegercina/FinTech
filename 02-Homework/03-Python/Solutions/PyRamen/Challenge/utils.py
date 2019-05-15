# -*- coding: UTF-8 -*-
"""PyRamen Utility Functions."""


def sum_field(report, field):
    """
    Summarize a column of data.

    Args:
        report (dict): The report dictionary.
        field (str): The column to perform the operation on.

    Returns:
        A sum total for the requested field (column) in the report.
    """

    total = 0
    for key in report:
        total += report[key][field]

    return total


def avg_field(report, field):
    """
    Average a column of data.

    Args:
        report (dict): The report dictionary.
        field (str): The column to perform the operation on.

    Returns:
        A calculated average for the requested field (column) in the report.
    """

    total = 0
    for key in report:
        total += report[key][field]

    avg = round(total / len(report), 2)
    return avg


def min_field(report, field):
    """
    Find the minimum and associated key of a column of data.

    Args:
        report (dict): The report dictionary.
        field (str): The column looking to perform the operation on.

    Returns:
        The minimum for the requested field (column) in the report and the associated key.
    """

    minimum = None
    min_key = None

    for key in report:
        if not minimum:
            minimum = report[key][field]

        elif report[key][field] < minimum:
            minimum = report[key][field]
            min_key = key

    return minimum, min_key


def max_field(report, field):
    """
    Find the maximum and associated key of a column of data.

    Args:
        report (dict): The report dictionary.
        field (str): The column looking to perform the operation on.

    Returns:
        The maximum for the requested field (column) in the report and the associated key.
    """

    maximum = None
    max_key = None

    for key in report:
        if maximum is None:
            maximum = report[key][field]

        elif report[key][field] > maximum:
            maximum = report[key][field]
            max_key = key

    return maximum, max_key
