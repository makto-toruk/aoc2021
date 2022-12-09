from __future__ import annotations

import argparse
import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input: str) -> int:

    xs = input.splitlines()[0]
    timers = [int(i) for i in xs.split(",")]

    n_days = 80

    flags = [False] * len(timers)
    prev = 0
    for _ in range(n_days):
        curr = 0
        for i, (t, f) in enumerate(zip(timers, flags)):
            if f:
                timers[i] = 6
                flags[i] = False
            else:
                timers[i] = t - 1
                if (t - 1) == 0:
                    flags[i] = True
                    curr += 1
        timers += [8] * prev
        flags += [False] * prev
        prev = curr

    return len(timers)


INPUT_S = """\
3,4,3,1,2
"""
EXPECTED = 5934


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
