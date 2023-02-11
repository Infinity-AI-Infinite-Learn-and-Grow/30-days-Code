"""Create top_developer, founder, and scientist tuples. Join the three tuples and assign them to a variable called mastermind_tp.
Add value in this tuple.
Print the first and last element on this same tuple time.
Slice out the middle item or items from the mastermind_tp tuple."""



top_developer=("shubham","shreya","sam")
founder=("ram","shyam","mona")
scientist=("shubham","shreya",)


mastermind_tp=top_developer+founder+scientist
print(mastermind_tp)
print(mastermind_tp[0])
print(mastermind_tp[-1])

#slice tuple
print(mastermind_tp[0:3])




