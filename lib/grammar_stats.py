class GrammarStats():
    def __init__(self):
        self._tests_checked = 0
        self._tests_good = 0

    def check(self, text):
        if text == "":
            raise Exception("Cannot enter an empty string")
        
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        punctuation = [".", "?", "!"]
        self._tests_checked += 1
        if text[0].isupper() and text[-1] in punctuation:
            self._tests_good += 1
            return True
        return False
    
    def percentage_good(self):
        return (self._tests_good / self._tests_checked) * 100