import PySimpleGUI as sg 
import GUIFunctions  as gf
import threading
import windowchanger
import sys
import SystemMenuGUI as tray
from ProcessEntity import ProcessEntity

def system_end():
    sys.exit()

sg.change_look_and_feel('black')

# implement a no windows title bar
column = [[sg.Text('Add a Process')],
          [sg.Text('Process Name')],
          [sg.Input(key='_NINPUT_')],
          [sg.Text('Process Name')],
          [sg.Combo(['2560 x 1440', '1920 x 1080'], enable_events=True, key='_RES_'), sg.Submit(key='_SUBMIT_')]
          ]

column2 = [[sg.Text('View Saved')],
           [sg.Multiline(gf.read_from_data(), disabled=True, size=(45,5), key='_DISPLAYSETTINGS_')],
           [sg.Button('Clear', key='_CLEARBUTTON_')]
           ]

layout  = [[sg.Column(column), sg.VerticalSeparator(pad=None) , sg.Column(column2)],
           ]

view_layout = [[sg.Text('Hello')]]

window = sg.Window('Resolution Manager').Layout(layout)


# add file save
# maybe use json
# Combo Element

x = threading.Thread(target=windowchanger.run, daemon='True')
x.start()

tray.run(window)


while True:
    event, values = window.Read()  
    
    if event == None:
        break

    if event == '_SUBMIT_':
        res_tuple = gf.determine_resolution(values['_RES_'])
        p = ProcessEntity(values['_NINPUT_'], res_tuple[0], res_tuple[1] )

        print(p.get_info())
        gf.add_process_entity(p)
        window.Element('_NINPUT_').Update('')
        window.Element('_RES_').Update('')
        # window.Element('_DISPLAYSETTINGS_').Update(gf.read_from_data().get_info())
        window.Element('_DISPLAYSETTINGS_').Update(gf.read_from_data())

    if event == '_CLEARBUTTON_':
        gf.clear_data()
        window.Element('_DISPLAYSETTINGS_').Update(gf.read_from_data())
