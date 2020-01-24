import re

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):

        # all tokens created by lexer will be stored here:
        tokens = []

        # Create a word list of the source code
        source_code = self.source_code.split()

        # This will track the index we are at the source code
        source_index = 0

        # Loop through the each word from the source code
        while source_index < len(source_code):
            word = source_code[source_index]

            if word == 'var':
                tokens.append(['VAR_DECLARATION', word])

            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[len(word) - 1] == ';':
                    # check and add if token is identifier after assign ('=')
                    tokens.append(['IDENTIFIER', word[0:len(word) - 1]])
                else:
                    # add identifier token
                    tokens.append(['IDENTIFIER', word])

            elif re.match('[0-9]', word):
                if word[len(word) - 1] == ';':
                    tokens.append(['INTEGER', word[0:len(word) - 1]])
                else:
                    tokens.append(['INTEGER', word])

            elif word in "=":
                tokens.append(['ASSIGN_OPERATOR', word])

            elif word in "==":
                tokens.append(['EQUAL_COMPARE_OPERATOR', word])

            elif word in "/":
                tokens.append(['DIV_OPERATOR', word])

            elif word in "*":
                tokens.append(['MULT_OPERATOR', word])

            elif word in "-":
                tokens.append(['SUB_OPERATOR', word])

            elif word in "+":
                tokens.append(['SUM_OPERATOR', word])

            elif word in "%":
                tokens.append(['MOD_OPERATOR', word])

            elif word in "//":
                tokens.append(['MOD_INT_OPERATOR', word])

            # If a STATEMENT_END (;) is found, add STATEMENT_END token:
            if word[len(word) - 1] == ';':
                tokens.append(['STATEMENT_END', ';'])
            source_index += 1

        print(tokens)
        return tokens