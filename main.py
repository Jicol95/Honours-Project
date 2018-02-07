from Score import Score
from Analyse import Analyse
from Menu import Menu
import argparse
from music21 import stream


def Main():
    parsed_score = Score('bwv0254')
    pattern_engine = Analyse()
    # parsed_score.voice_notes[0].show()
    # Speghet codez should really be in a class somewhere
    sequence_len, pattern_index = pattern_engine.find_sequence(parsed_score, '+0+0')
    stre = (parsed_score.voice_notes[0][pattern_index[0]:pattern_index[0] + sequence_len + 1])
    stre.show()


if __name__ == '__main__':
    Main()
