def estimate_reading_time(text):
    if text == "":
        raise Exception("Empty string cannot be estimated!")
    words = text.split()
    word_count = len(words)
    return word_count/200
