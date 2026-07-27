# 14 Prefer exceptions to returning None
# ------------------------------------------------------------------------

# Returning None: (this approach slightly mitigates the issue by returning a two-tuple - the first part returning whether there was an exception, and the second returning either the amount or None
def divide(a,b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

# the above is still problematic since the first part of the tuple can be ignored (using the underscore variable name (_) which is a Python convention for unused variables.
_, result = divide(0,5)
if not result:
    print('Invalid inputs')

def better_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

x,y = 5,3
try:
    result = better_divide(x,y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)

# Functions that return None are error-prone because None and other values (e.g. zero, the empty string) all evaluate to false in conditional expressions