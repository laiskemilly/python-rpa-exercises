import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm('Clique no botão desejado', buttons = ['Calculadora', 'Wordpad', 'Notepad'])

if opcao == "Calculadora":
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('calc')
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')

elif opcao == "Wordpad":
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('wordpad')
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')    
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Abrindo wordpad com script')

elif opcao == "Notepad":
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('notepad')
    escolha_opcao.sleep(2)
    escolha_opcao.press('enter')    
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Abrindo notepad com script')
