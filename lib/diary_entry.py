import math
class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        if title == "" or contents == "":
            raise Exception("Contents should not be empty!")
        self._title = title        # "_" makes them private
        self._contents = contents   # "_" private
        self._read_so_far = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self._title.title()}: {self._contents.capitalize()}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        # title_length = len(self._title.split())       I used two variables to store words from .split()
        # contents_length = len(self._contents.split())

        # return title_length + contents_length         Then returned the len of them added together

        words = self.format().split()       # this way by Kay is more concise and efficient
        return len(words)                   # just store the result from format() in a varibale words 
                                            # and return its lenght

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if wpm == 0:
            raise Exception("Value of wpm should not be 0")
        contents_word_count = len(self._contents.split())
        return math.ceil(contents_word_count / wpm)
    

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        words_user_can_read = wpm * minutes
        words = self._contents.split()
        if self._read_so_far >= len(words):
            self._read_so_far = 0
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self._read_so_far = words_user_can_read
        return " ".join(chunk_words)
