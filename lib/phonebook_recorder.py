class PhonebookRecorder():

    def __init__(self):
        self._number_list = set()
    # store numbers in a set avoiding duplicates

    def add_number(self, text):
        if text == "":
            raise Exception("Entry should not be empty")
        words = text.split()
        for word in words:
            formatted_word = word.replace("-", "").replace(" ", "")
            if formatted_word.isdigit() and len(formatted_word) == 11:
                self._number_list.add(formatted_word)
            
        # self._number_list().append(text)
    # adds/append text to self._number_list

    def get_number(self):
        return sorted(list(self._number_list))
    # returns list of string