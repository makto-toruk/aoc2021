from __future__ import annotations

import argparse
import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input: str) -> int:
    ins = [i.split(" ") for i in input.splitlines()]

    x, y = 0, 0
    for d, s in ins:
        s = int(s)
        if d.startswith("f"):
            x += s
        elif d.startswith("u"):
            y -= s
        elif d.startswith("d"):
            y += s

    return x * y


INPUT_S = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
EXPECTED = 150


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
