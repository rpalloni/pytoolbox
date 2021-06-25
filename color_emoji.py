import emoji

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
print(emoji.demojize('Python is 👍'))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))


# ASCII color codes
COLOR = {
    'blue': '\033[94m',
    'grey': '\033[90m',
    'yellow': '\033[93m',
    'black': '\033[90m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'red': '\033[91m',
    'default': '\033[0m' # close
}

# ANSI color codes
ANSI_COLOR = {
    # 0: normal
    'black': '\033[0;30m',
    'red': '\033[0;31m',
    'green': '\033[0;32m',
    'yellow': '\033[0;33m',
    'blue': '\033[0;34m',
    'purple': '\033[0;35m',
    'cyan': '\033[0;36m',
    'gray': '\033[0;37m',
    # 1: bold
    'b_gray': '\033[1;30m',
    'b_red': '\033[1;31m',
    'b_green': '\033[1;32m',
    'b_yellow': '\033[1;33m',
    'b_blue': '\033[1;34m',
    'b_purple': '\033[1;35m',
    'b_cyan': '\033[1;36m',
    'white': '\033[1;37m',
    # 4: underline
    'u_gray': '\033[4;30m',
    'u_red': '\033[4;31m',
    'u_green': '\033[4;32m',
    'u_yellow': '\033[4;33m',
    'u_blue': '\033[4;34m',
    'u_purple': '\033[4;35m',
    'u_cyan': '\033[4;36m',
    'u_white': '\033[4;37m',
    # background
    'g_black': '\033[0;40m',
    'g_red': '\033[0;41m',
    'g_green': '\033[0;42m',
    'g_yellow': '\033[0;43m',
    'g_blue': '\033[0;44m',
    'g_purple': '\033[0;45m',
    'g_cyan': '\033[0;46m',
    'g_white': '\033[0;47m',
}

SCHEMA = ANSI_COLOR
for (k, v) in SCHEMA.items():
    print(v + k)


class format:
    OFF = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_with_color(message, color='red'):
    print(COLOR.get(color) + message + COLOR.get('default'))

def print_with_format_b(message):
    print(f"{format.BOLD}" + message + f"{format.OFF}")

def print_with_format_u(message):
    print(f"{format.UNDERLINE}" + message + f"{format.OFF}")

'''
print_with_color('hello colorful world!')
print_with_color('hello colorful world!', 'blue')
print_with_color('hello colorful world!', 'magenta')

print_with_format_b('hello world!')
print_with_format_u('hello world!')
'''