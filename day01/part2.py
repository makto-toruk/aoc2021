from __future__ import annotations

import argparse
import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input: str) -> int:
    xs = [int(i) for i in input.splitlines()]

    n = 0
    for i in range(len(xs) - 3):
        if sum(xs[i + 1 : i + 4]) > sum(xs[i : i + 3]):
            n += 1

    return n


INPUT_S = """\
199
200
208
210
200
207
240
269
260
263
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
