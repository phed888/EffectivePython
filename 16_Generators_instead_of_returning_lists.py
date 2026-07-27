# 16 Consider Generators Instead of Returning Lists
# ------------------------------------------------------------------------
from itertools import islice


# Returning a list:
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
           result.append(index + 1)
    return result

address = 'Four score and seven years ago...'
result = index_words(address)
# print(result)

# A better way to write this function is using a generator.
# A generator is a function that uses 'yield' expressions. When called, generators don't actually run but instead
# immediately return an iterator. With each call to the next built-in function, the iterator will advance the generator
# to its next yield expression. Each value passed to yield by the generator will be returned by the iterator to the
# caller. Uses 'yield' instead of 'return'.
# Since the function evaluates each element in the list and yields a result, it doesn't require the entire list be
# held in memory, making it great for large data sets.

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

result2 = list(index_words_iter(address))
# print(result2)

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

with open('./temp/my_file2', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 25)
    print(list(results))