from Score import Score
from Analyse import Analyse
import argparse
from music21 import stream


def Main():
    score = Score('bwv0256')
    pattern_engine = Analyse()

    # Demo of known sequence search
    # pattern_engine.Search_Score('bwv0260', '---')

    # # Demo of blind sequence search of one song
    pattern_engine.common_patterns(score.contour_abstract)

if __name__ == '__main__':
    Main()
