# Aviso Importante
<p>
  Para quem não entende programação, esse programa tem o intuito de simular uma pessoa comum jogando no "Jogo do Bicho" através de uma interface, e não de tentar descobrir resultados ou burlar o jogo.
</p>
<hr>

# Jogo do Bicho
<p>
  Muito provavelmente você já ouviu falar bastante sobre esse jogo, e provavelmente também não conhece as regras. Esse era meu estado quando decidi iniciar esse projeto, então fui atrás de conhecer como funcionava o jogo para construir uma interface que simulasse como funcionava o <b>Jogo do Bicho</b>. 
</p>
<p>
  Foi uma tarefa bem difícil, perguntei para algumas pessoas como que funcionava na intenção de receber uma explicação breve e clara para montar meu código que achei que ía ter umas 400 linhas (meu primeiro projeto), mas sem sucesso nenhum. Foi aí que pesquisei no YouTube e achei um vídeo que foi a base da construção do meu programa, o link dele estará no final desse README.
</p>

<img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/My%20Projects/0001%20Jogo%20do%20bicho/%26%20-%20Image/Captura%20de%20Tela%20(155).png" width="1000px" align="center">


<hr>

# Regras do Jogo

<h6>8 Modos de aposta</h6>
<p>Existem vários outros modos, que só não foram inseridos por falta de popularidade e de informações sobre cada um, mas os principais estão no programa.</p>
    
<h6>25 Grupos de animais</h6>
<p>
  Grupos que vão do 'Avestruz' até a 'Vaca'. Cada grupo tem 4 dezenas que começam na 01 e vão até a 00 (substituindo o número 100). É necessário conhecer cada um e suas respectivas dezenas para a maioria das apostas.
</p>
    
<h6>Prêmiação</h6>
<p>Depende exclusivamente do modo, valor apostado e do resultado do jogo.</p>
    
<h6>Resultado do Jogo</h6>
<p>
  É dado pelo sorteio das milhares que é feito na última janela. Os números das milhares é uma sequência numérica de 4 digitos gerados aleatoriamente, e de acordo com sua aposta, o programa irá te mostrar se você ganhou ou perdeu.
</p>

<hr>

<div>
  
  <h3>Janela 2 → Opções de Jogo</h3>
  
  <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/My%20Projects/0001%20Jogo%20do%20bicho/%26%20-%20Image/janela2.gif" align="right" width="420px">
 
  <p align="justify">
    Nessa janela é decidido o valor e o modo de aposta. Caso o usuário ainda não conheça o jogo, ele pode apertar no botão de <b>"Conhecer as Regras"</b>, que após isso, será exibido no <b>Output</b> as regras do modo de aposta que estiver no campo acima.
  </p>
  <p align="justify">
    Para que o botão funcione e exiba as regras, as exigências são:
    <ol>
      <li>O usuário precisa inserir uma aposta, válida e a partir de 1 centavo.</li>
      <li>Que o grupo inserido seja válido e existente dentre os animais do jogo.</li>
    </ol>
  </p>
  <p align="justify">
    As regras e as premiações mudam conforme a escolha, com uma mensagem de premiação personalizada para cada modo, que levam em consideração o valor inserido pelo usuário no campo de aposta para fazer a soma e retornar quanto ele possivelmente ganharia.
  </p>
  <p align="justify">
    Após fazer essas duas etapas e confirmar o grupo escolhido, o próprio botão e o campo de modo de jogo são desabilitados, e outros dois botões são habilitados, o <b>"Cancelar"</b> serve caso o usuário queira cancelar e escolher outro modo de aposta, e o <b>"Enviar Escolha"</b> irá salvar os dados e levar o usuário para a "terceira" e última janela do programa. 
  </p>
  <p>Ao clicar no botão <b>"Voltar"</b>, a janela 2 fecha e ele retorna para janela 1.</p>
</div>

<hr>

