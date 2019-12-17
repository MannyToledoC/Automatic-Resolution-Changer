#!/usr/bin/hello

import psutil
import time
import os
import sys 
import ScreenRes
import DataHandling as dh
"""
https://psutil.readthedocs.io/en/latest/
https://stackoverflow.com/questions/20838201/resize-display-resolution-using-python-with-cross-platform-support

"""
# change from string to processentity.name
def system_house_keeping(name):
    print(os.getpid())
    # TODO: setup the python system task bar

# redundant function
def is_process_running(processes):
    for p in psutil.process_iter(attrs=['name']):
        for pname in processes:
            if p.info['name'] == pname.get_processname():
                return True
    return False


# returns a dictionary list with the process entity and its pid
def get_process_info(processes):
    processesinfo = []
    for p in psutil.process_iter(attrs=['name', 'pid']):
        for pname in processes:
            if p.info['name'] == pname.get_processname():
                processesinfo.append({'ProcessEn': pname, 'pid': p.info['pid']})
    return processesinfo

def is_still_running(processes):
    if psutil.pid_exists(processes.get("pid")):
        print("RUNNING\nProcess: " + processes.get('ProcessEn').get_processname() + " PID: " + str(processes.get('pid')))
        return True
    else:
        print("NOT RUNNING\nProcess: " + processes.get('ProcessEn').get_processname() + " PID: " + str(processes.get('pid')))
        return False

def get_processes():
    plist = dh.read_info()
    return plist  

def run():
    system_house_keeping("WindowChanger")
    running = False
    
    # game_process_names = ["RainbowSix_BE.exe"]
    
    processes_running = []
    
    while(True):
        time.sleep(0.8)
        terminated = True
        for i in get_processes():
            print("Looking for processes " + i.get_processname())

        # processes_running = get_process_info(game_process_names)
        processes_running = get_process_info(get_processes())

        for i in processes_running:
            if i.get('ProcessEn').get_width() == 1920:
                ScreenRes.to1080()
                running = True
                terminated = False

        '''
        #implement a for loop to change screen based on resolution
        if(processes_running):
            ScreenRes.to1080()
            running = True
            terminated = False
        '''

        while(not terminated):
            time.sleep(0.8)
            for p in processes_running:
                if(is_still_running(p)):
                    x = 1
                else:
                    print("Succesfull")
                    ScreenRes.to2k()
                    terminated = True
            

    
