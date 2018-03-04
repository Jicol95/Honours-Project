from Score import Score
from Analyse import Analyse
import argparse
from music21 import stream


def Main():
    pattern_engine = Analyse()
    # pattern_engine.Search_Score('bwv0260', '---')
    pattern_engine.common_patterns(["+++0000+-+-0","+-+0+++0-+-00000","+-+-+00+++-0-0000"])

if __name__ == '__main__':
    Main()
