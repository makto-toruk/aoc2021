from __future__ import annotations

import argparse
import os
import statistics

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input: str) -> int:

    xs = [int(i) for i in input.splitlines()[0].split(",")]

    m = statistics.median(xs)

    return int(sum([abs(x - m) for x in xs]))


INPUT_S = """\
16,1,2,0,4,2,7,1,2,14
"""
EXPECTED = 37


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
