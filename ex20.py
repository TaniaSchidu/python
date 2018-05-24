# The readline() function returns the \n that's in the file at the end of that line.
# This means that print's \n is being added to the one already returned by readline().
# To change this behavior simply add a , (comma) at the end of print so that it doesn't print its own \n.
# ****************************************************************************************
# Inside readline() is a code that scans each byte of the file until it find a \n character,
# than stops reading the file to return what it found so far. The file f is responsible for maintaining 
# the current position in the file after each readline() call, so that it will keep reading each line.
from sys import argv

script, input_file = argv
# se definsete functia print_all care are argumentul f
def print_all(f):
    # citeste si apoi printeaza continutul paramterului f
    print f.read()
# se defineste functia rewind cu argumentul f
def rewind(f):
    # the function seek() is dealing in bytes, not with lines
    # So that's going to the 0 byte (first byte) in the file.
    # when you open a file the system points to the beginning of the file.
    # Any read or write you do will happen from the beginning.
    # A seek() operation moves that pointer to some part of the file so you 
    # can read or write at that place.
    # 0: means your reference point is the beginning of the file
    # 1: means your reference point is the current file position
    # 2: means your reference point is the end of the file
    # Each time you do f.seek(0) you'ar moving to the start of the file 
    f.seek(0)

def print_a_line(line_count, f):
    # print the line number 
    # and read a line from the file f 
    # and move the read head to right after the /n that ends that file
    print line_count, f.readline()
    # print line_count, f.readline(), - printeaza fiecare linie fara a adauga new linw (\n)
    # deoarece am adaugat virgula la sfarsitul functiei print

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)