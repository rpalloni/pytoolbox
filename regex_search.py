'''
parse strings according to patterns and mini-language
https://docs.python.org/3.8/library/re.html
https://docs.python.org/3.8/howto/regex.html
https://regex101.com/
special character escape \
'''

# std fn
s = 'foo123bar'
'123' in s
s.find('123')
s.index('123')

import re
# re.search(<regex>, <string>)

re.search('123', s) # match object
s[3:6]

##########################################
### metacharacters and character class ###
##########################################

# [set/range of characters to match]
re.search('[0-9][0-9][0-9]', s) # string contains any three consecutive decimal digit
re.search('[0-9][0-9][0-9]', 'foo456bar')
re.search('[0-9][0-9][0-9]', '234baz')
re.search('[0-9][0-9][0-9]', 'qux678')
print(re.search('[0-9][0-9][0-9]', '12foo34'))
re.search('ba[artz]', 'foobarqux')
re.search('ba[artz]', 'foobazqux')
re.search('[a-z]', 'FOObar')
re.search('[^0-9]', '12345foo')

# (.) dot
re.search('1.3', s) # any single character except a newline
re.search('foo.bar', 'fooxbar')
print(re.search('foo.bar', 'foo\nbar'))

# (|) pipe
re.search('foo|bar|baz', 'bar')
re.search('foo|bar|baz', 'baz')
re.search('foo|grault', 'foograult') # lazy: the shortest possible match


# word and non-word
# \w [a-zA-Z0-9_]
# \W [^a-zA-Z0-9_]
re.search('\w', '#(.a$@&')
re.search('[a-zA-Z0-9_]', '#(.a$@&')
re.search('\W', 'a_1*3Qb')
re.search('[^a-zA-Z0-9_]', 'a_1*3Qb')

# digit and non-digit
# \d
# \D
re.search('\d', 'abc4def')
re.search('\D', '234Q678')

# space and non-space
# \s
# \S
re.search('\s', 'foo\nbar baz')
re.search('\S', '  \n foo  \n  ')

# any digit or word or whitespace character
re.search('[\d\w\s]', '---3---')
re.search('[\d\w\s]', '---a---')
re.search('[\d\w\s]', '--- ---')

# backslash to escape
re.search('.', 'foo.bar')
re.search('\.', 'foo.bar')
s = 'foo\bar'
s = r'foo\bar'
re.search(r'\\', s)

#######################################################################################
### anchors - dictates a particular location in the string where a match must occur ###
#######################################################################################
# beginning: ^ \A
re.search('^foo', 'foobar')
re.search('\Afoo', 'foobar')
print(re.search('^foo', 'barfoo'))

# end: $ \Z
re.search('bar$', 'foobar')
re.search('bar\Z', 'foobar')
print(re.search('bar$', 'barfoo'))
re.search('bar$', 'foobar\n') # newline ignored

# beginning or end of word: \b
re.search(r'\bbar', 'foo bar')
re.search(r'\bbar', 'foo.bar')
print(re.search(r'\bbar', 'foobar'))
re.search(r'foo\b', 'foo bar')
re.search(r'foo\b', 'foo.bar')
print(re.search(r'foo\b', 'foobar'))
re.search(r'\Bfoo\B', 'barfoobaz') # \B not

########################################################################
### quantifiers - dictates how many times a regex portion must occur ###
########################################################################
# greedy: the longest possible match
# zero or many: *
re.search('foo-*bar', 'foobar')     # Zero dashes
re.search('foo-*bar', 'foo-bar')    # One dash
re.search('foo-*bar', 'foo--bar')   # Two dashes
re.search('foo.*bar', '# foo $qux@grault % bar #') # everything between

# one or many: +
print(re.search('foo-+bar', 'foobar'))   # Zero dashes
re.search('foo-+bar', 'foo-bar')         # One dash
re.search('foo-+bar', 'foo--bar')        # Two dashes

# zero or one: ?
re.search('foo-?bar', 'foobar')                     # Zero dashes
re.search('foo-?bar', 'foo-bar')                    # One dash
print(re.search('foo-?bar', 'foo--bar'))            # Two dashes

# lazy: the shortest possible match
# *?
re.search('<.*>', '%<foo> <bar> <baz>%')
re.search('<.*?>', '%<foo> <bar> <baz>%')
# +?
re.search('<.+>', '%<foo> <bar> <baz>%')
re.search('<.+?>', '%<foo> <bar> <baz>%')
# ??
re.search('ba?', 'baaaa')
re.search('ba??', 'baaaa')


re.match('foo[1-9]*bar', 'foobar')
re.match('foo[1-9]*bar', 'foo42bar')
print(re.match('foo[1-9]+bar', 'foobar'))
re.match('foo[1-9]+bar', 'foo42bar')
re.match('foo[1-9]?bar', 'foobar')
print(re.match('foo[1-9]?bar', 'foo42bar'))

