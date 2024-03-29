# 2019/10/27

# Create a function /break_words/ to split a file.
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # .split记录
    return words
# Create a function /sort_words/ to sort words from the splitted file.
def sort_words(words):
    """Sorts the words"""
    return sorted(words) # sorted()记录
# Create a function to print 1st word.
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # pop ()记录
    print(word)
# Create a function to print the last word.
def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

sentence = input (">")
break_sentence = break_words(sentence)
