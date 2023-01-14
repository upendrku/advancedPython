import sys
import getopt

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(message)

# to execute above type <python3 argument_parsing.py test.txt Hello\ World!> in terminal

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message"])
# f for filename, m for message
print(opts)
print(args)

# to execute above type <python3 argument_parsing.py -f test.txt -m Hello\ World!> in terminal
# opts output as [('-f', 'test.txt'), ('-m', 'Hello World!')]
# args output as []

