from __future__ import annotations

import argparse
import os

import numpy as np
import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def is_low_point(i, j, X):

    imax, jmax = X.shape
    adjacent = []
    if i > 0:
        adjacent.append(X[i - 1, j])
    if i < imax - 1:
        adjacent.append(X[i + 1, j])
    if j > 0:
        adjacent.append(X[i, j - 1])
    if j < jmax - 1:
        adjacent.append(X[i, j + 1])

    if X[i, j] < min(adjacent):
        return True
    else:
        return False


def compute(input: str) -> int:

    xs = input.splitlines()

    X = []
    for x in xs:
        X.append([int(y) for y in x])

    X = np.array(X)
    imax, jmax = X.shape

    n = 0
    for i in range(imax):
        for j in range(jmax):
            if is_low_point(i, j, X):
                n += 1 + X[i, j]

    return n


INPUT_S = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""
EXPECTED = 15


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
