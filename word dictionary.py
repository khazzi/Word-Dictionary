from PyDictionary import PyDictionary

def get_word_definition(word):
    dictionary = PyDictionary()
    
    try:
        definition = dictionary.meaning(word)
        return definition
    except Exception as e:
        return f"Error: {e}"

# Example of using the function
word_to_lookup = input("Enter the word to search for: ")
result = get_word_definition(word_to_lookup)

if isinstance(result, dict):
    print(f"Definitions for '{word_to_lookup}':")
    for part_of_speech, meanings in result.items():
        print(f"{part_of_speech.capitalize()}: {', '.join(meanings)}")
else:
    print(result)
