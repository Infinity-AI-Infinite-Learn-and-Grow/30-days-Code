# Declare IT_Company list with more than 5 values.

list=['Tata Consultancy Services',
'OpenXcell',
'Agile Infoways Pvt Ltd',
'RapidOps',
'RadixWeb',
'Tatvasoft']

# Print the first, middle, and last company

print( "First => "  + list[0])
print("Middle => "  + list[len(list)//2])
print("Last => "  + list[-1])

# Insert it company name at a second position and last position.

list.insert(2,"Oracle")
list.append("IBM")

# Reverse the list in descending order using the reverse() method
list.reverse()
print(list)

# Remove the last IT company from the list
list=list[0:-1]
print(list)

# Destroy the IT company's list
del list