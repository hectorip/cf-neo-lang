class Program():
  def __init__(self, *expr) -> None:
    self.instructions = expr

  def __repr__(self):
    return "".join(f"{self.instructions}") or ""

class BinaryOp():
  def __init__(self, op, left, right):
    self.op = op
    self.left = left
    self.right = right
  
  def __repr__(self):
    return f"{self.left} {self.op} {self.right}"

class VarName():
  def __init__(self, literal):
    self.name = literal
  
  def __repr__(self):
    return f"{self.name}"

"""
var a1 = 8
var a2 = 9
var resultado = a1 + a2

"""

program1  = Program(
  BinaryOp('=', VarName('a'), 9),
  BinaryOp('=', VarName('b'), 8),
  BinaryOp('=', 
    VarName('resultado'), 
    BinaryOp("+", VarName("a"), VarName("b"))
  )
)

print(program1)