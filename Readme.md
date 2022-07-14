# Projeto Compilador de C para Python
 
A estrutura do projeto está dividida em:
 
- Scanner : Analisador Léxico
- Parser : Analisador Sintático
- Semantic Tree: Analisador Semântico
- Back : Converter para código Python
 
Além disso, os arquivos ``const`` e ``Token`` são usados para auxiliar na montagem do compilador
 
## Cost
 
No arquivo “const” está toda a tabela de símbolos, com suas definições e gramática. Além disso, são definidas as keywords, os tipos, inferência de tipos e compatibilidade de operadores. O arquivo “const” é usado em todo o compilador para acesso às tabelas auxiliares para uma melhor manipulação de seus propósitos.
 
## Front end
 
O front end constitui-se de três analisadores: léxico, sintático e semântico. Eles são desacoplados um do outro sendo possível sua substituição e manutenção sem afetar outras etapas. Eles utilizam a tabela de símbolos fornecida pelo arquivo const para saber qual passo tomar. Por exemplo: o analisador léxico utiliza as definições gramaticais de cada símbolo para gerar os tokens que serão usados posteriormente. O analisador léxico deve gerar um array de tokens que será analisado nas próximas etapas. As próximas etapas requisitam para o Scanner novos tokens para serem analisados, um de cada vez.
 
### Construindo estruturas
Para substituir algum analisador, deve ser seguido algumas regras:
 
Caso seja o analisador léxico (Scanner):
- Deverá oferecer um método ``nextToken``, que retorna o próximo token do código
- Deverá oferecer um método ``resetPos``, que reseta a posição de análise para o início do arquivo
 
Caso seja outro analisador (Parser,SemanticTree):
- Deverá usar ``resetPos`` no início da análise para resetar a posição do  Scanner ou se utilizar de outro artifício para isso
 
Os erros, em geral, são tratados utilizando ``throw`` (``raise``).
 
## Back End
 
O back end foi montado de tal forma que a linguagem de destino é o Python, ao invés de linguagem de máquina. Essa etapa não possui código intermediário, nem otimização, visto que não há necessidade já que o código final ainda irá passar para outra linguagem de alto nível que já possui um otimizador. A conversão respeita a declaração de variáveis sem a inicialização, o que não é usual em Python. Funções ``scanf`` e ``printf`` tiveram sua tradução apropriada para a linguagem.

