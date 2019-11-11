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
            print(source_code[source_index])

            source_index += 1

        #return created tokens
        return tokens
