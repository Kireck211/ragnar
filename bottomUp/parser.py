from lexicalAnalysis.lexicalAnalyzer import *

class Parser(object):
	def __init__(self, pattern):
		self.tokenizer = Token(pattern)

	def parseInput(self, text):
		tokens = []
		for tupleToken in self.tokenizer.tokenizeText(text):
			if (tupleToken[0] == 'identifier'):
				tokens.append(InputToken('ID', tupleToken[1]))
			elif (tupleToken[0] == 'number'):
				tokens.append(InputToken('NUMBER', int(tupleToken[1])))
			elif (tupleToken[0] == 'float'):
				tokens.append(InputToken('NUMBER', float(tupleToken[1])))
			elif (tupleToken[0] == 'string'):
				tokens.append(InputToken('STRING', tupleToken[1].replace('"', '').replace("'", '')))
			elif (tupleToken[0] == 'epsilon'):
				tokens.append(InputToken(tupleToken[1], ''))
			elif (tupleToken[0] == 'whitespace'):
				continue
			else:
				tokens.append(InputToken(tupleToken[1],tupleToken[1]))
		tokens.append(InputToken('$'))
		return tokens

class InputToken(object):
	def __init__(self, lexeme, value = None):
		self.lexeme = lexeme
		self.value = value
	
	def __str__(self):
		return self.lexeme
