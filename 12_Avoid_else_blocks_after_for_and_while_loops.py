# Avoid 'else' blocks after 'for' and 'while' loops
# ------------------------------------------------------------------------

# This is allowed in Python
a = 4
b = 9

for i in range(2, min(a,b) + 1):
    print('Testing...', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')

# A better way to do this is:
def coprime(a,b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

print(coprime(2, 4))