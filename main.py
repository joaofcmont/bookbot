from stats import word_counter,word_converter,sorted_dictionary
import sys 

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    book_text = get_book_text(file)
    counter_of_words = word_counter(book_text)
    word_dict = word_converter(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {counter_of_words} total words")
    print("--------- Character Count -------")
    sorted_dict = sorted_dictionary(word_dict)
    for item in sorted_dict:
         char = item["char"]
         count = item["num"]
         if char.isalpha():
              print(f"{char}: {count}")

def get_book_text(path):
        with open(path) as f:
            content = f.read()
        return content         

main()