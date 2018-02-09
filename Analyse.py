from music21 import stream, metadata
from Score import Score


class Analyse:

    def __init__(self):
        pass

    def find_sequence(self, parsed_score, sub_string):
        for i in range(0, len(parsed_score.contour_abstract)):
            string = ''.join(parsed_score.contour_abstract[i])
            listindex = []
            offset = 0
            i = string.find(sub_string, offset)
            while i >= 0:
                listindex.append(i)
                i = string.find(sub_string, i + 1)
            return len(sub_string), listindex

    def Search_Score(self, filename, sequence):
        parsed_score = Score(filename)
        pattern_engine = Analyse()
        voice_notes = parsed_score.voice_notes
        seq_len, match_index = pattern_engine.find_sequence(parsed_score, sequence)
        print(match_index)
        for i in range(0, len(match_index)):
            pattern = voice_notes[0][match_index[i]: match_index[i] + seq_len + 1]
            pattern.insert(0, metadata.Metadata())
            pattern.metadata.title = 'Sequence Match'
            pattern.metadata.composer = 'Github: https://github.com/Jicol95'
            pattern.show('text')
