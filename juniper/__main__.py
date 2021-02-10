#!/usr/bin/env python

"""
Command line interface to juniper
"""

import argparse
from juniper import species


def parse_command_line():
    "parses args for the juniper funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--east",
        help="returns species name for eastern U.S.",
        action="store_true")

    # add long args
    parser.add_argument(
        "--west",
        help="returns species name for western U.S.",
        action="store_true")

    # parse args
    args = parser.parse_args()

    # check that user only entered one action arg
    if sum([args.east, args.west]) > 1:
        raise SystemExit(
            "only one of 'east' or 'west' at a time.")
    return args


def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()

    # pass argument to call darwinday function
    if args.east:
        species('east')
    elif args.west:
        species('west')


if __name__ == "__main__":
    species('east')
