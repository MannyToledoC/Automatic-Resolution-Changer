import PySimpleGUIQt as sg
import GUIFunctions  as gf
import threading
import windowchanger
import sys
import SystemMenuGUI
from ProcessEntity import ProcessEntity


sg.change_look_and_feel('black')

# implement a no windows title bar
column = [[sg.Text('Add a Process')],
          [sg.Text('Process Name')],
          [sg.Input(key='_NINPUT_')],
          [sg.Text('Process Name')],
          [sg.Combo(['2560 x 1440', '1920 x 1080'], enable_events=True, key='_RES_'), sg.Submit(key='_SUBMIT_')],
          [sg.Button('Minimize', key='__MINIMIZE__')]
          ]

column2 = [[sg.Text('View Saved')],
           [sg.Multiline(gf.read_from_data(), disabled=True, size=(45,5), key='_DISPLAYSETTINGS_')],
           [sg.Button('Clear', key='_CLEARBUTTON_')]
           ]

layout  = [[sg.Column(column), sg.VerticalSeparator(pad=None) , sg.Column(column2)],
           ]

tray = sg.SystemTray(menu= ['menu',['Open', 'E&xit']], filename=r'cat.ico')

window = sg.Window('Resolution Manager').Layout(layout)


x = threading.Thread(target=windowchanger.run, daemon='True')
x.start()



while True:
    event, values = window.Read()  
    tray_event = tray.Read(timeout=0.8)
    print(tray_event)
    
    if event == None:
        sys.exit(0)
        break
    if event == '__MINIMIZE__':
        window.hide()
    if event == '_SUBMIT_':
        res_tuple = gf.determine_resolution(values['_RES_'])
        p = ProcessEntity(values['_NINPUT_'], res_tuple[0], res_tuple[1] )
        gf.add_process_entity(p)
        window.Element('_NINPUT_').Update('')
        window.Element('_RES_').Update('')
        window.Element('_DISPLAYSETTINGS_').Update(gf.read_from_data())

    if event == '_CLEARBUTTON_':
        gf.clear_data()
        window.Element('_DISPLAYSETTINGS_').Update(gf.read_from_data())

    if tray_event == 'Exit':
        sys.exit(0)
        break
    if tray_event == 'Open' or tray_event == '__ACTIVATED__':
        window.UnHide()