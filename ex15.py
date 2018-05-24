#argv is a list defined in sys module.
#import the argv list from the sys module
from sys import argv
#here argv is a list that is expected to contain 2 values:
#the script name and an argument;
#assign argv the value of script and filename from the command line
script, filename = argv
#deschide fisierul indicat ca argument in linia de comanda 
txt = open(filename)
#printeaza textul din ghilimele 
print "Here's your file %r:" % filename
#cisteste si printeraza fisierul deschis
print txt.read()
#printeaza textul din ghilimele
print "Type the filename again:"
#atribue variabilei file_again denumirea fisierului introdus in linia de comanda
file_again = raw_input("> ")
#deschide fisierul introdus in linia de comanda
txt_again = open(file_again)
#cisteste si printeraza fisierul deschis
print txt_again.read()