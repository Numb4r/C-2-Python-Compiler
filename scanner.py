from Token import Token
# import const as c
from const import _tableOfTypes
from const import _keyWordsTable
from const import TypeToken as tt
import re
class Scanner:
    def __init__(self,filename,debug=False):
        self.content=[]
        self.estado = 0
        self.pos = 0
        self.debug = debug
        try:
            with open(filename) as file:
                f = file.read()
                f = re.sub("\/\/.*",' ',f)
                f = re.sub("\/\*(.|\s)*\*\/",' ',f)
                v = f.splitlines()
                self.content =[]
                for x in v:                    
                    for y in x:
                        self.content.append(y)
                    self.content.append("\n")
            if debug == True:
                print("DEBUG------")
                print(self.content)
                print("-----------")
                print(len(self.content))
        except FileNotFoundError:
            print("Um erro ocorreu ao abrir o arquivo")
        
    def nextToken(self):
        self.estado = 0
        lexeme=""
        endOfToken = True
        if self.isEOF():
            return None 
        while True:
            currentChar = self.nextChar()
            while endOfToken:            
                if self.isSpace(currentChar):
                    currentChar = self.nextChar()
                else:
                    endOfToken = False
            lexeme+=currentChar
            if self.debug == True:
                print(currentChar,"-","-",self.pos,"-",self.estado)
            for i in _tableOfTypes:
                if re.match(i,lexeme):
                    lexemeType = _tableOfTypes.get(i)
                    lexeme = lexeme[:-1]
                    self.back()
                    endOfToken = True
                    # print(lexeme)
                    kw = _keyWordsTable.get(lexeme)
                    lexemeType =  kw if  kw != None else lexemeType
                    if lexemeType == tt.TK_OPHEAD:
                        currentChar = self.nextChar()
                        # TODO: Corrigir bug que o header nao captura os atributos
                        typeHeader = ''
                        while not re.match("\n", currentChar):
                            typeHeader += currentChar
                            currentChar = self.nextChar()

                        typeHeader,valor = typeHeader.split()
                        token = Token(lexemeType,typeHeader,valor)
                        valor = ''
                        typeHeader = ''
                        
                        
                    if lexemeType == tt.TK_IDENTIFIER or lexemeType == tt.TK_INTEGER or lexemeType == tt.TK_FLOATINGPOINT or lexemeType == tt.TK_CHARLITERAL or lexemeType == tt.TK_STRINGLITERAL :
                        token = Token(lexemeType,lexeme)
                    else:
                        token = Token(lexemeType)
                    return token

    def isSpace(self,c):
        return True if re.search("\s", c) else False
    def nextChar(self):
        c = self.content[self.pos]
        self.pos+=1
        return c
    def isEOF(self):
        return self.pos+1 >= len(self.content)
    def back(self):
        self.pos-=1