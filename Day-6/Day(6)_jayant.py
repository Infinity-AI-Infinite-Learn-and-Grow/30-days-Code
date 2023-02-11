#creation of tuples

top_developer=(1,2,3,)
founder=(4,5,6,)
scientist=(8,9,)
print("Top developer:",top_developer)
print("Founder:",founder)
print("Scientist:",scientist)

#concatenation of tuples

mastermind_tp=()
mastermind_tp=top_developer+founder+scientist
print("Mastermind:",mastermind_tp)

#slicing of tuples
print("first element of tuple is:-",mastermind_tp[0])
print("last element of tuple is:-",mastermind_tp[-1])
l=len(mastermind_tp)
print("slicing to the mid value of the tuple:-",mastermind_tp[:l//2])

#adding elements to tuples
mastermind_tp.append(10)
print("Mastermind:",mastermind_tp)
#the error shows because tuples are immutable
#so for the addtion of elements we have to create a new tuple and have to add it to the previous tuple
