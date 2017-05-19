import re

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

class TokenizerException(Exception): pass

class Token(object):
    def __init__(self,pattern): 
        self.token_re = re.compile(pattern, re.VERBOSE)

    def tokenizeText(self, text):
        position = 0
        tokens = []
        while True:
            result = self.token_re.search(text, position)
            if not result: break
            position = result.end()
            token_group = result.lastgroup
            token_value = result.group(token_group)
            tokens.append((token_group, token_value))
        if position != len(text):
            raise TokenizerException('Tokenizer stopped at position {} of {} from {}'.format(position, len(text), text))
        return tokens