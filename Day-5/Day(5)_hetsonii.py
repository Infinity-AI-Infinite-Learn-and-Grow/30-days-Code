#Declaration
IT_Company=["Meta", "Amazon", "Apple", "Netflix", "Google", "Microsoft"]
size = len(IT_Company)
print(IT_Company[0],IT_Company[(int(size/2))],IT_Company[size-1])

#Inserting an element
IT_Company.insert(2,"IBM")
IT_Company.append("Infosys")
print(IT_Company)

#Reversing the list
IT_Company.sort()
IT_Company.reverse()
print("Reversed list in Descending Order: {}\n".format(IT_Company))

#Removing an element
IT_Company.pop()
print(IT_Company)

#Destroying the list
del IT_Company

try:
    print(IT_Company)

except Exception:
    print("List has been deleted.")
