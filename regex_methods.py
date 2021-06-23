import re
###################################################################################
################################ Searching functions ##############################
###################################################################################
# re.search(<regex>, <string>, flags=0)
re.search('[a-z]+', '123FOO456', flags=re.IGNORECASE)

# re.match(<regex>, <string>, flags=0)
re.match('\d+', '123foobar') # only string beginning
re.match('\d+', 'foo123bar')

# re.fullmatch(<regex>, <string>, flags=0)
re.fullmatch('\d+', '123') # only entire string
re.fullmatch(r'\d+', 'foo123')

# re.findall(<regex>, <string>, flags=0)
re.findall('\w+', '...foo,,,,bar:%$baz//|') # all matches in list
re.findall('#(\w+)#', '#foo#.#bar#.#baz#')
re.findall('(#\w+#)', '#foo#.#bar#.#baz#')

# re.finditer(<regex>, <string>, flags=0)
it = re.finditer('\w+', '...foo,,,,bar:%$baz//|') # all matches in iterator
next(it)
next(it)
next(it)

for i in re.finditer('\w+', '...foo,,,,bar:%$baz//|'):
    print(i)

###################################################################################
############################## Substitution functions #############################
###################################################################################
# re.sub(<regex>, <repl>, <string>, count=0, flags=0)
s = 'foo.123.bar.789.baz'
re.sub('\d+', '#', s)
re.sub('[a-z]+', '(*)', s)

def function10x(match_obj):
    s = match_obj.group(0)  # matching string
    if s.isdigit(): # True if all chars are digits
        return str(int(s) * 10)
    else:
        return s.upper()

re.sub('\w+', function10x, 'foo.10.bar.20.baz.30')

re.sub('\w+', 'xxx', 'foo.bar.baz.qux', count=2) # apply times

# re.subn(<regex>, <repl>, <string>, count=0, flags=0)
re.subn('\w+', 'xxx', 'foo.bar.baz.qux') # number of substitutions

###################################################################################
################################# Utility functions ###############################
###################################################################################
# re.split(<regex>, <string>, maxsplit=0, flags=0)
re.split('\s*[,;/]\s*', 'foo,bar  ;  baz / qux')

string = 'foo,bar  ;  baz / qux'
regex = '\s*[,;/]\s*' # comma, semicolon, slash, spaces
a = re.split(regex, string)

for i, s in enumerate(a):
    if not re.fullmatch(regex, s):
        a[i] = f'<{s}>'

''.join(a)


# re.escape(<regex>)
re.escape('foo^bar(baz)|qux') == 'foo\^bar\(baz\)\|qux'


# re.compile(<regex>, flags=0)
re_obj = re.compile(r'(\d+)')
re.search(re_obj, 'foo123bar')
re_obj.search('foo123bar')

re_obj = re.compile('ba[rz]', flags=re.I)
r2 = re.search(re_obj, 'FOOBARBAZ')
r3 = re_obj.search('FOOBARBAZ')


# example

'''
match() function checks for a match only at the beginning of the string (by default)
search() function checks for a match anywhere in the string
groups() function returns all the groups matched
'''

pattern = "^[a-zA-Z0-9.-]+@([a-z]+\.[a-z]+)$" # regular expression for common email validation
search_string = "some.user-name@example.com"
match = re.match(pattern, search_string) # re instance

if match:
    domain = match.groups()[0]
    print(domain)

# example text parsing
import requests
the_idiot_url = 'https://www.gutenberg.org/files/2638/2638-0.txt'

def get_book(url):
    # sends a http request to get the text from project Gutenberg
    raw = requests.get(url).text
    # discards the metadata from the beginning of the book
    start = re.search("\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*", raw).end()
    # discards the metadata from the end of the book
    stop = re.search("Eydkuhnen", raw).start()
    # keeps the relevant text
    text = raw[start:stop]
    return text

def preprocess(sentence):
    return re.sub('[^A-Za-z0-9.,-]+' , ' ', sentence).lower() # extract letters, numbers, comma, dot, dash

book = get_book(the_idiot_url)
processed_book = preprocess(book)
print(processed_book)

# find number of 'the'
len(re.findall('the', processed_book))

# convert i to I (space i space)
processed_book = re.sub('\si\s', " I ", processed_book)

# words with --
re.findall('[a-zA-Z0-9]*--[a-zA-Z0-9]*', processed_book)