from music21 import stream, metadata
from Score import Score


class Analyse:

    def __init__(self):
        pass

    # Returns the indexs of the begining of all substring instances
    def find_sequence(self, parsed_score, sub_string):
        # For the length of the main string
        for i in range(0, len(parsed_score.contour_abstract)):
            # Convert parsed_score.contour_abstract to string from list
            string = ''.join(parsed_score.contour_abstract[i])
            # Declare listindex list which will hold the indexes
            listindex = []
            i = string.find(sub_string)
            # While find is finding substrings
            while i >= 0:
                # append the start index of the substring to listindex
                listindex.append(i)
                # Use find again offset with 1 + the index of last substring start
                i = string.find(sub_string, i + 1)
            # Return the length of the search sequence and the list of sub_string
            # positions
            return len(sub_string), listindex

    # Print the found sequences in the music
    def Search_Score(self, filename, sequence):
        # Create an instance of the score
        parsed_score = Score(filename)
        # Create an instance of the analysis engine
        pattern_engine = Analyse()
        # Get the series of notes
        voice_notes = parsed_score.voice_notes
        # Get the start indexs of the matching substrings in the sequence
        seq_len, match_index = pattern_engine.find_sequence(parsed_score, sequence)
        # For each match
        for i in range(0, len(match_index)):
            # Show in a music viewer each pattern match on their own
            pattern = voice_notes[0][match_index[i]: match_index[i] + seq_len + 1]
            pattern.insert(0, metadata.Metadata())
            pattern.metadata.title = 'Sequence Match'
            pattern.metadata.composer = 'Github: https://github.com/Jicol95'
            pattern.show('text')
