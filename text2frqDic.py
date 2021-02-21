# this is a script which converts a text into a frequency dictionary
"""
my first python script
     @ilaria
"""
import sys, re, os

FileInput = open(sys.argv[1],'r')

for Line in FileInput:
    Line = re.sub('<.*?>', '', Line)
    Line = Line.lower()
    Line = Line.strip()
    ListOfWords = re.split('[ ,\.:;\!\(\)\"\[\]]+', Line)
    sys.stdout.write( str( ListOfWords ) + '\n')

