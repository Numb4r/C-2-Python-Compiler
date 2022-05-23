import const as const
from scanner import Scanner

class Parser:
    def __init__(self,scanner:Scanner):
        self.sc = scanner
    def analysis(self):
        token = self.sc.nextToken()
        while token != None:
            nextToken = self.sc.nextToken()
            print(token," ",nextToken)
            if nextToken != None:
                # print(const._sintaxGraph.get(token.tipo))
                if nextToken.tipo not in const._sintaxGraph.get(token.tipo):
                    raise "Sintax Error"
            token = nextToken


        