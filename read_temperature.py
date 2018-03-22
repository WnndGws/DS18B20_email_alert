#!/usr/bin/python3
##
import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
xxxx_magic_number_xxxx = '28'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines

def read_temp():
    '''
    Successful response: '...YES t=31.25'?
    Failed response: '...NO...'?
    '''
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)  # need to wait for DS18B20 to finish ADC conversion
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

if __name__ == '__main__':
    while True:
        print(read_temp())
        time.sleep(1)
