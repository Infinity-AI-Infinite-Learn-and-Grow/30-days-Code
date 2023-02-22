#Day 18

#------Task 1------
import re

def is_valid_variable(variable_name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable_name))

print(is_valid_variable('first_name')) 
print(is_valid_variable('first-name')) 
print(is_valid_variable('1first_name')) 
print(is_valid_variable('firstname')) 
print("\t")

#------Task 2------
import re
from collections import Counter

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_text = re.sub(r'[^a-zA-Z\s]', '', sentence)
print(clean_text)