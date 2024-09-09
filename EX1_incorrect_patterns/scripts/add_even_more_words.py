import sys
import subprocess

def add_content_to_line(input_filename):
    f = open(input_filename, "r")
    line = f.readline()
    print("%s This sentence was added at the last stage." % (line[:-1]))

add_content_to_line(sys.argv[1])
