#!/usr/bin/env python
import fileinput


def main():
    input = [line.strip() for line in fileinput.input()]
    print input


if __name__ == '__main__':
    main()
