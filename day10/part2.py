from __future__ import annotations

import argparse
import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


CLOSERS = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


def compute(input: str) -> int:

    xs = input.splitlines()

    scores = []
    for ys in xs:
        t = []
        incorrect = False
        for y in ys:
            if y in CLOSERS.keys():  # openers
                t.append(y)
            else:
                if y == CLOSERS[t[-1]]:
                    t.pop()
                else:
                    incorrect = True
                    break

        if not incorrect:
            score = 0
            while t:
                score = 5 * score + POINTS[CLOSERS[t.pop()]]
            scores.append(score)

    return sorted(scores)[len(scores) // 2]


INPUT_S = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""
EXPECTED = 288957


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
