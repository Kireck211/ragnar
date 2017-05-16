import re

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