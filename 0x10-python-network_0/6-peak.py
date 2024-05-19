#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int: A peak element in the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    mid = n // 2
    mid_val = list_of_integers[mid]

    if (mid == 0 or mid_val >= list_of_integers[mid - 1]) and (mid == n - 1 or
       mid_val >= list_of_integers[mid + 1]):
        return mid_val
    elif mid > 0 and list_of_integers[mid - 1] > mid_val:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
