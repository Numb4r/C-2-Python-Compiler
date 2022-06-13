import const

class Token:
    def __init__(self,tipo,lexeme=None,valor=None):
        self.tipo = tipo
        self.lexeme = lexeme
        self.valor = valor
        
    def __str__(self):
        string = "<"+str(self.tipo)
        string += ","+self.lexeme if self.lexeme != None else ""
        string += ","+self.valor if self.lexeme != None and self.valor !=None else ""
        string += ">"
        return string
def validateTKHEAD(token:Token):
    print(token.valor)
    if token.lexeme == "include":
        return re.match("<.*>|\".*\"",token.valor)