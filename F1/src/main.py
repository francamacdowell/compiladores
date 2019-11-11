from F1.src.lexer.Lexer import Lexer

def main():

    # Read the current source code
    content = ""
    with open('test.f1', 'r') as file:
        content = file.read()

    # Call lexer with the Source Code
    lex = Lexer(content)
    # Now create Tokens
    tokens = lex.tokenize()


main()