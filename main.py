from scanner import Scanner
from parser_ import Parser
from const import TypeToken as tt
# import semanticTrees 
from back import Back
from semanticTrees import *
from const import TypeToken as tt
string = "newTestes/Código " 

# _id = Identifier('cu',tt.TK_KWINT,None)
# # print(_id)
# valor = [(tt.TK_KWINT,2)]
# validateValors(_id, valor)


sc = Scanner("./testes\example.cpp")
bk = Back(sc)
bk.transpile()
# pa = Parser(sc)
# pa.analysis()

# string = "código"
# from Token import Token 
# from Token import validateTKHEAD
# tk = Token(tt.TK_OPHEAD,"include","<stdio.h>")
# # vec = []
# # a = sc.nextToken()
# # while a != None:
# #     vec.append(a)
# #     a = sc.nextToken()
# # print(vec)
# sc = Scanner("./testes/newTestes/Código 1.txt")
# pa = Parser(sc)
# pa.analysis()
# print(pa.st.globalScope.identifiers.get("main").identifiers)
# print()
# print(pa.scope)
# for i in range(1,10):
# sc = Scanner("./testes/"+string+str(i)+".txt",False)
#     print(i)
    # try:
    # except BaseException as err:
    #     print(err)
    # # sc = Scanner("./testes/base.c")
    # tk = sc.nextToken()
    # while tk != None:
    #     print(tk)
    #     tk  = sc.nextToken()
    