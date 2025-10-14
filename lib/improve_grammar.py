def improve_grammar(text):
    marks = [".", "!", "?"]

    if not isinstance (text, str):
        raise TypeError("Input must be a string")
    
    if text == "":
        raise Exception("Cannot enter an empty string")
    
    if text[-1] in marks and text[0].isupper():
        return True
    return False

improve_grammar("Hello world, I hoope you have been well. But are you?")
