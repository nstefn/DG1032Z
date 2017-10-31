#!/usr/bin/env python

# Python module for controlling signal generator rigol dg1032z 
# 

'''

'''

import vxi11


class DG1032Z(vxi11.Instrument):

    def __init__(self, host):
        self.host = host
        super(DG1032Z, self).__init__(self.host)

    
    def write_string(self, cmd):
        super(DG1032Z, self).write(cmd)

    
    def gen_signal(self, output, signal, freq, ampl, offset, phase):
        self.write_string(':{}:{}:{} {},{},{}'.format(output, signal, freq, ampl, \
                offset, phase))
    
    
    def get_dev_id(self):
        self.write_string('*IDN?')

    
    def check_conn(self):
        try:
            self.get_dev_id()
        except:
            print('Unknown error occured')

    
