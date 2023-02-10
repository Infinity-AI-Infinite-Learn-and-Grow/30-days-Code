top_developer=('Terror','Cats','Warriors','Autocarts')

founder=('Steve Jobs','Jeff Bezos','Sunil Mittal','Bill Gates')

scientist=('Einstien','Thompson','Rutherford','Edison')

mastermind_tp=(top_developer+founder+scientist)

print(mastermind_tp)

#Add value in the tuple

y=list(mastermind_tp)

y.append('Yash Parmar')

mastermind_tp=tuple(y)

print(mastermind_tp)

#Print first and last element ->use indexing

print(mastermind_tp[0])

print(mastermind_tp[-1])

#Slicing

print(mastermind_tp[2: : 2])
