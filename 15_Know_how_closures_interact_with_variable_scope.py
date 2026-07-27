# Know how closures interact with variable scope
# ------------------------------------------------------------------------

# Example: You want to sort a list of notifications but prioritize one group above the rest.
# A common way to do this is to pass a helper function as the key argument to a list's sort method.

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
priority = {2, 3, 5, 7}
sort_priority(numbers, priority)
print(numbers)

# The reason this works: Python supports closures: functions that refer to variables from the scope in which they are defined

# Functions are first-class objects in Python: you can refer to them directly, pass them as arguments to other functions,
# and compare them in expressions and if statements, etc.

# Python has specific rules for comparing tuples: it first compares items from index 0, then index 1, index 2, and so on.
# This is why the return value from the helper closure causes the sort order to have 2 distinct groups.

# Python closure is a nested function that allows us to access variables of the outer function even after the outer
# function is closed.
def greet(name):
    # inner function
    def display_name():
        print("Hi", name)

    # call inner function
    display_name()


# call outer function
greet("John")

# Output: Hi John

# HOWEVER, the closure cannot change a variable in the enclosing function so the flow of data is one-way from the
# larger scope down into the closure but not from the closure back up to the enclosing function.

# In Python 3, there is a special syntax for getting data out of a closure. The nonlocal statement is used to indicate
# that scope traversal should happen for a specific variable name. The only limit is that nonlocal won't traverse up
# to the module level (to avoid polluting the global scope)

def sort_priority3(numbers, group):
    found = False # whether
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    print(found)
    return found

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
priority = {2, 3, 5, 7}
sort_priority3(numbers, priority)
print(numbers)

# The side effects of nonlocal can be hard to follow so for long functions it may be better to wrap your state in
# a helper class:

class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(priority)
numbers.sort(key = sorter)
assert sorter.found is True