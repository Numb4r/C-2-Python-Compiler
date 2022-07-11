from const import TypeToken as tt
from const import _sintaxGraph as sg
from Token import validateTKHEAD
from scanner import Scanner
from semanticTrees import SemanticAnalysis

class Parser:
    scope = [tt.TK_BRACESOPEN,tt.TK_PARENTHESESOPEN,tt.TK_BRACESOPEN,tt.TK_BRACESCLOSE,tt.TK_BRACKETSCLOSE,tt.TK_PARENTHESESCLOSE]
    brackets = 0
    parentheses = 0
    braces = 0
    st = SemanticAnalysis()
    
    def __init__(self,scanner:Scanner):
        self.sc = scanner
    def analysis(self):
        token = self.sc.nextToken()
        while token != None:
            if token.tipo == tt.TK_OPHEAD:
                token = self.sc.nextToken()
                pass
                # TODO: Corrigir bug
                # print(validateTKHEAD(token))
            nextToken = self.sc.nextToken()
            if nextToken != None:
                if nextToken.tipo in self.scope:
                    if nextToken.tipo ==tt.TK_BRACESOPEN:
                        self.braces+=1
                    elif nextToken.tipo == tt.TK_BRACESCLOSE:
                        self.braces-=1
                    elif nextToken.tipo == tt.TK_BRACKETSOPEN:
                        self.brackets+=1
                    elif nextToken.tipo == tt.TK_BRACKETSCLOSE:
                        self.brackets-=1
                    elif nextToken.tipo == tt.TK_PARENTHESESOPEN:
                        self.parentheses+=1
                    elif nextToken.tipo == tt.TK_PARENTHESESCLOSE:
                        self.parentheses-=1
                if nextToken.tipo not in sg.get(token.tipo):
                    raise "Sintax Error"
            self.st.analyseToken(token)
            token = nextToken

        if self.braces != 0 or self.parentheses !=  0 or self.brackets != 0:
            print(str(self.braces)+" "+str(self.parentheses)+" "+str(self.brackets))
            raise "Sintax Error"
        
        


        