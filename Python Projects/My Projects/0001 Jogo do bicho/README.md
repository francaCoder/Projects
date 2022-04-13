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
        Existem vários outros, que só não foram inseridos por falta de popularidade e de informações sobre cada um, mas os           principais estão no programa.
      </p>
    </li>
    <li>
      25 Grupos de animais
      <p>
        Grupos que vão do 'Avestruz' até a 'Vaca'. Cada grupo tem 4 dezenas que começam na 01 e vão até a 00 (substituindo o         número 100). É necessário conhecer cada um e suas respectivas dezenas para a maioria das apostas.
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
        É dado pelo sorteio das milhares que é feito na última janela. Os números das milhares são uma sequência de 4 números         gerados aleatoriamente, e de acordo com sua aposta, o programa irá te mostrar se você ganhou ou perdeu.
      </p>
    </li>
  </ul>
</p>

<hr>

<div>
  
  <h3>Janela 2 → Opções de Jogo</h3>
  
  <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/My%20Projects/0001%20Jogo%20do%20bicho/imagem%20teste%5D.jpg" align="right">
 
  <p align="justify">
    Nessa janela é decidido o valor e o modo de aposta. Caso o usuário não conheça o jogo, ele pode apertar no botão de           <b>"Conhecer as Regras"</b>, que após isso, será exibido no <b>Output</b> as regras do modo de aposta que estiver no         campo acima.
  </p>
  <p>
    Para que o botão funcione e exiba as regras, as exigências são:
    <ol>
      <li>O usuário precisa inserir uma aposta, válida e a partir de 1 centavo.</li>
      <li>Que o grupo inserido seja válido e existente dentro da</li>
    </ol>
  </p>
    Após fazer essas duas etapas e confirmar o grupo escolhido, o botão de <b>"Enviar Escolha"</b> é habilitado, e quando o       usuário o aperta, ele será direcionado para a "terceira" e última janela. 
  <p>
  </p>
</div>
