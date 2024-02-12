def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words in document\n")
    
    letter_count_dict = get_letter_count(text)
    letter_count_list = dict_to_list(letter_count_dict)

    letter_count_list.sort(reverse=True, key=sort_on)
    
    report_builder(letter_count_list)
    print("--- End report --- ")

def get_text(path):
    with open(path) as f:
         return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    lower_text = text.lower()
    letters = {i:lower_text.count(i) for i in lower_text}
    return letters

def dict_to_list(dict):
    list_dict = []
    for key,value in dict.items():
        if str(key).isalpha():
            list_dict.append({"letter":key,"num":value})
    return list_dict

def sort_on(dict):
    return dict["num"]

def report_builder(list):
    for dict in list:
        letter = dict["letter"]
        num = dict["num"]
        print(f"The '{letter}' character was found {num} times ")
main()