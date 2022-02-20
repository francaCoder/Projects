# Jogo de adivinhar


   * Um simples código em python onde fizemos um jogo de adivinha, no qual o intuito é adivinhar o número escolhido pelo usuário, que nesse caso o computador depende da honestidade do usuário, acreditando que ele escolherá um número mentalmente `(entre 1 = Número mínimo e o parâmetro passado pelo usuário quando chamasse a função)` e não trocará até o jogo se encerrar. O número é escolhido através de uma função, que usa o método `randint` (importado da biblioteca `math` que disponibiliza funções extras e prontas voltadas para o ramo da matemática).
   * De acordo com a intuição do computador, podemos dar a resposta colocando as `iniciais [H/L/C]` se o palpite dele foi muito alto, muito baixo ou se foi o número correto, e se jogarmos de maneira correta, automaticamente as possibilidades se afunilarão facilitanto a futura escolha do número correto `feita pelo computador`, que ao ser acertado colocaremos a `inicial [C]`, indicando ao programa que mostre a mensagem de felicitações que assim como as respostas de alto e baixo são retornadas graças ao poder das `estruturas condicionais` IF - Elif.
   
<img src="">


  * O código da direita foi melhorado usando um `método de verificação` para garantir que o usuário colocou uma das iniciais que estabelecemos como padrão, pois anteriormente não tinha nenhuma verificação e qualquer letra o programa aceitaria sem retornar nenhum erro e assim atrapalhando a funcionalidade do jogo. 
  
