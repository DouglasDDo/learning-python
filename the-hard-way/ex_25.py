def splitting_strs(phrase):
    words = phrase.split(' ')
    return words

def sorting_chars(phrase):
    # NOTE: returns a sorted array of chars
    return sorted(phrase)

def print_first(phrase):
    # NOTE: You can feed in index to pop(); negative indices also work, i.e., -1 is last
    if isinstance(phrase, str):
        return splitting_strs(phrase).pop(0)
    else:
        return phrase.pop(0)
    # NOTE: There's no unshift() for list objects
    # return phrase.unshift()

def print_last(phrase):
    if isinstance(phrase, str):
        return splitting_strs(phrase).pop()
    else:
        return phrase.pop()

def sort_sentence(phrase):
    # NOTE: In a sort of words, upper-case letters take priority over lower-case
    return sorted(splitting_strs(phrase))

def print_first_and_last(phrase):
    words = splitting_strs(phrase)
    result = print_first(words), print_last(words)
    for word in result:
        print word

print splitting_strs("hi there")
print sorting_chars("hello there")
print print_first("first second")
print print_last("1st 2nd")
print sort_sentence("This is a sentence")
print_first_and_last("Who let the dogs out?")
