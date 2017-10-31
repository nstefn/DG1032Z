#!/usr/bin/env python

# Python module for controlling signal generator rigol dg1032z 
# 

'''

'''

import vxi11


class DG1032Z(vxi11.Instrument):

    def __init__(self, '192.168.2.72'):
        
        super(DG1032Z, self).__init__(host)

    
    def write_string(self, cmd):
        super(DG1032Z, self).write(cmd)

    
    def gen_signal(self, output, signal, freq, ampl, offset, phase):
        self.write_string(':{}:{}:{} {},{},{}'.format(output, signal, freq, ampl, \
                offset, phase))
    
    
    def get_dev_id(self):
        self.write_string('*IDN?')

    
    def check_conn(self):
        self.get_dev_id()


def main():
    instrInst = DG1032Z('192.168.2.72')
    
    try:
        instrInst.write_string("*IDN?\n\n\n")

        instrInst.write_string(':SOUR1:APPL:SIN 1000,0.1,0,0')
    
    except:
        print('error')

    raw_input("Press any key to continue\n\n")
    instrInst.write_string(':SOUR1:APPL:SIN 1000,1,0,0')

