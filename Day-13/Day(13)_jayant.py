numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
l=[x for x in numbers if x<=0]
print(l)

L=[0,1,2,3,4,5,6,7,8,9,10]
lst = [(x,x**0,x**1,x**2,x**3,x**4,x**5) for x in L]
print(lst)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

lc=[{"country: {}, city: {}".format(x[0][0],x[0][1]) for x in countries}]
print(lc)
