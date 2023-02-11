#Create top_developer, founder, and scientist tuples. Join the three tuples and assign them to a variable called mastermind_tp.

top_developer=('abc','def','xyz')
founder=('abctg','rtgr')
scientist=('ffkh','ghrj','hfkhf')


# Add value in this tuple.
mastermind_tp=(top_developer + founder  + scientist)
print(mastermind_tp)

#- Print the first and last element on this same tuple time.
print(mastermind_tp[0])
print(mastermind_tp[-1])

#- Slice out the middle item or items from the mastermind_tp tuple. 
#3 middle items
print(mastermind_tp[len(mastermind_tp)//2 -1 :len(mastermind_tp)//2 +2 ])