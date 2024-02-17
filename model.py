"""
Modelo de datos del compilador
AST = Abstract Syntax Tree
Representación de un programa mediante una estructura de datos

var mi_variable = 8
var variable_2 = 7

mi_variable + variable_2

EXPR
STATEMENTS

int numero = numero_2 = 9;

         =

numero         =

        numero_2      9




                    EXPR
              /                 \
            /                     \
        EXPR                               EXPR
     /        \                        /         \
TYPE           NAME                EXPR             LITERAL
 |               |              /      \               |
(int)          (numero)      TYPE       NAME           9

"""

"""var mi_variable = 8"""

class Program():
    def __init__(self, *expr):
        self.instructions = expr
    def __repr__(self):
        instructions_as_str = [str(i) for i in self.instructions]
        return "\n".join(instructions_as_str)
    def exec(self, context={}):
        for inst in self.instructions:
            inst.exec(context)
        print(context)

class VariableName(): # VARIABLE
    def __init__(self, literal_name):
        self.name = literal_name
    def __repr__(self):
        return f"var {self.name}"
    def exec(self, context):
        context[self.name] = None

class BinaryOperation():
    def __init__(self, operation,left_side, right_side):
        self.operation = operation
        self.left_side = left_side
        self.right_side = right_side
    def __repr__(self):
        return f"{self.left_side} {self.operation} {self.right_side}"
    def exec(self, context):
        if self.operation == "=":
            # Del lado izquierdo sólamente puede ir una inicialización
            # o un nombre de variable
            # 0 = 9
            context[self.left_side.name] = self.right_side.exec()

class Name(): # IDENTIFIER 
    def __init__(self, literal_name):
        self.name = literal_name
    def __repr__(self):
        return self.name
    def exec(self, context):
        return context[self.name]


class Integer()
"""
suma 9 + 8      v1 + v2
resta
multiplicación
división



var a1 = 8
var a2 = 9
var resultado = a1 + a2

"""

programa_1 = Program(
    BinaryOperation("=", VariableName("a1"), 8),
    BinaryOperation("=", VariableName("a2"), 9),
    BinaryOperation(
        "=",
        VariableName("resultado"),
        BinaryOperation("+", Name("a1"), Name("a2"))
    )
)

print(programa_1)
print("Resultado")
programa_1.exec()

"""
DEFINIR PRECEDENCIA DE OPERACIONES
* /
+ -

var a1 = 8
var a2 = 9
var resultado = a1 * 8 + a2 * 9
"""

programa_2 = Program(
    BinaryOperation("=", VariableName("a1"), 8),
    BinaryOperation("=", VariableName("a2"), 9),
    BinaryOperation(
        "=",
        VariableName("resultado"),
        BinaryOperation("+", 
                        BinaryOperation("*", Name("a1"), 8),
                        BinaryOperation("*", Name("a2"), 9))
    )
)

# print(programa_2)


p3 = Program(
    BinaryOperation("=", VariableName("a1"), 8),
    BinaryOperation("=", VariableName("a2"), 9),
    BinaryOperation(
        "=",
        VariableName("resultado"),
        BinaryOperation(
            "+",
            BinaryOperation("*", Name("a1"), Name("a1")),
            BinaryOperation(
                "-",
                BinaryOperation("*", Name("a2"), Name("a2")),
                BinaryOperation("/", Name("a1"), Name("a2"))
            )
        )
    )
)

# print(p3)



