# Create top_developer, founder, and scientist tuples.
# Join the three tuples and assign them to a variable called mastermind_tp.
# Add value in this tuple.
# Print the first and last element on this same tuple time.
# Slice out the middle item or items from the mastermind_tp tuple.


# Create top_developer, founder, and scientist tuples.
top_developer = ('Ram', 'Elon', 'Musk')
founder = ('Mark', 'Bill', 'Gates')
scientists = ('APJ', 'Krishna', 'Venkatesh')

# Join the three tuples and assign them to a variable called mastermind_tp.
mastermind_tp = top_developer + founder + scientists
length = len(mastermind_tp)

# Add value in this tuple.
print("Joined Tuple is: {}".format(mastermind_tp))

# Print the first and last element on this same tuple time.
print("First element is: {}".format(mastermind_tp[0]))
print("Last element is: {}".format(mastermind_tp[length-1]))

# Slice out the middle item or items from the mastermind_tp tuple.
mastermind_lt = list(mastermind_tp)

if (length % 2 != 1):
    mastermind_lt.remove(mastermind_tp[int(length/2)])
    mastermind_lt.remove(mastermind_tp[int((length/2)+1)])
else:
    mastermind_lt.remove(mastermind_tp[int(length/2)])

mastermind_tp = tuple(mastermind_lt)

print("Tuple after removing the elemesmt: {}".format(mastermind_tp))
