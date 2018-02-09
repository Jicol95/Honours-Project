from Score import Score
from Analyse import Analyse
import argparse
from music21 import stream


def Main():
    pattern_engine = Analyse()
    pattern_engine.Search_Score('bwv0254', '+0+0')


if __name__ == '__main__':
    Main()
