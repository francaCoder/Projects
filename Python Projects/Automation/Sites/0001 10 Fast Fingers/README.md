<div>
<h1>Automação de Sites → 10 Fast Fingers</h1>
<p>Link → https://10fastfingers.com/typing-test/portuguese</p>
<p>
  <h3>◻ Propósito do Site</h3>
  Ao entrar no site nos deparamos com palavras aleatórias e um campo para inserir cada uma em um tempo máximo de 1 minuto. A cada palavra é verificado se ela foi escrita de maneira certa ou errada, somando um acerto ou um erro para cada uma e mostrando um resumo no final da nossa pontuação.
</p>
<hr>
<p>
  <h3>◻ Lógica para Automação</h3>
  Ao abrir o <b>Dev Tools</b> e inspecionar era possível saber o <b>classe</b> de cada palavra, geralmente toda vez que abrimos o site       temos 365 palavras aleatórias, e a "palavra da vez" tem a <b>class="highlight"</b>. Sabendo disso eu faço um loop For em um Range de 300
  (pois em todos os testes que eu fiz o computador não conseguiu digitar mais do que 300 palavras em mais de 1 minuto) que para cada         "palavra da vez" ele acha o campo do <b>Input()</b> através do <b>XPATH</b> e insere essa mesma palavra lá dentro e em seguida usando a   biblioteca do <b>Pyautogui</b> pressinamos a tecla <b>'space'</b>, fazendo com que no próximo loop a "palavra da vez" seja a próxima.
  <p>
    <br>
    <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/Automation/Sites/0001%2010%20Fast%20Fingers/%26%20-%20Image/automate%20fast%20fingers.gif">
  </p>
</p>
<hr>
<p>
  <h3>◻ Resultado</h3>
  <p>Após o loop acabar, ainda usando o <b>Selenium</b> verificamos <b>PPM (Palavras por minuto), Telcadas, Precisão, Palavras Certas e Errads.</b></p>
  <p>
    <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/Automation/Sites/0001%2010%20Fast%20Fingers/%26%20-%20Image/result%20automation.gif">
  </p>
</p>
<hr>
<p>
  <h3>◻ Dificuldades</h3>
  O único problema foi saber por quanto tempo eu deixaria o Loop rodando, pois mesmo que que eu fizesse uma varredura para cada palavra   e fizesse um <b>Loop For</b> nesse <b>range()</b>, ele continuaria rodando mesmo após o tempo limite de 1 minuto, pois o limite é de   aproximadamente 300 palavras por minuto, assim o Loop ficaria rodando por mais um tempo até finalizar. O ideal era deixar o Loop       rodando durante 1 minuto, e nesse intervalo o computador poderia continuar fazendo quantas palavras ele conseguisse. Eu até pensei em   fazer uma <b>Thread</b> que durasse 1 minuto e quando essa Thread acabasse eu colocaria um Break no While True, e aí o programa já     poderia coletar os dados da estatística final.
</p>
<hr>
<p>
  <h3>Comparação → Humano 👨‍💻 Vs Computador 🖥</h3>
  Vale ressaltar que a velocidade dos dois gifs são menores, mas obviamente não tem nem como comparar o desempenho contra o computador.
  <p>
    <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/Automation/Sites/0001%2010%20Fast%20Fingers/%26%20-%20Image/human%20score.gif" align="left" width=150>
    <img src="https://github.com/franssa01/Projects/blob/main/Python%20Projects/Automation/Sites/0001%2010%20Fast%20Fingers/%26%20-%20Image/human%20typing.gif" align="right" width=800>
  </p>
</p>
</div>
