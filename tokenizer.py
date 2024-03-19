
# Neo
# INT : 123, 78, 8, 9
# VAR : 'var'
# OP : +, -, *, /
# PLUS: +
# MINUS: -
# MULT: *
# DIV: /
# EQUAL: =

# 8 + 9
# TOKEN(INT, 8, 1, 1)
# TOKEN(OP, '+', 1, 3)
# TOKEN(INT, 9, 1, 5)
#
# var mi_variable = 9
# TOKEN(VAR, 'var', 1, 1)
# [8, 9, 9]
# TOKEN(LEFT_SBRACKET, '[')
# INT
# TOKEN COMA
# INT
# TOKEN COMA

class Token:
    def __init__(self, kind, value, line, column):
        self.type = kind
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        pass

def parse(program):
    ## Un programa es un conjunto de líneas
    tokens = []
    for line in program:
        parse_line(line)
    # Leer el programa linea por linea
    # Emitir tokens por cada unidad syntactito
    # Poner todos los tokens en una colección

def parse_line(line):
    column = 0
    current_value = '' 
    for c in line:
        if c in 'O'


