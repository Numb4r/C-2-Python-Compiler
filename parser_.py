from const import TypeToken as tt
from const import _sintaxGraph as sg
from Token import validateTKHEAD
from scanner import Scanner


class Parser:
    def __init__(self,scanner:Scanner):
        self.sc = scanner
    def analysis(self):
        token = self.sc.nextToken()
        
        # error = 1
        while token != None:
            # print(token)
            # Forma burra,arrumar depois
            if token.tipo == tt.TK_OPHEAD:
                token = self.sc.nextToken()
                pass
                # TODO: Corrigir bug
                # print(validateTKHEAD(token))
                    
                
            #     token = self.sc.nextToken()
            #     print(token)
            #     if token.tipo == tt.TK_IDENTIFIER and token.lexeme == "include":
            #         token =  self.sc.nextToken() 
            #         print(token)
            #         if token.tipo == tt.TK_OPLT:
            #             token =  self.sc.nextToken() 
            #             print(token)
            #             if token.tipo == tt.TK_IDENTIFIER:
            #                 token =  self.sc.nextToken() 
            #                 print(token)
            #             if token.tipo == tt.TK_OPDOT :
            #                 token =  self.sc.nextToken() 
            #                 print(token)
            #                 if token.tipo == tt.TK_IDENTIFIER:
            #                     token =  self.sc.nextToken() 
            #                     print(token)
            #                     if token.tipo == tt.TK_OPGT:
            #                         token =  self.sc.nextToken() 
            #                         print(token)
            #                         error = 0
            # if error == 1:
            #     raise "Sintax Error"


                
            nextToken = self.sc.nextToken()
            print(token,nextToken)
            if nextToken != None:
                if nextToken.tipo not in sg.get(token.tipo):
                    raise "Sintax Error"
            token = nextToken


        