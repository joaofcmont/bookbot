def word_counter(text):
    total_counter = 0
    new_text = text.split()
    for word in new_text:
        total_counter+=1
    return total_counter  

def word_converter(text):
    word_dict = {}
    new_text = text.lower()
    for word in new_text:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def sort_on(dictionary):
    return dictionary["num"]

def sorted_dictionary(dict):
    new_list = []
    for word,count in dict.items():
        dict_info = {"char": word, "num": count}
        new_list.append(dict_info)
    new_list.sort(reverse=True, key=sort_on)
    return new_list


