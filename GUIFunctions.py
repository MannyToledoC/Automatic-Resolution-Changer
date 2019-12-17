from ProcessEntity import ProcessEntity


import DataHandling as dh


def add_process_entity(process):
    dh.store_info(process)

def determine_resolution(s):
    if s == '2560 x 1440':
        return (2560, 1440)

    elif s == '1920 x 1080':
        return (1920, 1080)
    
    else:
        print('error')
        return (None, None)

def read_from_data():
    plist = dh.read_info()
    pstring = ''
    for i in plist:
        # change this ugly thing later
        buff = i.get_processname()
        buff2 = i.get_width()
        buff3 = i.get_length()
        pstring += ('Process Name: ' + buff + '\nResolution: ' + str(buff2)
                             + ' x ' + str(buff3) + '\n\n')

    return pstring


def clear_data():
    dh.data_setup()