from scanner import Scanner

sc = Scanner("a.c")
token = sc.nextToken()
if token == None:
    print("Error")
while  token != None:
    print(token)
    token = sc.nextToken()
    
