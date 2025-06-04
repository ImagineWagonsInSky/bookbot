from typing import List, Dict

def get_num_words(text: str) -> int:
    num_words = len(text.split()) # empty split will just get rid of whitespace
    return num_words

def get_character_counts(text: str) -> dict:
    count_dict = {}
    lower_text = text.lower()
    for i in range(len(lower_text)):
        if lower_text[i] in count_dict:
            count_dict[lower_text[i]] += 1
        else:
            count_dict[lower_text[i]] = 1
    
    return count_dict


def get_sorted_dicts(dictionary: dict) -> List[Dict]:
    # Exclude whitespace characters from the dictionary
    filtered_dict = {k: v for k, v in dictionary.items() if not k.isspace()}
    # Sorting key-value pairs by value descending, and by key if values are the same
    sorted_items = sorted(filtered_dict.items(), key=lambda kv: (-kv[1], kv[0]))

    list_of_dicts = []
    for k, v in sorted_items:
        list_of_dicts.append({"char": str(k), "num": v})
    return list_of_dicts
