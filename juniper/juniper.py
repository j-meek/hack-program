#!/usr/bin/env python

"""
A function to determine Juniperus species based on location
"""

import numpy as np


def species(arg):
    """
    returns a species of juniper
    """

    if arg == "west":
        print("Juniperus osteosperma")

    elif arg == "east":
        print("Juniperus virginiana")


def where(coord):
    """
    creates DataFrame and returns region based on longitude
    """

    if coord in np.arange(-124, -101):
        print("west")

    elif coord in np.arange(-101, -66):
        print("east")

    elif coord in np.arange(25, 41):
        print("south")

    elif coord in np.arange(41, 49):
        print("north")


if __name__ == "__main__":
    species('east')
    species('west')
    where(42)
