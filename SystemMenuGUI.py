import PySimpleGUIQt as sg
import time

# https://github.com/PySimpleGUI/PySimpleGUI/issues/1965



def run(window):
    # tray = sg.SystemTray(menu= ['menu',['Open', ['&Save::KEY', '---', 'Issues', '!Disabled'], 'E&xit']])
    # tray.ShowMessage('My Message', 'Resolution Manager is now running!')
    tray = sg.SystemTray(menu= ['menu',['Open', 'E&xit']])
    while True:
        time.sleep(0.8)
        event = tray.Read()
        print(event)
        if event == 'Exit':
            break
        if event == 'Open' or event == '__ACTIVATED__':
            window.close()
