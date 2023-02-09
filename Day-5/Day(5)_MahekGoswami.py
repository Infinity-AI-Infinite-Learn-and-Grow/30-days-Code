# Day5

#-----Task 1-----

IT_Company=["Facebook", "Google", "Microsoft", "Apple", "IBM","TCS" ]

#Print the first, middle, and last company
print("First company :" ,IT_Company[0])

middleIndex = int((len(IT_Company) - 1)/2)
print("Middle company :" ,IT_Company[middleIndex])

print("Last company :" ,IT_Company[-1])
print("\t\t")

#------------------------------------------------------------------------

#Insert it company name at a second position and last position.

# input_company=input("Enter a IT comapnay name :")
new_company=input("Enter an IT company name : ")
print("Inserting company",new_company,"at second position")
IT_Company.insert(1,new_company)
print("Modified list is :",IT_Company)
print("\t\t")

#------------------------------------------------------------------------

#Reverse the list in descending order using the reverse() method

IT_Company.sort(reverse=True)
print("Reversed list in descending order is :\t" ,IT_Company)
print("\t\t")

#------------------------------------------------------------------------

#Remove the last IT company from the list
print("Removing last company index ")
IT_Company.pop()
print("Modified list is : " ,IT_Company )
print("\t\t")

#------------------------------------------------------------------------

# Destroy the IT company's list
print("Destroying the IT_Company list")
IT_Company.clear()
print("Modiefied list is : ",IT_Company)