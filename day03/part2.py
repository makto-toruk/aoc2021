from __future__ import annotations

import argparse
import os

import numpy as np
import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input: str) -> int:

    xs = input.splitlines()
    X = []
    for x in xs:
        X.append([int(i) for i in x])

    X = np.array(X)
    w = X.shape[1]

    XO2 = X
    l = XO2.shape[0]
    for i in range(w):
        if np.sum(XO2[:, i]) >= l / 2:
            loc = np.where(XO2[:, i] == 1)[0]
        else:
            loc = np.where(XO2[:, i] == 0)[0]
        XO2 = XO2[loc, :]
        l = XO2.shape[0]
        if l == 1:
            XO2 = XO2[0][::-1]
            break

    XCO2 = X
    l = XCO2.shape[0]
    for i in range(w):
        if np.sum(XCO2[:, i]) >= l / 2:
            loc = np.where(XCO2[:, i] == 0)[0]
        else:
            loc = np.where(XCO2[:, i] == 1)[0]
        XCO2 = XCO2[loc, :]
        l = XCO2.shape[0]
        if l == 1:
            XCO2 = XCO2[0][::-1]
            break

    o2 = 0
    co2 = 0
    for i in range(len(XO2)):
        o2 += XO2[i] * (2 ** i)
        co2 += XCO2[i] * (2 ** i)

    return o2 * co2


INPUT_S = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
EXPECTED = 230


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
