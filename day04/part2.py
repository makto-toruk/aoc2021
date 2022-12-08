from __future__ import annotations

import argparse
import os

import numpy as np
import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def is_win(X):

    l = X.shape[0]

    for i in range(l):
        if X[i, :].sum() == l or X[:, i].sum() == l:
            return True

    return False


def compute(input: str) -> int:

    xs = input.splitlines()

    ns = [int(i) for i in xs[0].split(",")]

    bs = []
    strikes = []
    b = []
    for x in xs[2:]:
        if x:
            b.append([int(i) for i in x.split()])
        else:
            bs.append(np.array(b))
            b = []
    bs.append(np.array(b))

    for _ in range(len(bs)):
        strikes.append(np.zeros((5, 5)))

    has_won = [0] * len(bs)
    for n in ns:
        for i, (b, strike) in enumerate(zip(bs, strikes)):
            strike[np.where(b == n)] = 1
            if is_win(strike):
                has_won[i] = 1
                if sum(has_won) == len(bs):
                    return n * np.sum(b[np.where(strike == 0)])

    return 0


INPUT_S = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
EXPECTED = 1924


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
