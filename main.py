def count_letters(book):
    letter_dict = {}
    for char in book.lower():
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1

    sorted_letter = []
    for char in letter_dict:
        if char.isalpha():
            sorted_letter.append({"char": char, "num": letter_dict[char]})

    sorted_letter.sort(reverse=True, key=sort_on)

    return sorted_letter


def sort_on(d):
    return d["num"]


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    
    sorted_letters = count_letters(file_contents)
    for i in sorted_letters:
        print(f"The '{i['char']}' character was found {i['num']} times")

    print("--- End report ---")
    

