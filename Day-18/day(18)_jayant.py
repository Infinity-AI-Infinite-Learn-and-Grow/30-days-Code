def is_valid_variable_name(s):
    if s[0].isdigit():
        return False
    for i in s:
        if i.isdigit() or i.isalpha() or i=='_':
            continue
        else:
            return False
    return True

s=input()
print(is_valid_variable_name(s))

def clean_string(sentence):
    new_sentence = ''
    for i in sentence:
        if i.isalpha():
            new_sentence += i
        elif i == ' ':
            new_sentence += i
    return new_sentence

def most_frequent_word(sentence):  
    sentence = clean_string(sentence)
    words = list(sentence.split(' '))
    for i in range(3):
        t=max(set(words), key = words.count),words.count(max(set(words), key = words.count))
        words.remove(max(set(words), key = words.count))
        print(t)
    


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
print(clean_string(sentence))
most_frequent_word(sentence)
