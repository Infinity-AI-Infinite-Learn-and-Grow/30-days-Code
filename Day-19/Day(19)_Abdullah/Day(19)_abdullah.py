# 1. Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder: 
# # a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words

# 2. Extract all incoming email addresses as a list from the email_exchange_big.txt file
import re


def count_lines_and_words(filename):
    line_count = 0
    word_count = 0

    # Open the file and loop through each line
    with open(filename, "r") as file:
        for line in file:
            line_count += 1

            # Split the line into words and add to the word count
            words = line.split()
            word_count += len(words)

    return line_count, word_count


# Count lines and words in obama_speech.txt
filename = "Data/obama_speech.txt"
line_count, word_count = count_lines_and_words(filename)
print(f"{filename}: {line_count} lines, {word_count} words")

# Count lines and words in michelle_obama_speech.txt
filename = "Data/michelle_obama_speech.txt"
line_count, word_count = count_lines_and_words(filename)
print(f"{filename}: {line_count} lines, {word_count} words")

# Count lines and words in donald_speech.txt
filename = "Data/donald_speech.txt"
line_count, word_count = count_lines_and_words(filename)
print(f"{filename}: {line_count} lines, {word_count} words")

# Count lines and words in melina_trump_speech.txt
filename = "Data/melina_trump_speech.txt"
line_count, word_count = count_lines_and_words(filename)
print(f"{filename}: {line_count} lines, {word_count} words")


# ---- Task 2 ----
email_list = []

# Open the file and read the contents
with open("Data/email_exchange_big.txt", "r") as file:
    contents = file.read()

# Find all email addresses using regular expressions
email_pattern = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
email_matches = re.findall(email_pattern, contents)

# Add the email addresses to the list
for email in email_matches:
    email_list.append(email)

# Print the email list
print(email_list)
