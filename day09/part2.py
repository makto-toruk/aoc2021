from __future__ import annotations

import argparse
import math
import os

import numpy as np
import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def get_adjacent(i, j, X):

    imax, jmax = X.shape
    adjacent = []
    if i > 0:
        adjacent.append((i - 1, j))
    if i < imax - 1:
        adjacent.append((i + 1, j))
    if j > 0:
        adjacent.append((i, j - 1))
    if j < jmax - 1:
        adjacent.append((i, j + 1))

    return adjacent


def is_low_point(i, j, X):

    adjacent = get_adjacent(i, j, X)
    if X[i, j] < min([X[a] for a in adjacent]):
        return True
    else:
        return False


def get_low_points(i, j, X):

    if is_low_point(i, j, X):
        return [(i, j)]
    else:
        adjacent = get_adjacent(i, j, X)
        ls = []
        for p, q in adjacent:
            if X[p, q] < X[i, j] and X[p, q] != 9:
                ls += get_low_points(p, q, X)

        return ls


def compute(input: str) -> int:

    xs = input.splitlines()

    X = []
    for x in xs:
        X.append([int(y) for y in x])

    X = np.array(X)
    imax, jmax = X.shape

    low_points = []
    for i in range(imax):
        for j in range(jmax):
            if is_low_point(i, j, X):
                low_points.append((i, j))

    basins = {p: [] for p in low_points}
    for i in range(imax):
        for j in range(jmax):
            if X[i, j] != 9:
                l = get_low_points(i, j, X)
                if len(set(l)) == 1:
                    basins[l[0]].append((i, j))

    basin_sizes = [len(v) for v in basins.values()]

    return math.prod(sorted(basin_sizes)[-3:])


INPUT_S = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""
EXPECTED = 1134


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int | None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.input) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
