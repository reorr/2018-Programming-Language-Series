from sly import Lexer
from sys import *

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    IF = r'UPAMI'
    THEN = r'SATULUNYA '
    ELSE = r'SEDANGKEUN'
    FOR = r'KEUR'
    FUN = r'FUN'
    TO = r'KA'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

def open_file(filename):
    data = open(filename, "r").read()
    return data

if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    if len(argv) > 1:
        data = open_file(argv[1])
        lex = lexer.tokenize(data)
        for token in lex:
            print(token)
    else:
        while True:
            try:
                text = input('sundalang » ')
            except EOFError:
                break
            if text:
                lex = lexer.tokenize(text)
                for token in lex:
                    print(token)
