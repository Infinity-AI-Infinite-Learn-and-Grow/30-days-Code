top_developer = ('Missy', 'Jeff', 'Mary')
founder = ('Sheldon', 'George', 'Billy')
scientists = ('Linkletter', 'Sturgis', 'Paige')

mastermind_tp = top_developer + founder + scientists
length = len(mastermind_tp)
print("Joined Tuple is: {}".format(mastermind_tp))

print("First element is: {}".format(mastermind_tp[0]))
print("Last element is: {}".format(mastermind_tp[length-1]))

mastermind_lt=list(mastermind_tp)

if(length%2!=1):
    mastermind_lt.remove(mastermind_tp[int(length/2)])
    mastermind_lt.remove(mastermind_tp[int((length/2)+1)])
else:
    mastermind_lt.remove(mastermind_tp[int(length/2)])

mastermind_tp = tuple(mastermind_lt)

print("Tuple after removing the elemesmt: {}".format(mastermind_tp))