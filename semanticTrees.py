from const import TypeToken as tt
from Token import Token
from enum import Enum,auto 
from scanner import Scanner

_typeDeclaration = [
    tt.TK_KWINT,
    tt.TK_KWCONST,
    tt.TK_KWCHAR,
    tt.TK_KWDOUBLE,
    tt.TK_KWSHORT,
    tt.TK_KWLONG,
    tt.TK_KWFLOAT,
    tt.TK_KWUNSIGNED,
    tt.TK_KWSIGNED,
    tt.TK_KWVOID,
]
_typeValue=[
    tt.TK_IDENTIFIER,
    tt.TK_INTEGER,
    tt.TK_FLOATINGPOINT,
    tt.TK_CHARLITERAL,
    tt.TK_STRINGLITERAL,
]
_typeOperation =[
    tt.TK_OPSUM,
    tt.TK_OPSUB,
    tt.TK_OPMULT,
    tt.TK_OPDIV,
    tt.TK_OPMOD,
    tt.TK_OPINC,
    tt.TK_OPDEC,
]
_typeAssignment =[
    tt.TK_OPASSIGNMENT,
]
_typeConvert={
    tt.TK_KWINT : tt.TK_INTEGER,
    tt.TK_KWFLOAT : tt.TK_FLOATINGPOINT,

}
_typeAcceptance={
    tt.TK_KWINT:[tt.TK_KWINT,tt.TK_KWDOUBLE,tt.TK_FLOATINGPOINT,tt.TK_KWCHAR],
    tt.TK_KWFLOAT:[tt.TK_KWFLOAT,tt.TK_KWINT],
    tt.TK_KWDOUBLE:[tt.TK_KWDOUBLE,tt.TK_KWFLOAT,tt.TK_KWINT],
    tt.TK_STRINGLITERAL:[]
}

_typeToKw ={
    tt.TK_INTEGER : tt.TK_KWINT,
    tt.TK_FLOATINGPOINT: tt.TK_KWDOUBLE,
    # tt.TK_STRINGLITERAL : [tt.TK_KWCONST,tt.TK_KWCHAR,tt.TK_OPMULT],
    tt.TK_CHARLITERAL : tt.TK_KWCHAR
}

class Identifier:
    def __init__(self,name,type_,scope):
        self.name = name
        self.type = type_
        # print(self.type)
        # self.typeMatching = _typeAcceptance.get(self.type)
        self.scopeFather = scope
        self._valor = None
    def addValor(self,valor):
        self._valor = valor
    def __eq__(self, o):
        return self.name == o.name if o != None else False
def addValorFromLiteral(token):
    _type = _typeToKw.get(token.tipo) if _typeToKw.get(token.tipo) != None else token.tipo
    return (_type,token.lexeme)



def validateAssignment(valor):
    
    while (tt.TK_PARENTHESESOPEN,None) in valor:
        index = len(valor)+1
        pOpen = valor.index((tt.TK_PARENTHESESOPEN,None))
        pClose = valor.index((tt.TK_PARENTHESESCLOSE,None))
        resultValor = valor[pOpen+1:pClose]
        valor = validateAssignment(resultValor)
    while (tt.TK_OPMOD,None) in valor:
        index = valor.index((tt.TK_OPMOD,None))
        op = valor[index][0]
        val = validateOperations(valor[index-1],op,valor[index+1])
        valorAux = valor[index+2:]
        valor = valor[:index-1] 
        valor.append(val)
        valor+=valorAux
    while (tt.TK_OPMULT,None) in valor or (tt.TK_OPDIV,None) in valor:
        index =len(valor)+1
        if (tt.TK_OPMULT,None) in valor:
            firstMult = valor.index((tt.TK_OPMULT,None)) 
            index = firstMult if firstMult < index else index
        if (tt.TK_OPDIV,None) in valor:            
            firstMult =  valor.index((tt.TK_OPDIV,None))
            index = firstMult if firstMult < index else index
        op = valor[index][0]
        val = validateOperations(valor[index-1],op,valor[index+1])
        valorAux = valor[index+2:]
        valor = valor[:index-1] 
        valor.append(val)
        valor+=valorAux
        # print(valor)
    while (tt.TK_OPSUM,None) in valor or (tt.TK_OPSUB,None) in valor:
        
        index =len(valor)+1
        if (tt.TK_OPSUM,None) in valor:
            firstSum = valor.index((tt.TK_OPSUM,None)) 
            index = firstSum if firstSum < index else index
        if (tt.TK_OPSUB,None) in valor:            
            firstSub =  valor.index((tt.TK_OPSUB,None))
            index = firstSub if firstSub < index else index
        op = valor[index][0]
        # print("index",index)
        # print(valor[index-1],op,valor[index+1])
        # print("valor:",valor[:index-1])
        # print("valor:",valor[index+2:])
        # print("val",val)
        # print(valor[1])

        val = validateOperations(valor[index-1],op,valor[index+1])
        valorAux = valor[index+2:]
        valor = valor[:index-1] 
        valor.append(val)
        valor+=valorAux
        # print(valor)
        
        
    return valor

    
