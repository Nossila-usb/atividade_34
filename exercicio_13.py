
import pyautogui as auto


auto.PAUSE = 0.6

auto.press('win') #abre o menu iniciar
auto.write('chrome') #digita a palavra chrome
auto.press('enter') #aperta enter

#maximizar a tela, a janela do chrome
auto.hotkey('alt','space')    #hotkey = para usar tecla de atalho     
auto.press('x') #aperta enter

#entrar na pagina do yotube
auto.write('youtube.com') #digita youtube.com
auto.press('enter') #aperta enter

#apertar tab ate chegar na parte de digitar
for i in range(4):
    auto.press('tab')

#pesquisar Aulas de Python na busca
auto.write('Aulas de Python')

auto.press('enter') #aperta enter