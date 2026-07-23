# Item 9: Consider Generator Expressions for Large Comprehensions
# ------------------------------------------------------------------------

# Using list comprehension: only works for small input values. In this case a text file with a small number of items
# list comprehension requires the entire list be held in memory while generator expression will evaluate each line separately.
# value = [len(x) for x in open('../Dev/Python/Effective_Python/temp/my_file.txt')]
# print(value)

# Using a generator expression: immediately evaluates to an iterator
it = (len(x) for x in open('./temp/my_file.txt'))
# print(it) = <generator object <genexpr> at 0x10429ab50>
print(next(it))
print(next(it))
# the above 2 print functions will step through my_file.txt and give the length of each line

# generator expressions can be composed together:
# roots = ((x, x**0.5) for x in it)
# print(next(roots))