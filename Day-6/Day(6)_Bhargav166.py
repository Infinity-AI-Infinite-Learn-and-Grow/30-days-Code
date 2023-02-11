# - Create top_developer, founder, and scientist tuples. Join the three tuples and assign them to a variable called mastermind_tp.
# - Add value in this tuple.
# - Print the first and last element on this same tuple time.
# - Slice out the middle item or items from the mastermind_tp tuple.

top_developer = ("Dennis Ritchie", "Bjarne Stroustrup",
                 "Linus Torvalds", "James Gosling", "Tim Berners Lee")
founder = ("Bill Gates", "Steve Jobs", "Larry Page", "Mark Zuckerberg")
scientist = ("Albert Einstein", "Isaac Newton",
             "Galileo Galilei", "Marie Curie")

mastermind_tp = top_developer + founder + scientist
print("--------------------------\n\tMasterminds\n--------------------------")
for mastermind in mastermind_tp:
    print(mastermind)

mastermind_tp = mastermind_tp + ("Stephen Hawking",)
print("\n-------------------------------\n  Updated List of Masterminds\n-------------------------------")
for mastermind in mastermind_tp:
    print(mastermind)

print("\nFirst mastermind\t:", mastermind_tp[0])
print("Last mastermind\t\t:", mastermind_tp[-1])

# Middle masterminds


def MiddleMasterminds(mastermind_tp):
    if len(mastermind_tp) % 2 == 0:
        start_index = int(len(mastermind_tp) / 2) - 1
        end_index = int(len(mastermind_tp) / 2) + 1
        for i in range(start_index, end_index):
            print(mastermind_tp[i])
    else:
        index = int(len(mastermind_tp) / 2)
        print(mastermind_tp[index])


print("\n----------------------------------\n\tMiddle Mastermind/s\n----------------------------------")
MiddleMasterminds(mastermind_tp)
