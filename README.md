# WebcamSecurity
Projeto em python para usar a webcam como câmera de segurança com detecção de movimento.

Fiquei preocupado com a segurança quando tinha alugado a casa, eu tinha q ir trabalhar todos os dias deixando a casa apenas na fé. Se alguém entrasse despercebido na casa e levasse o Notebook, eu saberia quem foi / teria alguma informação, porque eu deixava rodando nas pastas do Google Drive com todas as gravações. Então no trabalho mesmo eu poderia ver quem foi.<br>
Vou deixar esses códigos aqui como portfólio e caso alguém ache interessante usar, pode baixar e editar também.<br>
<br>
<b>Dependencias: Python3, Opencv2, Pynput, Numpy.</b><br>
A combinação para parar a gravação é CTRL_LEFT + ALT_LEFT + SHIFT (não necessariamente nesta ordem)<br>
Como gravar o tempo todo gastaria uma grande quantidade de memória em um curto período, programei também detecção de movimento. A função <b>motionDetect</b> dentro da classe <b>Webcam</b>. Se passasse um inseto na frente por milésimos de segundos ele começava a gravar e terminava em 3 segundos, caso não ouvesse outro movimento na camera.<br>
O arquivo Microphone.py (não finalizado) ainda estava em desenvolvimento porque não havia tanta necessidade quanto o vídeo e o microfone do notebook também não ajudava muito, mas comecei a codar porque poderia ser uma informação a mais que poderia coletar (Nomes talvez, etc).
