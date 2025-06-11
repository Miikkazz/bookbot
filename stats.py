def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_dicts(dicts):
    sorted_dicts = []
    for d in dicts:
        new_dict = {}
        new_dict["char"] = d
        new_dict["num"] = dicts[d]
        sorted_dicts.append(new_dict)
    sorted_dicts.sort(key=lambda x: x["num"], reverse=True)
    return sorted_dicts