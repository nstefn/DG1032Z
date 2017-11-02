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

    
    def __write_string(self, cmd):
        super(DG1032Z, self).write(cmd)

    
    def generate_signal(self, output, signal, freq, ampl, offset, phase):
        self.__write_string(':{}:APPL:{} {},{},{},{}'.format(output, signal, freq, ampl, \
                offset, phase))
    
    def set_voltage_unit(self, output, unit):
        self.__write_string(':SOUR{}:VOLT:UNIT {}'.format(output, unit))


    def start_output(self, output):
        if output == 1:
            self.__write_string(':OUTP1 ON')
        else:
            self.__write_string(':OUTP2 ON')


    def stop_output(self, output):
        if output == 1:
            self.__write_string(':OUTP1 OFF')
        else:
            self.__write_string(':OUTP2 OFF')

    
    def get_dev_id(self):
        self.__write_string('*IDN?')

    
    def check_conn(self):
        try:
            self.get_dev_id()
        except:
            print('Unknown error occured')

    
