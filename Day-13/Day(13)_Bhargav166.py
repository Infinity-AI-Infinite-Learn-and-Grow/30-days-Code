# Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), (2, 1, 2, 4, 8, 16, 32), (3, 1, 3, 9, 27, 81, 243), (4, 1, 4, 16, 64, 256, 1024), (5, 1, 5, 25, 125, 625, 3125), (6, 1, 6, 36, 216, 1296, 7776), (7, 1, 7, 49, 343, 2401, 16807), (8, 1, 8, 64, 512, 4096, 32768), (9, 1, 9, 81, 729, 6561, 59049), (10, 1, 10, 100, 1000, 10000, 100000)]
# Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print("Only negative and zero:")
print([i for i in numbers if i <= 0])
print("\n")


def list_of_tuples(n):
    return [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(n)]


print("List of tuples:")
print(list_of_tuples(11))
print("\n")


countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print("Countries and cities:")

print([{'country': i[0][0].upper(), 'city': i[0][1].upper()}
      for i in countries])
