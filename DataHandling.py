import json
from ProcessEntity import ProcessEntity

# https://realpython.com/python-json/
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

def data_setup():
    # buf = ProcessEntity('Base', 3, 3)
    default = {}
    default['process'] = []
    # default['process'].append(buf.__dict__)
    
    with open('data.json', 'w') as outfile:
        json.dump(default, outfile, indent=4)

def clear():
    open('data.json', 'w').close()
    data_setup()

def store_info(processentity):
    with open('data.json') as f:
        data = json.load(f)

    data['process'].append(processentity.__dict__)

    with open('data.json', 'w') as f:
       f.write(json.dumps(data, indent=4))
    
def read_info():
    processnamelist = []
    with open('data.json') as json_file:
        data = json.load(json_file)
        for p in data['process']:
            '''
            print('Process Name: ' + p['processname'])
            print('Resolution: ' + str(p['width']) + ' x ' + str(p['length']))
            print('')
            '''
            processnamelist.append(ProcessEntity(p['processname'], p['width'], p['length']))
    return processnamelist

read_info()