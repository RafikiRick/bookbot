def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    letter_count_dict = get_letter_count(text)
    letter_count_list = dict_to_list(letter_count_dict)
    letter_count_list.sort(reverse=True, key=sort_on)
        
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words in document\n")

    for item in letter_count_list:
        print(f"The '{item["letter"]}' character was found {item["num"]} times ")
    
    print("--- End report --- ")

def get_text(path):
    with open(path) as f:
         return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter = {}
    for l in text:
        if l.isalpha():
            lowercase = l.lower()
            if lowercase in letter:
                letter[lowercase] += 1
            else:
                letter[lowercase] = 1
    return letter

def dict_to_list(dict):
    list_dict = []
    for key,value in dict.items():
            list_dict.append({"letter":key,"num":value})
    return list_dict

def sort_on(dict):
    return dict["num"]

main()