### Tratamento de Erros e Lógica

<div>
  <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/My%20Projects/0001%20Jogo%20do%20bicho/%26%20-%20Image/bet_error.gif" align="right" width="420px">
    <ul>
      <li>Campo de Aposta</li>
      <p align="justify">
        Nas regras é necessário fazer a multiplicação de acordo com o valor inserido. Na programação só é possível fazer a multiplicação por valores que separam as casas decimais por ponto, então foi feito um <b>Loop For</b> que, para cada caracter no campo de aposta, ele verifica se o caracter é uma vírgula e faz a troca para ponto, afinal sempre que colocamos um valor "quebrado" aqui no Brasil separamos por vírgula.
      </p>
      <p align="justify">
        Após isso é exibido um <b>PopUp</b> para cada opção inválida, são elas: Começar ou Terminar com . ou , / 2 ou mais . ou , / Letras ou símobolos / Valor menor que 1 centavo.
      </p>
    </ul>
</div>

<br>
<br>

<div>
  <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/My%20Projects/0001%20Jogo%20do%20bicho/%26%20-%20Image/error_game_mode.gif" align="right" width="420px">
    <ul>
      <li>Modo de Jogo</li>
      <p align="justify">
        A cada vez que o usuário aperta no botão de <b>"Confirmar"</b>, o programa verifica se aquela opção (com <b>.strip() e .upper()</b>) existe dentro das opções válidas. Caso exista, a opção por enquanto será temporariamente salva e o campo e o próprio botão serão desativados. Se não existir será exibido um <b>"PopUp"</b> notificando e orientando o usuário a escolher outro grupo adequado.
      </p>
    </ul>
  <br>
</div>

<div>
    <ul>
      <li>Enviar Escolha</li>
      <p align="justify">
        Ele tem basicamente as mesmas verificações que o botão de <b>"Conhecer as Regras"</b>, afinal, não necessariamente o usuário vai usar aquele botão, talvez ele já conheça as regras, então, ao clicar em <b>"Enviar Escolha"</b> tem que ser verificado também as condições do campo de valor de aposta. Não é necessário verificar se a opção de jogo é válida nesse botão, porque isso já é apurado no botão de confirmar, lembrando que botão de <b>"Enviar Escolha"</b> só é ativado quando o botão <b>"Confirmar"</b> está desabilitado.
      </p>
    </ul>
</div>
<hr>

### Falha na biblioteca

<div>
  <p align="justify">
  Obviamente, para cada opção de jogo são necessários diferentes campos, botões e lógicas. A ideia inicial era criar todos os elementos fundamentais de todas as 8 opções de jogo já na segunda janela e deixar todos com o parâmetro <b>"visible="False"</b>, e após o usuário clicar no botão de <b>"Confirmar"</b>, apenas os elementos essenciais para aquele modo seriam exibidos.
  </p>
  <p align="justify">
    Essa ideia é muito boa, afinal economizaria diversas interfaces e linhas de código. No entanto, isso infelizmente não foi possível por conta de um erro na própria biblioteca. Imagine uma linha com quaisquer 3 elementos, um ao lado do outro, todos habilitados e visíveis, porém existe outro botão que, ao ser pressionado, a função dele é esconder/exibir esses três elementos. Para o erro ficar mais claro, no momento de esconder funciona perfeitamente, mas na hora de exibir, esses mesmos 3 elementos que estavam alinhados lado à lado voltam um embaixo do outro. Por esse motivo que eu fui impossibilitado de criar todos os elementos específicos para cada modo de jogo na segunda janela, e tive que criar mais <b>8 janelas</b>, que são específicas com o modo de jogo que o usuário escolheu, muito parecidas e ambas servem como a 3º janela no programa.
  </p>
  
  <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/My%20Projects/0001%20Jogo%20do%20bicho/%26%20-%20Image/error_library.gif" height="200px" align="left">
  
  <p align="right">
    <br><br>
    <ol>
      <li>Todos elementos visíveis e alinhados.</li>
      <li>Todos elementos escondidos.</li>
      <li>Os elementos não voltaram alinhados.</li>
    </ol>
  </p>
