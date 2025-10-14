def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
        print(char)
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[1][0] # this line was where the bug was
    print(letter)
    return letter
    # THE bug HAS BEEN FIXED. It was on line 6. 
    # The key=lambda method applied on the letter list on line 6, was indexing the least common letter in the text "(item[1])[0][1]""
    # as the list returned was in asccending order, we had to reverse it and then apply
    # the correct index for "e" which we found by printing the letter list
    # in the Debug console to pin point the index for the expected "e" letter. 

print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
