# 1. Write a pattern which identifies if a string is a valid python variable
# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True

# 2. Clean the following text. After cleaning, count three most frequent words in the string.
# sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# print(clean_text(sentence));
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

# ---- Task 1 ----
from collections import Counter
import re


def is_valid_variable(variable_name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable_name))


print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

# ---- Task 2 ----

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re 
rewarding as educa@ting &and& @emp%o@wering peo@ple. ; I found tea@ching m%o@re interesting tha@n 
any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_text = re.sub(r'[^a-zA-Z\s]', '', sentence)
print(clean_text)
