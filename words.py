def print_upper_words(words, must_start_with):
    """Print each word in the given list that starts with any of the letters in must_start_with in all uppercase."""
    for word in words:
        if any(word[0].lower() == letter.lower() for letter in must_start_with):
            print(word.upper())

# Testing the function
print_upper_words(["hello", "world", "python", "Example", "easy"],
                   must_start_with={"h", "E", "y"})

