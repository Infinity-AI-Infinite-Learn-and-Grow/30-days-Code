#Day 14

#------Task 1------
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def cap_list(ele):
  return ele.capitalize()
    
result_countries = map(cap_list, countries)
result_names = map(cap_list, names)
final_list=list(result_countries)+list(result_names)
print(final_list)

#------Task 2------
def myFunc(letters):
  if len(letters)==6:
    return True
  else:
    return False

countries_new = filter(myFunc, countries)
print(list(countries_new))

#------Task 2------
def fib(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b
f = fib()
print(', '.join(str(next(f)) for _ in range(5)))