#Write a pattern which identifies if a string is a valid python variable is_valid_variable('first_name') # True is_valid_variable('first-name') # False is_valid_variable('1first_name') # False is_valid_variable('firstname') # True

import re
def is_valid_variable(s):
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', s))

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

#Clean the following text. After cleaning, count three most frequent words in the string. sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

import re
from collections import Counter
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_text = re.sub(r'[^a-zA-Z\s]', '', sentence)
print(clean_text)