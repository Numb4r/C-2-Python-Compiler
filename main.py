from scanner import Scanner
from parser_ import Parser
string = "newTestes/Código " 
# string = "código"
for i in range(1,10):
    print(i)
    sc = Scanner("./testes/"+string+str(i)+".txt",False)
    # sc = Scanner("./testes/base.c")
    # tk = sc.nextToken()
    # while tk != None:
    #     print(tk)
    #     tk  = sc.nextToken()
    pa = Parser(sc)
    pa.analysis()

