
def count_words(string):
    number_of_words = len(string.split())
    return number_of_words

def count_characters(string):
    number_of_characters = {}
    string = string.lower()
    for i in range(1,len(string)):
        # create new entry if character hasn't been seen before
        if string[i] not in number_of_characters: 
            number_of_characters[string[i]] = 1
        else: 
            number_of_characters[string[i]] += 1
    return number_of_characters

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(chardict):
    sorted_list = []
    for ch in chardict: 
        sorted_list.append({"char": ch, "num": chardict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


