# Aviso Importante
<p>
  Para quem não entende programação, esse programa tem o intuito de simular uma pessoa comum jogando no "Jogo do Bicho" através de uma interface, e não de tentar descobrir resultados ou burlar o jogo.
</p>
<hr>

<img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/My%20Projects/0001%20Jogo%20do%20bicho/%26%20-%20Image/Captura%20de%20Tela%20(155).png" width="1000px" align="center">

# Jogo do Bicho
<p>
  Muito provavelmente você já ouviu falar bastante sobre esse jogo, e provavelmente também não conhece as regras. Esse era meu estado quando decidi iniciar esse projeto, então fui atrás de conhecer como funcionava o jogo para construir uma interface que simulasse como funcionava o <b>Jogo do Bicho</b>. 
</p>
<p>
  Foi uma tarefa bem difícil, perguntei para algumas pessoas como que funcionava na intenção de receber uma explicação breve e clara para montar meu código que achei que ía ter umas 400 linhas (meu primeiro projeto), mas sem sucesso nenhum. Foi aí que pesquisei no YouTube e achei um vídeo que foi a base da construção do meu programa, o link dele estará no final desse README.
</p>

<hr>

# Regras 
<p>
  <ul>
    <li>
      8 Modos de aposta
      <p>
        Existem vários outros, que só não foram inseridos por falta de popularidade e de informações sobre cada um, mas os principais estão no programa.
      </p>
    </li>
    <li>
      25 Grupos de animais
      <p>
        Grupos que vão do 'Avestruz' até a 'Vaca'. Cada grupo tem 4 dezenas que começam na 01 e vão até a 00 (substituindo o número 100). É necessário conhecer cada um e suas respectivas dezenas para a maioria das apostas.
      </p>
    </li>
    <li>
      Prêmiação
      <p>
        Depende exclusivamente do modo, valor que você apostou e do resultado do jogo.
      </p>
    </li>
    <li>
      Resultado do Jogo
      <p>
        É dado pelo sorteio das milhares que é feito na última janela. Os números das milhares são uma sequência de 4 números gerados aleatoriamente, e de acordo com sua aposta, o programa irá te mostrar se você ganhou ou perdeu.
      </p>
    </li>
  </ul>
</p>

<hr>

<div>
  
  <h3>Janela 2 → Opções de Jogo</h3>
  
  <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/My%20Projects/0001%20Jogo%20do%20bicho/%26%20-%20Image/janela2.gif" align="right" width="420px">
 
  <p align="justify">
    Nessa janela é decidido o valor e o modo de aposta. Caso o usuário não conheça o jogo, ele pode apertar no botão de <b>"Conhecer as Regras"</b>, que após isso, será exibido no <b>Output</b> as regras do modo de aposta que estiver no campo acima.
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
        Ele tem basicamente as mesmas virificações que o botão de <b>"Conhecer as Regras"</b>, afinal, não necessariamente o usuário vai usar aquele botão, talvez ele já conheça as regras, então, ao clicar em <b>"Enviar Escolha"</b> tem que ser verificado também as condições do campo de valor de aposta. Não é necessário verificar se a opção de jogo é válida nesse botão, porque isso já é apurado no botão se confirmar, e o botão de <b>"Enviar Escolha"</b> só é ativado quando o botão <b>"Confirmar"</b> está desabilitado.
      </p>
    </ul>
</div>
<hr>
