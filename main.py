book_path = 'books/book-1.txt' 

def count_letters(words):
    letters_stats = {}
    for word in words:
        for letter in word:
            letter_to_lower = letter.lower() 
            if not letter_to_lower.isalpha():
                continue
            if letter_to_lower in letters_stats:
                letters_stats[letter_to_lower] += 1 
            else:
                letters_stats[letter_to_lower] = 1 
    return sorted(letters_stats.items())

def format_and_output_text(words, letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{len(words)} words found in the document\n\n")
    for letter in letters:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")
with open(book_path) as f:
    file_contents = f.read()
    words = file_contents.split()

letters_count = count_letters(words)
format_and_output_text(words, letters_count)
