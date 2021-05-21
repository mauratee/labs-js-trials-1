"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

print(output_all_items([1, 'hello', True]))

def get_all_evens(nums):
    evens=[]
    for num in nums:
        # print(num)
        if num % 2 == 0:
            # print(num)
            evens.append(num)
    return evens


print(get_all_evens([7, 8, 10, 1, 2, 2]))

def get_odd_indices(items):
    pass  # TODO: replace this line with your code


def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code


def get_range(start, stop):
    pass  # TODO: replace this line with your code


def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
