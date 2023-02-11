# Declare IT_Company list with more than 5 values.
# Print the first, middle, and last company
# Insert it company name at a second position and last position.
# Reverse the list in descending order using the reverse() method
# Remove the last IT company from the list
# Destroy the IT company's list

# Declare IT_Company list with more than 5 values.
from re import I


print("\n")
IT_Company = ['Meta', 'Apple', 'Amazon', 'Netflix', 'Google']

# Print the first, middle, and last company
print("First name of the comapy is,", IT_Company[0], "middle name of the company is",
      IT_Company[int(len(IT_Company)/2)], "and the last name of the company is", IT_Company[4])

# Insert it company name at a second position and last position.
IT_Company.insert(2, "TCS")
IT_Company.append("WIPRO")
print(IT_Company)

# Reverse the list in descending order using the reverse() method
IT_Company.sort()
print(IT_Company)
IT_Company.reverse()
print("Reverse the list in descending order using the reverse() method: ", IT_Company)


# Remove the last IT company from the list
IT_Company.pop()
print("Remove the last IT company from the list", IT_Company)


# Destroy the IT company's list

del IT_Company
print("IT_Company's list is destroyed ")

print("\n")
