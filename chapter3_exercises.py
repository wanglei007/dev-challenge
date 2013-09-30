# Exercises for chapter 3:

# Name: Lei Wang

# EX3.1
# will get "Name Error: name 'repeat_lyrics' is not defined"

# EX3.2
# will get same (correct) output as the original script

# EX3.3
def right_justify(s):
	print ' '*(70 - len(s)) + s

right_justify('allen')

# EX3.4 
def do_twice(f, v):
	f(v)
	f(v)

def print_twice(s):
	print s
	print s

print 'Now we call do_twice twice'
do_twice(print_twice, 'spam')
do_twice(print_twice, 'spam')

def do_four(f, v):
	do_twice(f,v)
	do_twice(f,v)

print 'Now we call do_four'
do_four(print_twice, 'spam')	

