from music21 import clef, stream, metadata, humdrum
from suffix_trees import STree
from Score import Score


class Analyse:

    def __init__(self):
        pass

    # Returns the indexs of the begining of all substring instances
    def find_sequence(self, parsed_score, sub_string):
        listindex = []
        # For the length of the main string
        for i in range(0, len(parsed_score.contour_abstract)):
            # Convert parsed_score.contour_abstract to string from list
            string = ''.join(parsed_score.contour_abstract[i])
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
                elif j <= listindex_tmp[-1][1]:
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
        # Create an instance of the score
        parsed_score = Score(filename)
        # Create an instance of the analysis engine
        pattern_engine = Analyse()
        # Get the series of notes
        voice_notes = parsed_score.voice_notes
        # Get the start indexs of the matching substrings in the sequence
        seq_len, match_index = pattern_engine.find_sequence(parsed_score, sequence)
        match_composition = parsed_score.parsed_score.template()
        # For each match
        for i in range(0, len(match_index)):
            for sequence_range in match_index[i]:
                match_range = voice_notes[i][sequence_range[0]:sequence_range[1]]
                range_start = voice_notes[i][sequence_range[0]].offset
                match_composition.parts[i].insert(range_start,match_range)
        match_composition.show()

    def common_patterns(self, list_of_scores):

        # Just a bit of house keeping, the scores are in the form of lists but
        # I need them as strings in only this function. Hence the "hack-ish" code
        for score in list_of_scores:
            score = str(score)
        # Order the list of scores by length of list
        list_of_scores = sorted(list_of_scores, key=len, reversed=True)
        # Unredacted version of list_of_scores
        master_list = list_of_scores
        # Construct the generalised suffix tree of list of scores
        st = STree.STree(list_of_scores)
        # This will contain our list of matches
        matches = []
        # This is where matches which are yet to be processed are stored
        queue = []

        # Continue to do this until there is no common strings
        while st.lcs() != "":
            # Find the longest common substring and it's start and end point
            longest_common_substring = st.lcs()
            lcs_start = master_list[0].find(longest_common_substring)
            lcs_end = lcs_start + len(longest_common_substring)

            # If we don't have a match in our queue
            if not queue:
                # If the longest common substring isnt in the list of matches then add it
                if not any([(longest_common_substring in match) for match in matches]):
                    matches.append(longest_common_substring)
                    lookback = list(longest_common_substring)

                    # Redact the matched pattern one byte at a time left to right
                    for i in range(lcs_start, lcs_end):
                        # Strings are imutable so we change the type for a moment
                        TEMP = list(list_of_scores[0])
                        # Redact with 'x'
                        TEMP[i] = 'x'
                        # Convert back to string
                        list_of_scores[0] = "".join(TEMP)
                        # Rebuild the suffix tree with new strings
                        st = STree.STree(list_of_scores)
                        # Add any new pattern to the queue
                        if (st.lcs() != longest_common_substring and
                            st.lcs() not in queue and
                            st.lcs not in matches):

                            queue.append(st.lcs())

                    # Remove the redaction one byte at a time left to right
                    for i in range(lcs_start, lcs_end):
                        # Strings are imutable so we change the type for a moment
                        TEMP = list(list_of_scores[0])
                        # Remove the oldest char in lookback and insert into TEMP[i]
                        TEMP[i] = lookback.pop(0)
                        # Convert back to string
                        list_of_scores[0] = "".join(TEMP)
                        # Rebuild the suffix tree with new strings
                        st = STree.STree(list_of_scores)
                        # Add any new pattern to the queue
                        if (st.lcs() != longest_common_substring and
                            st.lcs() not in queue and
                            st.lcs not in matches):

                            queue.append(st.lcs())

                    # Get enough x's to redact the pattern
                    redaction = 'x' * len(longest_common_substring)
                    # Replace the first occurence of the pattern with the x's
                    list_of_scores[0].replace(longest_common_substring, redaction,1)

                    # Re-Instantiate the lookback becuase we used pop()
                    lookback = list(longest_common_substring)
                    # Remove the redaction one byte at a time right to left
                    for i in range(lcs_end-1, lcs_start-1, -1):
                        # Strings are imutable so we change the type for a moment
                        TEMP = list(list_of_scores[0])
                        # Remove the newest char in lookback and insert into TEMP [i]
                        TEMP[i] = lookback.pop()
                        # Convert back to string
                        list_of_scores[0] = "".join(TEMP)
                        # Rebuild the suffix tree with new strings
                        st = STree.STree(list_of_scores)
                        # Add any new pattern to the queue
                        if (st.lcs() != longest_common_substring and
                            st.lcs() not in queue and
                            st.lcs not in matches):

                            queue.append(st.lcs())

                    # Get enough x's to redact the pattern
                    redaction = 'x' * len(longest_common_substring)
                    # Replace the first occurence of the pattern with the x's
                    list_of_scores[0].replace(longest_common_substring, redaction,1)

                if not(lookback) and not(queue):
                    break
            print(matches)
