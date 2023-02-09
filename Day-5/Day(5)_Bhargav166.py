# - Declare IT_Company list with more than 5 values.
# - Print the first, middle, and last company
# - Insert it company name at a second position and last position.
# - Reverse the list in descending order using the reverse() method
# - Remove the last IT company from the list
# - Destroy the IT company's list

IT_company = ["Microsoft", "IBM", "Oracle", "TCS", "Infosys"]
size = len(IT_company)

print("First company:\t{}".format(IT_company[0]))
print("Middle company:\t{}".format(IT_company[int(size/2)]))
print("Last company:\t{}\n".format(IT_company[size-1]))

print("Before Insertion:\n{}".format(IT_company))
IT_company.insert(1, "HCL Technologies")
IT_company.append("Wipro")
print("After Insertion:\n{}\n".format(IT_company))

IT_company.reverse()
print("Reversed list:\n{}\n".format(IT_company))

IT_company.pop()
print("After removing last company:\n{}\n". format(IT_company))

del IT_company
print("List check if exist or not:")
try:
    print("IT company list: ", IT_company)
except Exception:
    print("IT company list does not exist")
