
# create a file for storing a process name with its resolution wanted.

# view current resolution
# then change to wanted resolution



class ProcessEntity:

    def __init__(self, processname, width, length):
        self.processname = processname
        self.width = width
        self.length = length
        self.info = {'name': processname, 'width':width,
                        'length': length}


    def get_processname(self):
        return self.processname

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length
    
    def get_info(self):
        return self.info
        

