from music21 import stream


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
