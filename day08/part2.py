from __future__ import annotations

import argparse
import os

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


DECODER = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def to_string(s):

    return "".join(s)


def decode(s, encoder):

    decoder = {v: k for k, v in encoder.items()}
    t = set([decoder[c] for c in s])

    for k, v in DECODER.items():
        if set(k) == t:
            return str(v)

    print(f"no decoder for {s}:{t} with ")


def compute(input: str) -> int:

    xs = input.splitlines()

    n = 0
    for x in xs:
        ls, rs = [y.split() for y in x.split("|")]
        a1 = ""
        a7 = ""
        a4 = ""
        a8 = ""
        a235 = []
        a069 = []
        for l in ls:
            if len(l) == 2:
                a1 = set(l)
            elif len(l) == 3:
                a7 = set(l)
            elif len(l) == 4:
                a4 = set(l)
            elif len(l) == 7:
                a8 = set(l)
            elif len(l) == 5:
                a235.append(set(l))
            elif len(l) == 6:
                a069.append(set(l))

        encoder = {}

        t = [(a & a1) for a in a069]
        encoder["f"] = to_string(t[0] & t[1] & t[2])
        encoder["c"] = to_string(a1 - {encoder["f"]})

        t = [(a & a7) for a in a069]
        encoder["a"] = to_string(a7 - {encoder["f"], encoder["c"]})

        t = [(a & a4) for a in a069]
        encoder["b"] = to_string((t[0] & t[1] & t[2]) - {encoder["f"]})
        encoder["d"] = to_string(a4 - a7 - {encoder["b"]})

        t = a235
        encoder["g"] = to_string(
            (t[0] & t[1] & t[2]) - {encoder["a"], encoder["d"]}
        )
        encoder["e"] = to_string(a8 - set([e for e in encoder.values()]))

        s = ""
        for r in rs:
            s += decode(r, encoder)

        n += int(s)

    return n


INPUT_S = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""
EXPECTED = 61229


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
