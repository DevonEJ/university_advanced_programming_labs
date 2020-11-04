
def count_characters(sentence: str):
    counts_dict = {
        "A": "",
        "E": "",
        "I": "",
        "O": "",
        "U": ""
    }

    other_chars = 0

    for char in sentence.upper():
        if char in counts_dict.keys():
            counts_dict[char] = counts_dict[char] + "*"
        else:
            other_chars += 1

    for key, val in counts_dict.items():
        print(key+":", val)
    print("Other (non-space) Characters", other_chars)


# Call function
count_characters("The black cat sat up on the orange mat!")
