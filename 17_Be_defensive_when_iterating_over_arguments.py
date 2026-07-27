# Be Defensive When Iterating Over Arguments
# ------------------------------------------------------------------------

# Calculating the percentage of visitors each city contributes to Texas' tourism total
# Sum up the individual cities contributions and divide that total by each city's total
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
# print(percentages)

# To scale this up, read the data from a file. Define a generator to do this so that the same equations can be used
# on a data set of the whole world.

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            line_stripped = line.strip(',\n')
            yield int(line_stripped)

it = read_visits('./temp/my_numbers.txt')
percentages_file = normalize(it)
# print(percentages_file)

# percentages_file is an empty list because the iterator only produces its result a single time. If you iterate over
# over an iterator or generator that has already raised a StopIteration exception, you won't get any results the
# second time around. Many functions in Python can't tell the difference between an iterator that has no output and
# one that had output and is now exhausted.

# To solve this problem, you can explicitly exhaust an input generator and keep a copy of its entire contents in a list.

def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('./temp/my_numbers.txt')
percentages_file_copy = normalize_copy(it)
print(percentages_file_copy)