</div>

<br><hr>

### Janela 3 → Resultado do jogo

<p>
  <h6>Informações Repetidas</h6>
  <p align="justify">
    Todas as janelas tem blocos separados por Frames e e salvam o modo e o valor apostado. O usuário pode clicar no botão de <b>"voltar"</b> e retornar para a 2º janela a qualquer momento (antes de sortear as milhares) e fazer novas escolhas. Os campos com grupos ou números são do tipo <b>"Combo"</b>, que facilitam muito e já mostram as opções válidas para o usuário quando ele aperta na setinha lateral. O botão de <b>"Cancelar"</b> só é habilitado depois que o usuário aperta no botão de <b>"Confirmar"</b> da mesma linha, e o de <b>"Sortear Milhares"</b> só é habilitado depois que o usuário apertou o último botão de <b>"confirmar"</b> no Frame de escolha. As Janelas que tem o Frame de <b>Premiação</b>, dão a opção do usuário fazer dois tipos de apostas através de <b>Radio Buttons</b> que obviamente mudam a lógica do campo de sortear as milhares para verificar se o usuário ganhou ou não, e seus respectivos botões não tem funcionalidades, apenas informam a possível recompensa. E os que não tem esse Frame, é porque o modo de aposta já exige que seja apostado em todas as milhares. As 6 milhares começam com 4 asteríscos representando a sequência numérica, e o verdadeiro resultado é mostrado depois que o botão é apertado. E por fim, o botão de jogar novamente é habilitado e sua função é nos conduzir novamente para a primeira janela do programa.
  </p>
</p>
  
<hr>

  <p>
  Vou detalhar somente uma janela da 3º etapa, afinal todas são parecidas e as próprias regras já são mostradas e explicadas no próprio programa. Compilem o código e joguem por conta própria para conhecer melhor.
  </p>

<div>
  <h6>Modo: Terno de Grupo</h6>
  <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/My%20Projects/0001%20Jogo%20do%20bicho/%26%20-%20Image/terno_de_grupo.gif" align="left" height="500px">
  <p>→ Lógica dos Elementos</p>
  <p>1. Grupos são considerados válidos quando, com <b>.strip() e .upper()</b>, coincidem com algum grupo do array oficial.</p>
  <p>2. A cada botão de confirmar pressionado, o <b>"Cancelar"</b> da mesma linha e o campo de animais da próxima linha são habilitados.</p>
  <p>3. No 2º e no 3º campo de animais, é verificado se o animal da vez já foi escolhido anteriormente.</p>
  <p>4. O botão de <b>"Sortear Milhares"</b> só é habilitado depois que o usuário clicou no último botão de <b>"Confirmar"</b>, assim temos a certeza de que todos os campos estão válidos e preenchidos.</p>
  <p>5. Para cada milhar, é verificado se nos últimos 2 números existe uma dezena de algum dos 3 grupos escolhidos.</p>
  <p>6. Mensagens personalizadas caso você acerte os 3 grupos (igual o exemplo do gif), quando acerta 2 grupos ele te diz qual faltou acertar e quando acerta apenas 1 ele mostra qual você acertou.</p>
  <p>7. Dependendo do resultado, as milhares são pintadas de verde ou de vermelho.</p>
</div>
<hr>