# {m} m repetitions of the regex
print(re.search('x-{3}x', 'x--x'))                # Two dashes
re.search('x-{3}x', 'x---x')                      # Three dashes
print(re.search('x-{3}x', 'x----x'))              # Four dashes

# {m,n} any number of repetitionsfrom m to n
for i in range(1, 6):
    s = f"x{'-' * i}x"
    print(f'{i}  {s:10}', re.search('x-{2,4}x', s))

re.search('x{}y', 'x{}y') # omit m,n to match literally
re.search('x{ffffff}y', 'x{ffffff}y')
re.search('a{3,5}', 'aaaaaaaa')
re.search('a{3,5}?', 'aaaaaaaa')


############################################################
### groups - a single syntactic entity ( subexpression ) ###
############################################################
re.search('(bar)', 'foo bar baz bar')
re.search('(bar)+', 'foo bar baz')
re.search('(bar)+', 'foo barbar baz')
re.search('(bar)+', 'foo barbarbarbar baz')
re.search('(foo|bar|baz)+', 'foofoofoo') # sequence of one or more foo or bar or baz
re.search('([0-9]+|[a-z]+)', '456') # sequence of one or more decimal digit or char
re.search('([0-9]+|[a-z]+)', 'ffda')
re.search('(ba[rz]){2,4}(qux)?', 'bazbarbazqux')
re.search('(ba[rz]){2,4}(qux)?', 'barbar')
re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar')
re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar123')
re.search('(foo(bar)?)+(\d\d\d)?', 'foofoo123')

# m.groups() returns a tuple containing all the captured groups from a regex match
m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
m.groups()
m.group(2)

m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz') # named groups (?P<name><regex>)
m.group('w3')

# not captured
m = re.search('(\w+),(?:\w+),(\w+)', 'foo,quux,baz')
m.groups()
m.group(2)

######################################################################
### conditional match - if regex match, statement1 else statement2 ###
######################################################################
# (?(<n>)<yes-regex>|<no-regex>) if a group numbered <n> exists
# (?(<name>)<yes-regex>|<no-regex>) if a group named <name> exists

r = '^(###)+foo(?(1)bar|baz)' # ^(###)+ = if begin with one or many '###' => create group numbered 1 => add 'bar'
re.search(r, '###foobar')
re.search(r, '######foobar')
re.search(r, '######foobaz') # else

p = '^(?P<char>\W)?foo(?(char)(?P=char)|)$' # single non-word character + foo + same single non-word character | empty
# ^ at string beginning
# (?P<char>\W) single non-word character, captured in a group named char
# (?P<char>\W)? zero or one occurrence of the above
# foo string 'foo'
# (?(char)(?P=char)|'empty') contents of the group named char if it exists, or the empty string if it doesn’t
# $ end of the string

# if a non-word character precedes 'foo', then the parser creates a group named char which contains that character.
# the same character must also follow 'foo' for the entire match to succeed.
# if 'foo' isn’t preceded by a non-word character, then the parser doesn’t create group char
# <no-regex> is the empty string, which means there must not be anything following 'foo'

re.search(p, 'foo')
re.search(p, '#foo#')
re.search(p, '@foo@')
print(re.search(p, '#foo'))
print(re.search(p, 'foo@'))
print(re.search(p, '#foo@'))
print(re.search(p, '@foo#'))

##############################################################################################
### lookahead and lookbehind - match what is behind (left) or ahead (right) of the parser ####
##############################################################################################
re.search('foo(?=bak)', 'foobak')
re.search('foo(?=[a-z])', 'foobak') # what follows 'foo' must be [a-z] and is not returned in the match
print(re.search('foo(?=[a-z])', 'foo123'))

print(re.search('foo(?![a-z])', 'foobar')) # negative lookahead
re.search('foo(?![a-z])', 'foo123')

re.search('(?<=[a-z])bar', 'foobar') # what precedes 'bar' must be [a-z] and is not returned in the match
print(re.search('(?<=qux)bar', 'foobar'))

print(re.search('(?<!foo)bar', 'foobar'))
re.search('(?<!qux)bar', 'foobar')

re.search('(?<=a+)def', 'aaadef') # error: length of the string matched is indeterminate


#############################################
### flags - modify regex parsing behavior ###
#############################################
# case-insensitive: re.IGNORECASE
re.search('a+', 'aaaAAA')
re.search('a+', 'aaaAAA', re.I)

# match embedded \n: re.MULTILINE
s = 'foo\nbar\nbaz'
print(s)
re.search('foo$', s, re.M)
re.search('bar$', s, re.M)
re.search('baz$', s, re.M)

# dot match a \n: re.DOTALL
re.search('foo.bar', 'foo\nbar', re.S)

# include space: re.VERBOSE
re.search('foo bar', 'foobar', re.VERBOSE)

# debug info: re.DEBUG
re.search('foo.bar', 'fooxbar', re.DEBUG)

# encoding: re.ASCII re.UNICODE re.LOCALE