# NOTE: You can *not* have an argument with a default preceed one without a default
# defaults_fn(bar = 3, foo, zoo = 'star') would not work
def defaults_fn(foo, bar = 3, zoo = 'star'):
    print(foo * bar, 'world', zoo)

defaults_fn('hello')

# NOTE: You can get around order of args by using arg keywords (names) when you call the fn
defaults_fn('hi', zoo = 'stage')

# NOTE: Python has two types of spread operators: the first has just one asterisk
# Using the first form will produce a tuple (1,2,3...) which can be accessed like a list/array
def varargs_fn(usual = 'normal', *various_in_tuple):
    print(usual)
    for whatever in various_in_tuple:
        print(whatever)

varargs_fn('first', 1,2,3,4,5)

# NOTE: The second type of spread operator creates a dict, using the keywords in the fn call
def double_asterisk_fn(usual = 'normal', **dict_of_args):
    print(usual)
    # NOTE: to access the pairs of a dict in a for loop, you need the items() method
    for key, val in dict_of_args.items():
        print(key, val)

double_asterisk_fn('hello', foo = 'first in the dict', bar = 'second')
