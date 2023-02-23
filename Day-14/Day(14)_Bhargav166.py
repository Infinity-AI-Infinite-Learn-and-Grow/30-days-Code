# - countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# - names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# - numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1. Use a map to create a new list by changing each country and name to uppercase in the countries list
# 2. Use a filter to filter out countries having precisely six characters.
# 3. Using the generator print the Fibonacci series.

def upper(itr):
    return itr.upper()


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
country_in_uppercase = map(upper, countries)
print("Countries in uppercase:")
print(list(country_in_uppercase))


def six_char(str):
    if len(str) != 6:
        return True
    else:
        return False


filtered = filter(six_char, countries)
print("\nCountries not having six character long names:")
print(list(filtered))


def fibonacci(n):
    n1 = 0
    n2 = 1

    while (n1 < n):
        yield n1
        n1, n2 = n2, n1+n2


print("\nFibonacci series: ")
for i in fibonacci(50):
    print(i, end=" ")
print("...")
