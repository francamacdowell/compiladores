class Parser(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def parse(self):

        while self.token_index < len(self.tokens):
            # Get token type e.g.: INTEGER
            token_type = self.tokens[self.token_index][0]
            # Get token value e.g: 7
            token_value = self.tokens[self.token_index][1]

            print(token_type, token_value)

            self.token_index += 1