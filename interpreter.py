from sys import argv
from bottomUp.bottomUpParser import *

script, filename = argv

def main():
	inputString = ""
	with open(filename, 'r') as input_file:
		for line in input_file:
			inputString += line.replace('\n', '');
	algorithm(inputString)

main()