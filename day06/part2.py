from __future__ import annotations

import argparse
import os
from collections import Counter

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input: str) -> int:

    xs = input.splitlines()[0]
    timers = [int(i) for i in xs.split(",")]
    count = Counter(timers)
    for i in range(9):
        if i not in count:
            count[i] = 0
    new_count = count.copy()

    n_days = 256

    for _ in range(n_days):
        for k, v in count.items():
            if k != 0:
                new_count[k - 1] = v

        new_count[8] = 0
        if count[0] >= 1:
            new_count[6] += count[0]
            new_count[8] = count[0]

        count = new_count.copy()
    return sum(count.values())


INPUT_S = """\
3,4,3,1,2
"""
EXPECTED = 26984457539


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