def validateOperations(valor1,operation,valor2):    
    if valor2[0] in  _typeAcceptance.get(valor1[0]) :
        if operation is tt.TK_OPDIV and float(valor1[1])== float(valor2[1])==0:
            raise BaseException("FLOATING POINT EXCEPTION: DIVISION BY 0") 
        if operation is tt.TK_OPMOD and valor1[0] ==  valor2[0] == tt.TK_KWFLOAT :
            raise BaseException("CANNOT OPERATE FLOAT%FLOAT")
        return valor1
    else:
        raise BaseException("Cannot convert ",valor2[0]," to ",valor1[0])
    
    
        
def validateValors(identifier,valor):
    
    # print("validate ",identifier.name," = ",valor)
    
    valorFinal = validateAssignment(valor)
    # print("VALOR FINAL",valorFinal)
    # # print(valorFinal)
    if valorFinal[0][0] in _typeAcceptance.get(identifier.type):
        newType= _typeAcceptance.get(identifier.type)[0]
        valorFinal = [(newType,valorFinal[0][1])]
        valorFinal = (True,valorFinal)
    else:
        valorFinal = (False,valorFinal[0][0])
    return valorFinal






class Function(Identifier):
    def __init__(self,name,typeFunc,scopeFather,scopeCreate):
        super().__init__(name,typeFunc,scopeFather)
        self.scopeCreate = scopeCreate
        self.args = []
class Variable(Identifier):
    def __init__(self,name,typeVar,scope):
        super().__init__(name, typeVar, scope)
        self.valor = []

class Scope:
    def __init__(self,idScope,name,scopeFather):
        self.id = idScope 
        self.name = name
        self.identifiers = {}
        self.scopeFather = scopeFather
    def variableInScope(self,token):
        return token in self.variables



def scopeIdentifiers(scope:Scope):
    identifiers= scope.identifiers
    while scope.scopeFather != None:
        scope = scope.scopeFather
        identifiers.update(scope.identifiers)
    return identifiers
def isIdentifierAlreadyDeclares(identifier,scope):
    if  identifier.lexeme in scopeIdentifiers(scope):
        return True
    return False
        
def getIdentinfier(identifier,scope):
    return scopeIdentifiers(scope).get(identifier.lexeme)
    
        

    

