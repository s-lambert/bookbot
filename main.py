def main():
  book_path = './books/frankenstein.txt' 
  with open(book_path) as f:
    file_contents = f.read()
    words = file_contents.split()
    letters = {}
    for word in words:
      for letter in word.lower():
        if letter in letters:
          letters[letter] += 1
        else:
          letters[letter] = 1
    letter_dicts = [{'letter': k, 'count': v} for k, v in letters.items() if k.isalpha()]
    letter_dicts.sort(reverse=True, key=lambda letter: letter['count'])
    print(f"--- Begin report of {book_path} ---")
    print(f"{len(words)} words found in the document\n")
    for letter_dict in letter_dicts:
      print(f"The '{letter_dict['letter']}' character was found {letter_dict['count']} times")
    print("--- End report ---")

main()