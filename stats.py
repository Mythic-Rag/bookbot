def word_count(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    char_counts = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_character_counts(char_counts_dict):
    """
    Takes a dictionary of character counts and returns a sorted list of (character, count) tuples.
    Sorted by count in descending order.
    """
    sorted_chars = sorted(char_counts_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars

def get_formatted_sorted_character_report(char_counts_dict):
    """
    Takes a dictionary of character counts, filters for alphabetical characters,
    and returns a sorted list of dictionaries with 'char' and 'num' keys.
    """
    report_list = []
    
    # First, filter and format into the desired dictionary structure
    for char, count in char_counts_dict.items():
        if char.isalpha(): # Only include alphabetical characters
            report_list.append({"char": char, "num": count})
            
    # Then, sort the list of dictionaries by the 'num' (count) key in descending order
    # Using the .sort() method as requested
    report_list.sort(key=lambda item: item["num"], reverse=True)
    
    return report_list
