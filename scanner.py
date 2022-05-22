from Token import Token
import const as const
from const import TypeToken
import re
class Scanner:
    def __init__(self,filename,debug=False):
        self.content=[]
        self.estado = 0
        self.pos = 0
        self.debug = debug
        try:
            with open(filename) as file:
                # self.content = [y for x in file.read().splitlines() for y in x]
                self.content =[]
                for x in file.read().splitlines():
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
            for i in const._tableOfTypes:
                if re.search(i,lexeme):
                    lexemeType = const._tableOfTypes.get(i)
                    lexeme = lexeme[:-1]
                    self.back()
                    endOfToken = True
                    print(lexeme)
                    kw = const._keyWordsTable.get(lexeme)
                    
                    lexemeType =  kw if  kw != None else lexemeType
                    if lexemeType == const.TypeToken.TK_IDENTIFIER or lexemeType == const.TypeToken.TK_INTEGER or lexemeType == const.TypeToken.TK_FLOATINGPOINT or lexemeType == const.TypeToken.TK_CHARLITERAL or lexemeType == const.TypeToken.TK_STRINGLITERAL :
                        token = Token(lexemeType,lexeme)
                    else:
                        token = Token(lexemeType)
                    return token

            # if self.estado  == 0:
            #     if self.isChar(currentChar):
            #         lexeme+=currentChar
            #         self.estado = 1
            #     elif self.isDigit(currentChar):
            #         lexeme+=currentChar
            #         self.estado = 3
            #     elif self.isSpace(currentChar):
            #         self.estado = 0
            #     elif  self.isOperator(currentChar):
            #         self.estado =5
            #     else:
            #         raise Exception("Unrecognized Symbol")
            # elif self.estado == 1:
            #     if self.isChar(currentChar) or self.isDigit(currentChar):
            #         self.estado = 1
            #         lexeme+=currentChar
            #     elif self.isSpace(currentChar) or self.isOperator(currentChar):
            #         self.estado = 2
            #     else:
            #         raise "Malformed Identifier"
            # elif self.estado == 2:
            #     token = Token(const.const.TypeToken.TK_IDENTIFIER,lexeme)
            #     self.back()
            #     return token
            # elif self.estado == 3:
            #     if self.isDigit(currentChar):
            #         self.estado==3
            #         lexeme+=currentChar
            #     elif not self.isChar(currentChar):
            #         self.estado = 4;
            #     else:
            #         raise Exception("Unrecognized Number")
            # elif self.estado == 4:
            #     token = Token(const.const.TypeToken.TK_NUMBER,lexeme)
            #     self.back()
            #     return token
            # elif self.estado == 5:
            #     lexeme += currentChar
            #     token = Token(const.TK_OPERATOR,lexeme)
            #     return token
                
        
    def isChar(self,c):
        return True if re.search("[a-zA-Z]", c) else False
    def isDigit(self,c):
        return True if re.search("[0-9]",c) else False
    def isOperator(self,c):
        # return 
        pass 
    def isSpace(self,c):
        return True if re.search("\s", c) else False
        # return c == ' ' or c == '\t' or c == '\n' or c == '\r'
    def nextChar(self):
        c = self.content[self.pos]
        self.pos+=1
        
        return c
    def isEOF(self):
        return self.pos+1 >= len(self.content)
    def back(self):
        self.pos-=1