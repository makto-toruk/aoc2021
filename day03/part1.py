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
    l = X.shape[0]
    s = X.sum(axis=0)

    g = [1 if i > l // 2 else 0 for i in s]
    gamma = 0
    epislon = 0
    g.reverse()
    for i in range(len(g)):
        gamma += g[i] * (2 ** i)
        epislon += (1 - g[i]) * (2 ** i)

    return gamma * epislon


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
EXPECTED = 198


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
