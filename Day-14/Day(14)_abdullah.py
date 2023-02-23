# - countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# - names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# - numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1. Use a map to create a new list by changing each country and name to uppercase in the countries list
# 2. Use a filter to filter out countries having precisely six characters.
# 3. Using the generator print the Fibonacci series.


# 1. Use a map to create a new list by changing each country and name to uppercase in the countries list

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']


def upper_case(num):
    return num.upper()


uc_list = list(map(upper_case, countries))
print(uc_list)  # [1, 8, 27, 64, 125]


# 2. Use a filter to filter out countries having precisely six characters.
def length_of_countries(countries):
    return len(countries) == 6


result = list(filter(lambda x: length_of_countries(x), countries))

# Print the result
print(result)

# 3. Using the generator print the Fibonacci series.


def fibonacciGenerator():
    a = 0
    b = 1
    for i in range(6):
        yield b
        a, b = b, a+b


obj = fibonacciGenerator()

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
