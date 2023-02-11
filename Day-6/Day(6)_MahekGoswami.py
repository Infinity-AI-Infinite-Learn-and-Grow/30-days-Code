# Day6

top_developer=("Rahul","Qazi")
founder=("Steve" ,"Jeff")
scientist=("James","Ernest")

#Joining the tuples
mastermind_tp = top_developer + founder + scientist

#Adding value 
mastermind_list=list(mastermind_tp)
mastermind_list.append("Newton")
mastermind_tp=tuple(mastermind_list)
print(mastermind_tp)

#Printing first and last element
print("First element is: ",mastermind_tp[0])
print("Last element is: ",mastermind_tp[-1])

#Slicing mid elements
middleIndex=int(len(mastermind_tp)-1/2)
mastermind_list.pop(middleIndex)
mastermind_tp=tuple(mastermind_list)
print("Modified tuple after slicing mid element :",mastermind_tp)