class SemanticAnalysis:

    def __init__(self,sc:Scanner):
        self.sc = sc
        self.sc.resetPos()
        self.state = 0
        self.scopeLevel = 0
        self.scope = Scope(self.scopeLevel,'global',None)
        self.globalScope = self.scope
        
        self.typeDeclaration = None
        self.identifier = None
        self.beginTypeDeclaration = False
        self.typeAssignment = None
        self.valorAssignment = []
        self.beginAssignment = False
        self.lastScopeDeclaration = 0
        self.beginIdentifierDeclaration = False
        
    def analysis(self):
        token = self.sc.nextToken()
        while token != None:
            self.analyseToken(token)
            token = self.sc.nextToken()

    def analyseToken(self,token:Token):
        
        # print(self.globalScope == self.scope)
        if token.tipo in _typeDeclaration and not self.beginAssignment:
            # self.typeDeclaration.append(token)
            self.typeDeclaration = token.tipo
            # print(self.typeDeclaration,end=" ")
            self.beginTypeDeclaration = True
            return
        if token.tipo is tt.TK_OPSEPARATOR:
            
            self.beginIdentifierDeclaration = True
            self.beginAssignment = False
            error = validateValors(self.identifier,self.valorAssignment)
            if not error[0]:
                raise "ERROR CANNOT CONVERT " + error[1] + " TO "+ self.identifier.type
            self.identifier.addValor(error[1])
            self.valorAssignment = []
            return
        if self.beginTypeDeclaration == False and token.tipo == tt.TK_OPSEPARATOR:
            self.beginTypeDeclaration = True
            return
        
        if token.tipo is tt.TK_OPEOL or ((token.tipo is tt.TK_PARENTHESESOPEN or token.tipo is tt.TK_PARENTHESESCLOSE) and not self.beginAssignment):
            # print("a")
            if self.beginAssignment and len(self.valorAssignment) > 0 and token.tipo is tt.TK_OPEOL:
                print("a",self.valorAssignment)
                error = validateValors(self.identifier,self.valorAssignment)
                if not error[0]:
                    raise BaseException("ERROR CANNOT CONVERT ", error[1], " TO ", self.identifier.type)
                self.identifier.addValor(self.valorAssignment[0])
                # print("=",self.identifier._valor,end=" ")
                # print()
                self.valorAssignment = []
                
            if token.tipo is tt.TK_PARENTHESESCLOSE:
                pass
                # print()
                # self.identifier = None   
            if token.tipo is tt.TK_OPEOL:
                # print("")
                if self.identifier != None:
                    self.scope.identifiers[self.identifier.name] = self.identifier
                self.beginAssignment = False 
                self.identifier = None   
            if token.tipo == tt.TK_PARENTHESESOPEN and not self.beginAssignment:
                # print("open")
                scopeAnt = self.scope
                self.scope = Scope(self.scopeLevel+1,str(self.scope.name+self.identifier.name), self.scope)
                self.identifier = Function(self.identifier.name, self.identifier.type, self.scope,scopeAnt)
                self.globalScope.identifiers[self.identifier.name] = self.identifier
                self.typeAssignment = []
                self.identifier = None   
            # elif self.identifier != None:
            #     self.scope.identifiers[self.identifier.name] = self.identifier
            #     self.identifier = None   
            self.beginTypeDeclaration = False
            self.typeAssignment = []
            self.typeDeclaration = None
            # self.identifier = None   
            return


        if self.beginAssignment:
            if token.tipo is tt.TK_IDENTIFIER and isIdentifierAlreadyDeclares(token,self.scope):
                print("b",getIdentinfier(token,self.scope))
                self.valorAssignment+=getIdentinfier(token,self.scope)._valor
            elif token.tipo is not tt.TK_IDENTIFIER:
                self.valorAssignment.append(addValorFromLiteral(token))
            else:
                raise BaseException("SEMANTIC ERRO: IDENTIFIER ",token.lexeme ," NOT DECLARED")
            return
       
            
        if token.tipo in _typeAssignment:
            self.beginAssignment = True
            return
        if token.tipo is tt.TK_IDENTIFIER:
            if self.beginTypeDeclaration or  self.beginIdentifierDeclaration:
                # print(token.lexeme,end=" ")
                if self.identifier != None:
                    self.scope.identifiers[self.identifier.name] = self.identifier
                self.beginTypeDeclaration = False
                self.beginIdentifierDeclaration = False
                self.beginAssignment = False
                if isIdentifierAlreadyDeclares(token, self.scope):
                    raise BaseException("SEMANTIC ERRO: IDENTIFIER "+ token.lexeme + " ALREADY DECLARED IN SCOPE")
                self.identifier = Identifier(token.lexeme, self.typeDeclaration, self.scope)
                return 
            if isIdentifierAlreadyDeclares(token,self.scope):
                self.identifier = getIdentinfier(token,self.scope)
                # print(self.identifier.name,end=" ")
            else:
                raise BaseException("SEMANTIC ERRO: IDENTIFIER ",token.lexeme ," NOT DECLARED")


        