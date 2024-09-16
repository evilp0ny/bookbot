file_path = "books/frankenstein.txt"

def main ():
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    char_dict = get_char_dict(book_text)
    list_of_dict = make_dict_list(char_dict)
    
    print_final_report(file_path, list_of_dict, num_words)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
            
def get_num_words(book_text):
    return len(book_text.split())

def get_char_dict(book_text):
    book_text_lowered_case = book_text.lower()
    character_dict = {}
    for character in book_text_lowered_case: 
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def make_dict_list(char_dict):
    dict_list = []
    for i in char_dict:
        if i.isalpha():
            new_dict = {"char" : i, "num" : char_dict[i]}
            dict_list.append(new_dict)
    return dict_list
    
def sort_on(dict):
    return dict["num"]

def print_final_report(file_path, list_of_dict, num_words):
    
    print(f"=== Begin report on {file_path} ===")
    print("=============================")
    print(f"Your book has {num_words} words in it!")
    print("=============================")
    
    list_of_dict.sort(reverse = True, key = sort_on)
    
    for dict in list_of_dict:
        char = dict["char"]
        num = dict["num"]
        message = f"The '{char}' character was found {num} times"
        print(message)
    print("=== End report ===")

main()