### Principais Dificuldades
<div>
  <h6>Dezenas / Centenas / Milhares </h6>
  <p>
    Tive que fazer um array armazenando cada número válido, e não consegui gerar esses números com um <b>for</b> ou com a biblioteca <b>random</b> porque muitos números começam com 0 na frente, e esse tipo de número no python dá erro, exceto que ele seja uma string. Então escrevi todos os números com ajuda da ferramenta barra de busca, mas senti muita falta de uma biblioteca específica pra isso. 
  </p>
  
  <h6>Tamanho dos elementos</h6>
  <p>
    Deixei o máximo possível simétrico, mas seria melhor se eu tivesse conseguido colocar medidas do tipo pixel/px para ser mais preciso, já que o parâmetro <b>"size"</b> fica diferente dependendo dos elementos, mesmo que dentro dele seja o mesmo número para ambos. 
  </p>
  
  <h6>2 Ou mais Output's</h6>
  <p>Eu tentei algumas vezes colocar mais de um <b>Output</b> na mesma janela, só que eu não consegui direcionar certos textos para um e outros textos para o outro.</p>
  
  <h6>Tratamento do campo de aposta</h6>
  <p>
    Passei bastante tempo fazendo tratamentos nesse campo, por conta da troca de vírgulas para ponto, verificar a quantidade e a posição, não aceitar símbolos e estipular um valor mínimo para a aposta, no final nem era tão complicado mas exigiu tempo.
  </p>
  
  <h6>Textos</h6>
  <p>
    Cada texto eu tive que formatar manualmente usando o <b>"\n"</b> para quebrar linhas, dentro do <b>"Output"</b> por exemplo, ele não respeita o tamanho de elemento e vai expandindo lateralmente a cada nova palavra inserida. Eu não consegui usar a função de <b>"Autosize"</b> que aparecia como sugestão, então por isso que foi necessário usar muitas quebras de linhas.
  </p>
  <p>
    Não só na formatação mas a qualquer momento que eu precisasse exibir um texto de acordo com algum dado do meu programa, eu já sabia que teria alguma complicação. Essa parte é bem confusa, tive que variar entre <b>window['elemento'], window['elemento'].get_text(), window['elemento'].DisplayText</b> ou printar o <b>"value"</b> de algum elemento e testar qual dessas opções que dá certo.
  </p>
  
</div>
<hr>

### O que falta ser feito
<h6>Os tópicos que tiverem ❌ na frente faltam ser feitos e ✅ já foram concluídos</h6>
<ul>
  <li>❌ Aplicar o Swicth para diminuir a quantidade de IF's</li>
  <li>❌ Usar Classes</li>
  <li>❌ Separar o código em módulos</li>
</ul>
<hr>

### Experiência do projeto
<p>
  Eu estava terminando de fazer esse código de forma normal, sem interface. Apresentei para algumas pessoas e inclusive minha irmã disse que seria mais legal se tivesse algum "aplicativo" para jogar ao invés de ficar respondendo tudo no terminal, e até então eu nem sabia que era possível criar interfaces com python. Mas quando comecei a aprender o <b>PySimpleGUI</b> em um curso, eu deicidi passar todo o código para uma interface. 
</p>
<p>
  O conhecimento do curso foi muito raso, diria que ensinou uns 40% do que eu apliquei no código. Apesar de realmente ser simples de mexer na biblioteca, o resto foi feito com muitas tentativas e erros, mas à cada acerto eu via a minha ideia tomando forma e se tornando de fato um programa.
</p>
<p>
  Demorou mais do que eu esperava pelo fato de eu ter mexido muito na minha rotina esses tempos, mas foi muito legal tirar uma idea da teoria e aplicar na prática somente com os meus conhecimentos, para meu primeiro projeto eu fiquei muito satisfeito.
</p>
<hr>

### Considerações Finais
<h6>Thalysson e Gustavo - Os primeiros a verem e a opinar sobre o projeto.</h6>
<h6>Link do Vídeo que aprendi as regras do jogo:</h6> https://www.youtube.com/watch?v=B65sptnOru8
<hr>

<h3 align="center">Autor do Projeto</h3>
<p align="center">© 2022 França, The GOAT.</p>
<h6 align="right"><i>15/04/2022</i></h6>
