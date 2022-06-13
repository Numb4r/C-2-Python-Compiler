from const import TypeToken as tt
from Token import Token
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
_typeAcceptance={
    tt.TK_IDENTIFIER:[],
    tt.TK_INTEGER:[tt.TK_INTEGER,tt.TK_FLOATINGPOINT,tt.TK_CHARLITERAL],
    tt.TK_FLOATINGPOINT:[tt.TK_INTEGER,tt.TK_FLOATINGPOINT,tt.TK_CHARLITERAL],
    tt.TK_CHARLITERAL:[],
    tt.TK_STRINGLITERAL:[],

}
class LexicalAnalysis:

    def __init__(self):
        self.scope={}
        self.variables={}
        self.typeDeclaration = []
        self.idDeclaration = None
        self.beginDeclaration = False
        self.beginAssignment = False
        self.lastScopeDeclaration = 0
        

    def analyseToken(self,token:Token):
        if token.tipo in _typeDeclaration:
            self.typeDeclaration.append(token)
            self.beginDeclaration = True
            return
        if token.tipo is tt.TK_IDENTIFIER and self.idDeclaration is None:
            self.idDeclaration = token
            return
        if token.tipo is tt.TK_OPASSIGNMENT:
            self.beginAssignment = True
            return 
        if (token.tipo in _typeDeclaration or token.tipo in _typeOperation) and self.idDeclaration is not None:
            if self.idDeclaration.valor is None:
                self.idDeclaration.valor = []
            self.idDeclaration.valor.append(token)
            return
        if token.tipo is tt.TK_PARENTHESESCLOSE:
            return
            
        if token.tipo is tt.TK_OPEOL:
            if self.idDeclaration is not None:
                if self.beginDeclaration == True :
                    if self.variables.get(self.idDeclaration.lexeme) is not None:
                        raise "LEXIAL ERROR: VARIABLE " + self.idDeclaration.lexeme + " IS ALREADY DECLARED"
                    if self.escopo.get(self.idDeclaration.lexeme) is not None:
                        raise "LEXICAL ERROR: FUNCTION " + self.idDeclaration.lexeme+ " IS ALREADY DECLARED"
                elif self.beginAssignment == True and self.variables.get(self.idDeclaration.lexeme) is None: # corrigir isso pra agir de acordo com o escopo
                        raise "LEXICAL ERROR: VARIABLE "+ self.idDeclaration.lexeme + "IS NOT IN THE SCOPE"
                self.variables[self.idDeclaration.lexeme]



