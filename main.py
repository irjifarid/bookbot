def main():
    path_to_file = "books/frankenstein.txt"

    try:
        with open(path_to_file, "r") as f:
            file_contents = f.read()
            print("--- Begin report of", path_to_file, "---")
            print(f"{count_words(file_contents)} words found in the document\n")

            # Call the new function to count letters
            letter_count = count_letters(file_contents)

            # Sort the letters alphabetically
            sorted_letters = sorted(letter_count.items(), key=lambda x: x[0])

            # Print character occurrences
            for char, count in sorted_letters:
                print(f"The '{char}' character was found {count} times")

            print("--- End report ---")
    except FileNotFoundError:
        print(f"Error: File '{path_to_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    # Convert text to lowercase and remove non-alphabetic characters
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    
    # Use a dictionary to count occurrences of each character
    letter_count = {}
    for char in cleaned_text:
        letter_count[char] = letter_count.get(char, 0) + 1
    
    return letter_count

if __name__ == "__main__":
    main()
