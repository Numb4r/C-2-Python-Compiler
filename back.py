import re
from scanner import Scanner
from semanticTrees import _typeDeclaration as typeId
from semanticTrees import _typeAssignment as typeAss 
from semanticTrees import _typeToKw as typeToKw
from const import TypeToken as tt
_KWToStr = {
    tt.TK_KWINT:"int",
    tt.TK_KWFLOAT:"float",
    tt.TK_KWFOR:"for",
    tt.TK_KWIF:"if",
    tt.TK_KWELSE:"else",
    tt.TK_KWRETURN:"return",
}
_mathToStr = {
    tt.TK_OPSUM:"+",
    tt.TK_OPSUB:"-",
    tt.TK_OPDIV:"/",
    tt.TK_OPMULT:"*",
    tt.TK_OPMOD:"%"
}
_opToStr = {
    tt.TK_OPGT:">",
    tt.TK_OPLT:"<",
    tt.TK_OPEQ:"==",
    tt.TK_OPNEQ:"!="
}
_literals = [tt.TK_INTEGER,tt.TK_STRINGLITERAL,tt.TK_FLOATINGPOINT]
_kw = [tt.TK_KWIF,tt.TK_KWFOR,tt.TK_KWELSE,tt.TK_KWRETURN]
class Back:
    def __init__(self,sc:Scanner):
        self.sc = sc 
        self.sc.resetPos()
        self.code = ""
        self.identation = 0        
    def addIdentation(self):
        self.identation+=1
    def removeIdentation(self):
        self.identation-=1
    def applyIdentation(self):
        self.code+=str(self.identation*"    ")
    def transpile(self):
        
        declaredVarsinFunctions = {}
        functionAtual = None
        token = self.sc.nextToken()
        typeDeclaration = None
        identifierName = ""
        argsIdentifier = []
        functionScope=""
        beginArgs=False
        beginCallFunction = False
        beginIdentifierDeclaration = False
        while token != None:
            if token.tipo in typeId:
                typeDeclaration = token.tipo 
                beginIdentifierDeclaration = True
            elif token.tipo is tt.TK_IDENTIFIER:
                if beginArgs:
                    argsIdentifier.append(token.lexeme)
                else:
                    identifierName = token.lexeme 
                print(" ",token.lexeme)
            elif token.tipo is tt.TK_BRACESOPEN:
                
                if typeDeclaration is not None:
                    self.code+="def "
                    self.code+=identifierName
                    self.code +="("
                    self.code+=",".join(argsIdentifier)
                    self.code+=")"
                    argsIdentifier = []
                    typeDeclaration = None 
                    declaredVarsinFunctions[identifierName] = {}
                    functionScope=identifierName
                    identifierName = ""
                    self.code+=":\n"
                    self.addIdentation()
                    self.applyIdentation()
            elif token.tipo is tt.TK_PARENTHESESOPEN or token.tipo is tt.TK_OPASSIGNMENT:
                beginArgs = True
                if token.tipo is tt.TK_PARENTHESESOPEN and beginIdentifierDeclaration == False:
                    beginCallFunction = True
            elif token.tipo is tt.TK_PARENTHESESCLOSE:
                beginArgs = False
            # elif token.tipo is tt.TK_OPSEPARATOR and beginIdentifierDeclaration and functionScope != '':
            #     self.code+=identifierName
            #     if typeDeclaration is not None:
            #         typeVar= _KWToStr.get(typeDeclaration)
            #         self.code +=" = "
            #         self.code+=str(typeVar)
            #         self.code+="("
            #         declaredVarsinFunctions[functionScope][identifierName] = typeVar
            #     if len(argsIdentifier) > 0:
            #         self.code+="".join(argsIdentifier)
            #         argsIdentifier = []
            #     if typeDeclaration is not None:
            #         self.code+=")\n"
                # self.applyIdentation()
                
            elif token.tipo in _literals and beginArgs:
                argsIdentifier.append(token.lexeme)
            elif token.tipo in _literals:
                self.code+=token.lexeme
            elif token.tipo in _mathToStr and beginArgs:
                argsIdentifier.append(_mathToStr.get(token.tipo))
            elif token.tipo is tt.TK_BRACESCLOSE:
                self.removeIdentation()
                self.code += "\n"
                self.applyIdentation()
                print(self.identation)
                functionAtual = None
            elif token.tipo in _kw :
                self.code+=_KWToStr.get(token.tipo)+" "
            elif token.tipo in _opToStr:
                argsIdentifier.append(_opToStr.get(token.tipo))
            elif token.tipo is tt.TK_OPEOL:
                beginArgs = False
                if identifierName != "":
                    if beginCallFunction:
                        beginCallFunction = False
                        # print(argsIdentifier)
                        if identifierName == "scanf":
                            var = argsIdentifier[1]
                            self.code+=var+" = "
                            typeOfVar = declaredVarsinFunctions[functionScope][var]
                            self.code+=typeOfVar+"(input())"
                        elif identifierName == "printf":
                            print(argsIdentifier)
                            self.code+="print("
                            self.code+=argsIdentifier[0]
                            if len(argsIdentifier) > 1:
                                self.code+="%("
                                self.code+=",".join(argsIdentifier[1:])
                                self.code+=")"
                            self.code+=")"
                        identifierName = ""
                        typeDeclaration = None 
                        argsIdentifier = []
                        pass
                    else:
                        self.code+=identifierName
                        if typeDeclaration is not None:
                            typeVar= _KWToStr.get(typeDeclaration)
                            self.code +=" = "
                            self.code+=str(typeVar)
                            self.code+="("
                            declaredVarsinFunctions[functionScope][identifierName] = typeVar
                        if len(argsIdentifier) > 0:
                            self.code+="".join(argsIdentifier)
                            argsIdentifier = []
                        if typeDeclaration is not None:
                            self.code+=")"
                        typeDeclaration = None 
                        identifierName = ""
                        beginIdentifierDeclaration = False
                self.code+="\n"
                self.applyIdentation()
            token = self.sc.nextToken()
        f = open("out/toPy.py","w")
        f.write(self.code)
        f.close()
