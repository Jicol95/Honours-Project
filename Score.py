from music21 import converter, stream, interval


class Score:
    '''
    This class is a representaion of one musical score and all its voices.
    '''

    def __init__(self, filename):
        '''
        Args:
            filename (str): The filename of the score you want to represent as a
                           class.

        Attributes:
            name: The name of the score.
            parsed_score (obj): The kern** representation parsed as a music21
                                object.

            voices (obj): A list of all the separate voices in the score.
            voice_count(int): A count of how many voices are in the composition
            melodicIntervals(obj): A list of interval objects which represent
                                   the melodic distance of note pairs.
            contour_abstract(Array: list(str)): A list of intervals in symbolic
                                                form eg. [+,0,-]
        '''
        self.name = filename
        self.parsed_score = None
        self.voice_notes = None
        self.voices = None
        self.voice_count = None
        self.melodicIntervals = None
        self.contour_abstract = None
        self.contour_suffix_array = None
        self.kern_parse(self.name)
        self.voice_split(self.parsed_score)
        self.get_melodic_interval(self.voices, self.voice_count)
        self.get_abstract_contour(self.melodicIntervals, self.voice_count)
        self.sequences = []

    def kern_parse(self, filename):
        '''
        This function turns kern represented music into a music21 object

        Args:
            filename (str): The filename of the score you want to represent as a
                            class.

        Returns:
            parsed_score (obj): The kern** score as a music21 object.
        '''

        # Denotes the path to the collection of music
        filepath = ['Music/', filename, '.krn']
        filepath = ''.join(filepath)
        # Uses the music21 library to convert kern to a music21 object
        score = converter.parse(filepath)
        self.parsed_score = score

    def voice_split(self, score):
        '''
        This function splits up a score of many voices into an array of voice
        objects.

        Args:
            score (obj): The music21 representation of the score.

        Returns:
            voices (array: list(obj)): A list of voice objects representing each
                                       musical vocie.
            voice_count(int): The number of vocies in the composition.
        '''

        # If a score contains multiple voices then separate them
        score_split = score.voicesToParts()
        # Count how many voices there are in total
        score_number_of_voices = len(score_split)
        self.voices = score_split
        self.voice_count = score_number_of_voices

    def get_melodic_interval(self, voices, voice_count):
        '''
        This function takes each voice and calculates the intervals of each notes
        pairs.

        Args:
            voices (Array: List(obj)): A list of voice objects representing
                                       musical voices.
            voice_count (int): The number of voices in the composition.

        Returns:
            melodicIntervals(Array:list(obj)): A list of voices in the form of
                                               interval objects.
        '''

        # Intitate the list containing the melodic intervals
        score_voices_intervals = []
        score_voices_notes = []
        # For each voice in the composition
        for i in range(0, voice_count, 1):
            # Rid notation that effects parsing
            score = voices[i].flat
            # Get the notes of that voice in a list
            score = score.notes.stream()
            score_voices_notes.append(score)
            # calculates the melodic intervals for each note pair
            score = score.melodicIntervals()
            # append the list of intervals to the list containing melodic
            # intervals
            score_voices_intervals.append(score)
        # Update self value from None
        self.voice_notes = score_voices_notes
        self.melodicIntervals = score_voices_intervals

    def get_abstract_contour(self, melodicIntervals, voice_count):
        '''
        This function takes in melodicIntervals and abstracts it to a notion of
        upward/downward/flat melodic motion. In other words it captures the
        melodic contour of the composition.

        Args:
            melodicIntervals(Array:list(obj)): A list of voices in the form of
                                               interval objects.
            voice_count (int): The number of voices in the composition.
        Returns:
            contour_abstract Array:list(Array:list(char)): A list of symbols
                                                          (+/-/0) representing
                                                          wheather the meloidic
                                                          interval
                                                          increased/decreased/stayed
                                                          the same.
        '''
        # intitate list containing melodic contours of all voices
        voices_abstract_contours = []
        # for each voice in the composition
        for i in range(0, voice_count, 1):
            # list of abstract intervals of the ith voice
            voice_abstract_contour = []
            # For all the intervals in the voice
            for interval in melodicIntervals[i]:
                # Check if the intervall was DESCENDING/ASCENDING OR OTHER
                if str(interval.direction) == 'Direction.DESCENDING':
                    voice_abstract_contour.append('-')
                elif str(interval.direction) == 'Direction.ASCENDING':
                    voice_abstract_contour.append('+')
                else:
                    voice_abstract_contour.append('0')
            # Append that interval to the list of abstarct iintervals for
            # contours of all voices
            voices_abstract_contours.append(voice_abstract_contour)
        # update the self value from None
        self.contour_abstract = voices_abstract_contours

    def get_contour_suffix_array(self):
        pass
