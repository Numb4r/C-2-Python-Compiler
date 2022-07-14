from scanner import Scanner
from parser_ import Parser
from const import TypeToken as tt
# import semanticTrees 
from back import Back
from semanticTrees import SemanticAnalysis
from const import TypeToken as tt
string = "newTestes/Código " 



print("lexico")
sc = Scanner("./testes\example.cpp")
ps = Parser(sc)
print("Sintatico")
ps.analysis()
st = SemanticAnalysis(sc)
print("Semantico")
print("Back")
bk = Back(sc)
bk.transpile()
