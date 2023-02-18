countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_countries=map(lambda x: x.upper(), countries)
print(list(new_countries))


countries_filter=filter(lambda x: len(x) == 6, countries)
print(list(countries_filter))

# A simple generator for Fibonacci Numbers
def fib(limit):
	a, b = 0, 1
	while a < limit:
		yield a
		a, b = b, a + b
x = fib(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

