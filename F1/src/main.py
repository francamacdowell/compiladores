from lexer.Lexer import Lexer

def main():

    # Read the current source code
    content = ""
    with open('test.f1', 'r') as file:
        content = file.read()

    # Call lexer with the Source Code
    lex = Lexer(content)
    # Now get the Tokens
    tokens = lex.tokenize()
    #
    # # Start Parser Phase:
    # parse = Parser(tokens)
    # parse.parse()

main()