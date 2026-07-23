# Prefer Enumerator Over Range
# ------------------------------------------------------------------------

# random_bits = 0
# for i in range(64):
#     if randint(0, 1): # Randomly produces either 0 or 1, that is either False or True
#         random_bits |= 1 << i
#
# print(random_bits)

flavor_list = ['Vanilla', 'Chocolate', 'Pecan', 'Strawberry']
# for flavor in flavor_list:
#     print('%s is delicious' % flavor )

# for i in range(len(flavor_list)):
#     flavor = flavor_list[i]
#     print('%d %s' % (i + 1, flavor))

for i, flavor in enumerate(flavor_list, 1): # the number following 'flavor_list' is the number that enumerate should start from.
    print('%d: %s' % (i, flavor))