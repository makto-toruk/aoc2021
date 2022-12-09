from __future__ import annotations

import argparse
import os
from collections import Counter

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def get_points(a, b):

    x1, y1 = a
    x2, y2 = b

    c = [a, b]
    if x1 == x2:
        for i in range(min(y1, y2) + 1, max(y1, y2)):
            c.append((x1, i))
    elif y1 == y2:
        for i in range(min(x1, x2) + 1, max(x1, x2)):
            c.append((i, y1))

    return c


def compute(input: str) -> int:

    xs = input.splitlines()

    coords = []
    for x in xs:
        l, r = x.split(" -> ")
        x1, y1 = [int(i) for i in l.split(",")]
        x2, y2 = [int(i) for i in r.split(",")]

        if x1 == x2 or y1 == y2:
            coords += get_points((x1, y1), (x2, y2))

    d = Counter(coords)

    return sum([True for i in d.values() if i >= 2])


INPUT_S = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
EXPECTED = 5


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
