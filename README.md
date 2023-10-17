# WebcamSecurity
Projeto em Python para usar a webcam como câmera de segurança com detecção de movimento.

Fiquei preocupado com a segurança quando tinha alugado a casa, eu tinha q ir trabalhar todos os dias deixando a casa apenas na fé. Se alguém entrasse despercebido na casa e levasse o Notebook, eu saberia quem foi / teria alguma informação, porque eu deixava rodando nas pastas do Google Drive com todas as gravações. Então no trabalho mesmo eu poderia ver quem foi.<br>
Vou deixar esses códigos aqui como portfólio e caso alguém ache interessante usar, pode baixar e editar também.<br>
<br>
<b>Dependencias: Python3.11.6, Opencv2, Pynput, Numpy, Wave, PyAudio.</b><br>
As gravações ficam todas salvas na pasta <b>recs</b>, e a combinação para parar a gravação é <b>CTRL_LEFT + ALT_LEFT + SHIFT</b> (não necessariamente nesta ordem)<br>
Como gravar o tempo todo gastaria uma grande quantidade de memória em um curto período, programei também detecção de movimento. A função <b>motionDetect</b> dentro da classe <b>Webcam</b>. Se passasse um inseto na frente por milésimos de segundos ele começava a gravar e terminava em 3 segundos, caso não ouvesse outro movimento na camera.<br>
<s>O arquivo Microphone.py (não finalizado) ainda estava em desenvolvimento porque não havia tanta necessidade quanto o vídeo e o microfone do notebook também não ajudava muito, mas comecei a codar porque poderia ser uma informação a mais que poderia coletar (Nomes talvez, etc).</s><br>
Criei uma função para gravar o audio com PyAudio, so que o tempo todo, porque não consegui decodificar os bytes muito bem (arquivo Microphone.py linhas 62, 63, 64 comentadas), ele grava e salva o que foi gravado a cada 10 segundos. Eu tinha criado uma função de detectar som e gravar, mas foi com a biblioteca sounddevice e os dados eram números, então era mais fácil ler.
Tive dificuldades para instalar o PyAudio no Windows 10.
