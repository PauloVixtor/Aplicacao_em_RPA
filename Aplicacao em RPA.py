import pyautogui
import PySimpleGUI as sg

sg.theme('Reddit') # Tema escolhido


layout = [ # Criando layout
    [sg.Text('Usuario: '), sg.Input(key='usuario', size=(20, 1))], # Texto e informação a ser inserida com chave de localização, Tamanho
    [sg.Text('  Senha: '), sg.Input(key='senha', password_char='*', size=(20, 1))], # Texto, escrever, chave e proteção de dados, Tamanho
    [sg.Checkbox('Salvar o Login:')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout=layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'teste' and valores['senha'] == '123':
            sg.popup('Seja Bem-vindo!')
            janela.close()
            pyautogui.alert('O codigo vai ser executado na sua maquina, por favor não aperte nada!')
            pyautogui.PAUSE = 1.8
            pyautogui.press('win')
            pyautogui.write('chorme')
            pyautogui.press('enter')
            pyautogui.write('Qual definicao de RPA em python')
            pyautogui.press('enter')
            pyautogui.press('f11')
            pyautogui.mouseDown(187, 202)
            for c in range(0, 4):
                pyautogui.hotkey('shift', 'down')
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.sleep(1)
            pyautogui.mouseUp(187, 202)
            pyautogui.hotkey('alt', 'f4')
            pyautogui.sleep(1)
            pyautogui.press('win')
            pyautogui.write('bloco')
            pyautogui.press('enter')
            pyautogui.write('       Qual definicao de RPA em python?')
            pyautogui.press('enter')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('ctrl', 's')
            pyautogui.write('RPA_Aplicacoes')
            pyautogui.press('enter')
            pyautogui.hotkey('alt', 'f4')
            pyautogui.alert('Teste finalizado com sucesso!')
            # print(pyautogui.position())
        else:
            sg.popup('Senha ou Login incorreto. Por favor, informe novamente!')