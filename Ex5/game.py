import itertools
from typing import List


def combine(words: List[str]):
    """
    :param words: list of sub-sequences
    :return: shortest sequence containing all the sub-sequences

    """
    seq = words.pop()
    while len(words) > 0:
        wordBefore = words.pop()
        for i in range(len(wordBefore) + 1):
            # In order to give the possibility to find equality also in the sub-sequence within a word
            subLast = min(i + len(seq), len(wordBefore))
            if wordBefore[i:subLast] == seq[:subLast - i]:
                seq = wordBefore[:subLast] + seq[subLast - i:] + wordBefore[i + len(seq):]
                # wordBefore[i + len(seq):] for cases where a sub-sequence is in the middle of another sub-sequence
                break
    return seq


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
subsequences = [input() for i in range(n)]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(min(len(combine(list(p))) for p in itertools.permutations(subsequences)))
