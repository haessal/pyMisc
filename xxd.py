#!/usr/bin/env python3

"""xxd.py is a hexdump utility."""

import sys
import argparse


def getargs():
    """Parse command line and get arguments."""
    parser = argparse.ArgumentParser(description="a hexdump utility")

    if sys.stdin.isatty():
        parser.add_argument("infile", help="Input file")

    args = parser.parse_args()
    return(args)


def cmd_xxd(args, f):
    """Execute main routine."""
    line = f.read(16)
    for b in line:
        print("{0:x}".format(b), end=" ")
    print("")


def main():
    """Provide entry point."""
    args = getargs()

    if hasattr(args, "infile"):
        with open(args.infile, 'rb') as f:
            cmd_xxd(args, f)
    else:
        cmd_xxd(args, sys.stdin.buffer)

    sys.exit(0)


if __name__ == '__main__':
    main()
