def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    
    total_word_count = count_word(text)
    
    char_dict = get_char_dict(text)

    char_sorted_list = char_dict_to_sorted_list(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_word_count} words found in the document")
    print("")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_word(text):
    words = text.split()
    length = len(words)
    return length

def get_char_dict(text):
    chars = {}
    for i in text.lower():
        if i in chars:
            chars[i] = chars[i] + 1
        else:
            chars[i] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for c in char_dict:
        sorted_list.append({"char" : c ,"num"  :char_dict[c]})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list

main()
