# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# 2. Read the countries API and find
#    a. the 10 largest countries
#    b. the 10 most spoken languages
#    c. the total number of languages in the country's API

# -- Task 1 --

import urllib.request
import re
from collections import Counter


def get_words(url):
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
    words = re.findall(r'\w+', text.lower())
    return words


def main():
    words = get_words('http://www.gutenberg.org/files/1112/1112.txt')
    print(Counter(words).most_common(10))


if __name__ == '__main__':
    main()


# -- Task 2 --
