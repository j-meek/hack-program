#!/usr/bin/env python

"""
A function to determine Juniperus species based on location
"""


def species(arg):
    """
    returns a species of juniper
    """

    if arg == "west":
        print("Juniperus osteosperma")

    elif arg == "east":
        print("Juniperus virginiana")


if __name__ == "__main__":
    species('east')
    species('west')
