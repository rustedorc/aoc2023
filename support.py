from __future__ import annotations

from typing import Generator
from enum import Enum

def parse_numbers_split(s: str) -> list[int]:
    return [int(x) for x in s.split()]

def parse_numbers_comma(s: str) -> list[int]:
    return [int(x) for x in s.strip().split(',')]

def parse_point_comma(s: str) -> tuple[int, int]:
    a_s, b_s = s.split(',')
    return int(a_s), int(b_s)

def parse_coords_int(s: str) -> dict[tuple[int, int], int]:
    coords = {}
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            coords[(x, y)] = int(c)
    return coords

def parse_coords_hash(s: str) -> set[tuple[int, int]]:
    coords = set()
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                coords.add((x, y))
    return coords

def adjacent_4(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y

def adjacent_8(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    for y_d in (-1, 0, 1):
        for x_d in (-1, 0, 1):
            if y_d == x_d == 0:
                continue
            yield x + x_d, y + y_d

class Direction(Enum):
    NORTH = (1, 0)
    SOUTH = (-1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

    @staticmethod
    def rotateRight(d: Direction) -> Direction:
        if d == Direction.NORTH:
            return Direction.EAST
        elif d == Direction.EAST:
            return Direction.SOUTH
        elif d == Direction.SOUTH:
            return Direction.WEST
        elif d == Direction.WEST:
            return Direction.NORTH
        else:
            raise Exception("Something broke bozo")
        
    @staticmethod
    def rotateLight(d: Direction) -> Direction:
        if d == Direction.NORTH:
            return Direction.WEST
        elif d == Direction.WEST:
            return Direction.SOUTH
        elif d == Direction.SOUTH:
            return Direction.EAST
        elif d == Direction.EAST:
            return Direction.NORTH
        else:
            raise Exception("Something broke bozo")
