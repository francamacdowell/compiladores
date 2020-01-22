from Objects.varObject import VariableObject

class Parser(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0
        self.transpiled_code = ""

    def parse(self):

        while self.token_index < len(self.tokens):
            # Get token type e.g.: INTEGER
            token_type = self.tokens[self.token_index][0]
            # Get token value e.g: 7
            token_value = self.tokens[self.token_index][1]

            if token_type == "VAR_DECLARATION" and token_value == "var":
                self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])

            self.token_index += 1
        print(self.transpiled_code)

    def parse_variable_declaration(self, token_stream):

        tokens_checked = 0

        name = ""
        operator = ""
        value = ""

        for token in range(0, len(token_stream)):
            # Get token type e.g.: INTEGER
            token_type = token_stream[tokens_checked][0]
            # Get token value e.g: 7
            token_value = token_stream[tokens_checked][1]

            # If the STATEMENT_END token is found, break out of loop
            if token_type == "STATEMENT_END":
                break


            elif token == 1 and token_type == 'IDENTIFIER':
                name = token_value
            elif token == 1 and token_type != 'IDENTIFIER':
                print("ERROR: Invalid variable name '" + token_value + "'")
                quit()

            # This will get an assignment operator
            elif token == 2 and token_type == 'OPERATOR':
                operator = token_value
            elif token == 2 and token_type != 'OPERATOR':
                print("ERROR: Assignment  Operator is missing or invalid, should be '='")
                quit()

            # This will get the variable value assigned:
            elif token == 3 and token_type in ['STRING', 'INTEGER', 'IDENTIFIER']:
                value = token_value
            elif token_type == 3 and token_type not in ['STRING', 'INTEGER', 'IDENTIFIER']:
                print("Invalid variable assignment value '" + token_value + "'")
                quit()

            tokens_checked += 1

        self.token_index += tokens_checked
        varObj = VariableObject()
        self.transpiled_code += varObj.transpile(name, operator, value)