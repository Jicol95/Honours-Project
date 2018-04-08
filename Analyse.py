from music21 import clef, stream, humdrum, note, editorial, metadata
from suffix_trees import STree
from Score import Score


class Analyse:

    def __init__(self, export, parsed_score):
        self.viewers = export
        self.score = parsed_score

    def score_refresh(self, score):
        self.score = score

    # Returns the indexs of the begining of all substring instances
    def find_sequence(self, sub_string):
        listindex = []
        # For the length of the main string
        for i in range(0, len(self.score.contour_abstract)):
            # Convert self.score.contour_abstract to string from list
            string = ''.join(self.score.contour_abstract[i])
            # Declare listindex_tmp list which will hold the indexes
            listindex_tmp = []
            # Pattern length
            pattern_length = len(sub_string)+1
            # If the pattern is found return the index
            j = string.find(sub_string)
            # While find is finding substrings
            while j >= 0:
                # If there are no matches yet then there is no need for check
                # or If the pattern found overlaps with the last pattern
                if (not(listindex_tmp)) or (j > listindex_tmp[-1][1]):
                    # append the start index of the substring to listindex_tmp
                    listindex_tmp.append((j, j + pattern_length))
                # If the pattern found overlaps with the last pattern
                elif j < listindex_tmp[-1][1]:
                    # Extend the last tuple upper bound to the upper bound of
                    # the new match
                    listindex_tmp[-1] = list(listindex_tmp[-1])
                    listindex_tmp[-1][1] = j + pattern_length
                    listindex_tmp[-1] = tuple(listindex_tmp[-1])
                else:
                    # No special case just add the sequence lower and upper bound
                    listindex_tmp.append((j, j + pattern_length + 1))
                # Look for the same substring but this time only search substrings
                # after the index of the last match
                j = string.find(sub_string, j + 1)
            listindex.append(listindex_tmp)
        # Return the length of the search sequence and the list of sub_string
        # positions
        return len(sub_string), listindex

    # Print the found sequences in the music
    def Search_Score(self, filename, sequence):
        # Get the series of notes
        voice_notes = self.score.voice_notes
        # Get the start indexs of the matching substrings in the sequence
        seq_len, match_index = self.find_sequence(sequence)
        # Get a copy of the score
        match_composition = self.score.parsed_score
        # Edit the title of the score to indicate the sequence
        match_composition.metadata.title = match_composition.metadata.title + ': ' + sequence
        # For each match
        for i in range(0, len(match_index)):
            keep_note_index = []
            for boundary in match_index[i]:
                keep_note_index += list(range(boundary[0], boundary[1]))
            for elem in voice_notes[i]:
                if voice_notes[i].index(elem) not in keep_note_index:
                    r = note.SpacerRest(type=elem.duration.type)
                    loc = voice_notes[i].index(elem)
                    match_composition.parts[i].flat.replace(elem, r)
        if len(self.viewers) == 2:
            match_composition.write('lily.pdf', fp = 'Results/' + self.score.name + '_' + sequence)
            match_composition.show()
        elif self.viewers[0] == "MuseScore":
            match_composition.show()
        elif self.viewers[0] == "LillyPond":
            match_composition.write('lily.pdf', fp = 'Results/' + self.score.name + '_' + sequence)


    def common_patterns(self, sequences):

        list_of_sequences = []
        # Just a bit of house keeping, the scores are in the form of lists but
        # I need them as strings in only this function. Hence the "hack-ish" code
        for sequence in sequences:
            voice = "".join(sequence)
            list_of_sequences.append(voice)

        # To be as fast as possible we window search the smallest string
        list_of_sequences = sorted(list_of_sequences, key=len)
        # Construct the genralised suffix tree
        suffix_tree = STree.STree(list_of_sequences)
        # List of common sequences
        matches = []
        # search window size
        window_size = len(suffix_tree.lcs())
        # Lower bound of the search window
        window_lower = 0
        # Upper bound of the search window
        window_upper = window_lower + window_size
        # If window size is 0 then suffix_tree.lcs() returned ""
        if window_size == 0:
            print('no match')
        elif suffix_tree.lcs() == list_of_sequences[0]:
            matches.append(suffix_tree.lcs())
            return matches
        # If there was a match then append it
        else:
            matches.append(suffix_tree.lcs())
        # Do this until the window size is 0
        while window_size != 0:
            # Create a copy of the sequence list
            list_of_sequences_copy = list_of_sequences[:]
            # Redefine the first element of the copy to only the elements in the window
            list_of_sequences_copy[0] = list_of_sequences[0][window_lower:window_upper]
            # Rebuild the suffix tree
            suffix_tree = STree.STree(list_of_sequences_copy)
            # If an unseen match is found and is not empty then append it
            if not suffix_tree.lcs() in matches and suffix_tree.lcs() != "" and len(suffix_tree.lcs())>= 5:
                matches.append(suffix_tree.lcs())
            # shift the window one to the right
            window_lower += 1
            window_upper += 1
            # Once the upper bound of the window touches the end or the string
            if window_upper == len(list_of_sequences[0]) - 1:
                # Decrease the window size by one
                window_size -= 1
                # Reset the window back to the start
                window_lower = 0
                window_upper = window_lower + window_size
        return matches
