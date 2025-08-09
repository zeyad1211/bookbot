def get_word_count(txt):
    words = txt.split()
    return len(words)

def get_char_count(txt):
    char_counts = {}
    for char in txt.lower():
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    return char_counts

def sort_on(items):
    return items["count"]

def lst_of_sorted_dicts(dictionary):
    lst = []
    for key, value in dictionary.items():
        lst.append({"char": key, "count": value})
    lst.sort(reverse=True, key=sort_on)
    return lst
    