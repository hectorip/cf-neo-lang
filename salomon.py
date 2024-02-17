class Program:
    def __init__(self, *expr):
        self.instructions = expr

    def __repr__(self):
        # return "".join(f"{self.instructions}") or ""
        return "\n".join([repr(expr) for expr in self.instructions]) or ""


class BinaryOperation:
    def __init__(self, operation,left_side, right_side):
        self.operation = operation
        self.left_side = left_side
        self.right_side = right_side

    def __repr__(self):
        return f"{self.left_side} {self.operation} {self.right_side}"


class VariableName:
    def __init__(self, literal_name):
        self.name = literal_name
    
    # Add __repr__ method to VariableName
    def __repr__(self):
        return self.name

programa_1 = Program(
    BinaryOperation("=", VariableName("a1"), 8),
    BinaryOperation("=", VariableName("a2"), 9),
    BinaryOperation(
        "=",
        VariableName("resultado"),
        BinaryOperation("+", VariableName("a1"), VariableName("a2"))
    )
)
print(programa_1)