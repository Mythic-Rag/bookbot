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
